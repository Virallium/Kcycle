from rest_framework.routers import DefaultRouter

from .views import PartenairesViewSet, ProgrammeViewSet, SponsorisationViewSet

router = DefaultRouter()
router.register('partenaires', PartenairesViewSet, basename='partenaire')
router.register('programmes', ProgrammeViewSet, basename='programme')
router.register('sponsorisations', SponsorisationViewSet, basename='sponsorisation')

urlpatterns = router.urls
