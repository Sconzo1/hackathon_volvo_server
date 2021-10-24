from rest_framework import routers

from api.views import *

router = routers.DefaultRouter()
router.register(r'country', CountryView)
router.register(r'loc', LocationView)
router.register(r'travel', TravelView)
router.register(r'steptype', StepTypeView)
router.register(r'historytype', HistoryTypeView)
router.register(r'travelstep', TravelStepView)
router.register(r'tag', TagView)
router.register(r'car', CarView)
router.register(r'carissue', CarIssueView)
router.register(r'leveltag', LevelTagView)
router.register(r'usertravel', UserTravelView)
router.register(r'usertravelstep', UserTravelStepView)
router.register(r'userinsurance', UserInsuranceView)
router.register(r'usercar', UserCarView)
router.register(r'usercarhistory', UserCarHistoryView)
urlpatterns = router.urls
