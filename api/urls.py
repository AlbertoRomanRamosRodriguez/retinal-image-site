from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'ofundus', views.OFViewSet, basename='ofundus')

urlpatterns = [
    path('', views.home, name=''),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)