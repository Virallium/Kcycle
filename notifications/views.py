from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Reception
from .serializers import ReceptionSerializer


class ReceptionViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = ReceptionSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Reception.objects.filter(user=self.request.user).select_related(
			'notification'
		)

	@action(detail=True, methods=('post',), url_path='mark-read')
	def mark_read(self, request, pk=None):
		reception = self.get_object()
		reception.is_read = True
		reception.save(update_fields=('is_read',))
		return Response(self.get_serializer(reception).data, status=status.HTTP_200_OK)
