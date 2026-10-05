from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Abonnement, Payement
from .serializers import AbonnementSerializer, PayementSerializer


class AbonnementViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = AbonnementSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Abonnement.objects.filter(user=self.request.user)


class PayementViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = PayementSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Payement.objects.filter(
			abonnement__user=self.request.user
		).select_related('abonnement')
