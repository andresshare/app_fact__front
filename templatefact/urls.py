from django.urls import include, path

from templatefact.views import Home

urlpatterns = [
    path('',Home.as_view(), name='home'),
    
]
