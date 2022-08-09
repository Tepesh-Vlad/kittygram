from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet

router = SimpleRouter()
router.register('cats', CatViewSet)
router.register('owner', OwnerViewSet)
router.register(r'mycats', LightCatViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
