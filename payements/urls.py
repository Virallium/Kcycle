from rest_framework.routers import DefaultRouter

from .views import AbonnementViewSet, PayementViewSet

router = DefaultRouter()
router.register('abonnements', AbonnementViewSet, basename='abonnement')
router.register('transactions', PayementViewSet, basename='payement')

urlpatterns = router.urls
