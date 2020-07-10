from django.urls import path
from rest_framework.routers import DefaultRouter


from . import views

urlpatterns = [
    path('api-view-features/', views.APIViewFeatures.as_view())
]
