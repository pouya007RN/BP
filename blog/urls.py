from rest_framework import routers
from .views import ContentRateViewSet, ContentViewSet

router = routers.SimpleRouter()
router.register('contents', ContentViewSet, basename='contents')
router.register('rate', ContentRateViewSet, basename='rate')

urlpatterns = [

]

urlpatterns += router.urls