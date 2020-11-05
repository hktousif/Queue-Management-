from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('allauth.urls')),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls'))
]
