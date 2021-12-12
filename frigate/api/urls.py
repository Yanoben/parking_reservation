from .views import bookings, bookings_detail
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('v1/bookings/', bookings),
    path('v1/bookings/<int:park_id>/', bookings_detail),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
