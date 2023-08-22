from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.StuViewset import StuViewset
router=routers.DefaultRouter()
router.register(r'Virat',StuViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
