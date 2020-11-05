from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from clients.views import ClientView

router = routers.DefaultRouter()
router.register('', ClientView)
urlpatterns = router.urls
