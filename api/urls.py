from django.urls import path
from . import views

urlpatterns = [
    path('get_current_usd/', views.get_current_usd),
]
