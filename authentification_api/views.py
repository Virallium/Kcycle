from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer, RegistrationSerializer


class RegistrationView(generics.CreateAPIView):
	serializer_class = RegistrationSerializer
	permission_classes = (AllowAny,)


class ProfileViewSet(viewsets.ModelViewSet):
	serializer_class = ProfileSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
