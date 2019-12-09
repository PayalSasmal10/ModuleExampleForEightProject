from django.urls import path
from . import views

urlpatterns = [
    path('emp/', views.emplyoee_info_view),
]