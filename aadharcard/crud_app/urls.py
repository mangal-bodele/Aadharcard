from django.urls import path
from .views import create_aadhar,show_aadhar,update_aadhar,delete_aadhar
urlpatterns = [
    path('create/',create_aadhar,name='create_url'),
    path('show/',show_aadhar,name='show_url'),
    path('update/<int:pk>/',update_aadhar,name='update_url'),
    path('delete/<int:pk>/',delete_aadhar,name='delete_url')
]