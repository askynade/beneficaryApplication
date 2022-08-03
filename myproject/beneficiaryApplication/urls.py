from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ApplicationViewSet', ApplicationViewSet)
urlpatterns=[
    path('application',CreateApplicationAPI.as_view(),name="userlogin"),
    path('', include(router.urls))
    
]

