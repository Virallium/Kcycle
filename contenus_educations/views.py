from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Categorie, Consultation, ContenuEducatif
from .serializers import (
	CategorieSerializer,
	ConsultationSerializer,
	ContenuEducatifSerializer,
)


class AdminWriteViewSet(viewsets.ModelViewSet):
	def get_permissions(self):
		permission_class = (
			IsAdminUser
			if self.action in ('create', 'update', 'partial_update', 'destroy')
			else IsAuthenticated
		)
		return (permission_class(),)


class CategorieViewSet(AdminWriteViewSet):
	queryset = Categorie.objects.all().order_by('name')
	serializer_class = CategorieSerializer


class ContenuEducatifViewSet(AdminWriteViewSet):
	queryset = ContenuEducatif.objects.select_related('categorie').all()
	serializer_class = ContenuEducatifSerializer


class ConsultationViewSet(viewsets.ModelViewSet):
	serializer_class = ConsultationSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Consultation.objects.filter(user=self.request.user).select_related(
			'contenu_educ'
		)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
