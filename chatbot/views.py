from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Conversation
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
	serializer_class = ConversationSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Conversation.objects.filter(user=self.request.user).prefetch_related('messages')

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	@action(detail=True, methods=('get', 'post'))
	def messages(self, request, pk=None):
		conversation = self.get_object()

		if request.method == 'GET':
			messages = conversation.messages.all()
			serializer = MessageSerializer(
				messages,
				many=True,
				context=self.get_serializer_context(),
			)
			return Response(serializer.data)

		serializer = MessageSerializer(
			data=request.data,
			context=self.get_serializer_context(),
		)
		serializer.is_valid(raise_exception=True)
		serializer.save(conversation=conversation, sender='user')
		return Response(serializer.data, status=status.HTTP_201_CREATED)
