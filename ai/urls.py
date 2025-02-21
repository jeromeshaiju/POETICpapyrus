from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstview, name='home'),
    path('peom-generating/', views.process_input_view, name='process-input'),
]