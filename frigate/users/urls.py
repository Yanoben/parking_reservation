from django.urls import path

from .views import RegisterView, home, create_park, change_park, delete_park

urlpatterns = [
    path('', home, name='users-home'),
    path('create-park/', create_park, name='create_park'),
    path('delete-park/<int:park_id>/', delete_park, name='delete_park'),
    path('change-park/<int:park_id>/', change_park, name='change_park'),
    path('register/', RegisterView.as_view(), name='users-register'),
]
