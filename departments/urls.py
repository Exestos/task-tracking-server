from rest_framework.routers import SimpleRouter

from .views import (
    UserModelViewSet,
    EmployeeModelViewSet,
    DepartmentModelViewSet,
    PositionModelViewSet
)

router = SimpleRouter()

router.register(r'user', UserModelViewSet)
router.register(r'employee', EmployeeModelViewSet)
router.register(r'department', DepartmentModelViewSet)
router.register(r'position', PositionModelViewSet)

urlpatterns = router.urls
