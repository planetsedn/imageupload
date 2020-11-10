from imagelabel import views
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'imagelabel', views.ImageUploadViewSet)

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('', RedirectView.as_view(url="api/")),
]