from django.urls import path

from .views import RegisterView, home

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
]
