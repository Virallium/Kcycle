from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CycleMenstruel, Menstruation, RessentirSymptome, Symptome
from .serializers import (
	CycleMenstruelSerializer,
	MenstruationSerializer,
	RessentirSymptomeSerializer,
	SymptomeSerializer,
)


class CycleMenstruelViewSet(viewsets.ModelViewSet):
	serializer_class = CycleMenstruelSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return CycleMenstruel.objects.filter(user=self.request.user)


class MenstruationViewSet(viewsets.ModelViewSet):
	serializer_class = MenstruationSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Menstruation.objects.filter(
			cycle__user=self.request.user
		).select_related('cycle')


class RessentirSymptomeViewSet(viewsets.ModelViewSet):
	serializer_class = RessentirSymptomeSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return RessentirSymptome.objects.filter(
			menstruation__cycle__user=self.request.user
		).select_related('menstruation', 'symptome')


class SymptomeViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Symptome.objects.all()
	serializer_class = SymptomeSerializer
	permission_classes = (IsAuthenticated,)
