from rest_framework.routers import DefaultRouter

from .views import (
	CycleMenstruelViewSet,
	MenstruationViewSet,
	RessentirSymptomeViewSet,
	SymptomeViewSet,
)

router = DefaultRouter()
router.register('cycles', CycleMenstruelViewSet, basename='cycle-menstruel')
router.register('menstruations', MenstruationViewSet, basename='menstruation')
router.register(
	'symptomes-ressentis',
	RessentirSymptomeViewSet,
	basename='symptome-ressenti',
)
router.register('symptomes', SymptomeViewSet, basename='symptome')

urlpatterns = router.urls
