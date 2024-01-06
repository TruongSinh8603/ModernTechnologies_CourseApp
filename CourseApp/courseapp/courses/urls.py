from django.urls import path, include
from rest_framework import routers
from courses import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
