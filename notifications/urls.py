from rest_framework.routers import DefaultRouter

from .views import ReceptionViewSet

router = DefaultRouter()
router.register('receptions', ReceptionViewSet, basename='reception')

urlpatterns = router.urls
