from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePages.as_view())
]
