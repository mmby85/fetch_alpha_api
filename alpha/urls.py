from django.conf.urls import url, include
from .views import DataViewset, DataAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('data', DataViewset, basename='alpha-data')
# router.register('data', DataViewset.save_data_api, basename='force-alpha-data')


urlpatterns = [
    url('', include(router.urls)),
    url('create/', DataAPIView.as_view(), name="create")
]