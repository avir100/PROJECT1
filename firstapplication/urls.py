from django.urls import path
from firstapplication import views

urlpatterns = [
    path('', views.home_view, name='home'),
]