from rest_framework import routers
from .api import LeadViewSet
from .api import VaccineViewSet
from .api import MakersViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/vaccines', VaccineViewSet)
router.register('api/makers', MakersViewSet)

urlpatterns = router.urls
