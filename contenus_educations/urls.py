from rest_framework.routers import DefaultRouter

from .views import CategorieViewSet, ConsultationViewSet, ContenuEducatifViewSet

router = DefaultRouter()
router.register('categories', CategorieViewSet, basename='categorie')
router.register('contenus', ContenuEducatifViewSet, basename='contenu-educatif')
router.register('consultations', ConsultationViewSet, basename='consultation')

urlpatterns = router.urls
