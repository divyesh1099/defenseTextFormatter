from django.urls import path
from . import views
app_name='home'

# Your Paths here
urlpatterns=[
    path('', views.index, name='index'),
    path('send_message', views.send_message, name='send_message'),
]
