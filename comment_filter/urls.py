from rest_framework import routers
from comment_filter.api.views import FilterViewSet

router = routers.DefaultRouter()
router.register(r'filter', FilterViewSet, base_name='filter')
urlpatterns = router.urls