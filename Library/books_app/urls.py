from django.urls import path, include
from rest_framework import routers, urlpatterns
from rest_framework.viewsets import ViewSet
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('bookapi', viewset=views.BookViewset, basename='book')


urlpatterns = [
    path('', include(router.urls))
]
