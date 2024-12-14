from rest_framework.routers import DefaultRouter
from .views import PortfolioViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'portfolios', PortfolioViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls
