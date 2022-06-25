from rest_framework.routers import SimpleRouter

from .views import (
    WorkCategoryModelViewSet,
    WorkTypeModelViewSet,
    TimeLineModelViewSet
)

router = SimpleRouter()

router.register(r'workcategory', WorkCategoryModelViewSet)
router.register(r'worktype', WorkTypeModelViewSet)
router.register(r'timeline', TimeLineModelViewSet)

urlpatterns = router.urls
