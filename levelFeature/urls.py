from django.urls import path
from . import views

urlpatterns = [
    path('get_latest/', views.get_latest, name='get_latest'),
]
