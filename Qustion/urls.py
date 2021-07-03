from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),
   path('detail/<int:pk>', views.detail, name='detail'),
   path('add_school/', views.add_school, name='add_school'),
]