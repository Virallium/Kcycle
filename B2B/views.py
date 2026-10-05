from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Partenaires, Programme, Sponsorisation
from .serializers import (
	PartenairesSerializer,
	ProgrammeSerializer,
	SponsorisationSerializer,
)


class PartenairesViewSet(viewsets.ModelViewSet):
	serializer_class = PartenairesSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Partenaires.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ProgrammeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Programme.objects.all()
	serializer_class = ProgrammeSerializer
	permission_classes = (IsAuthenticated,)


class SponsorisationViewSet(viewsets.ModelViewSet):
	serializer_class = SponsorisationSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Sponsorisation.objects.filter(
			partenaire__user=self.request.user
		).select_related('partenaire', 'programme')
