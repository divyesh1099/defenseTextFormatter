from django.urls import path
from . import views
app_name='home'

# Your Paths here
urlpatterns=[
    path('', views.index, name='index'),
    path('download_document/<path:doc_path>/', views.download_document, name='download_document'),
]
