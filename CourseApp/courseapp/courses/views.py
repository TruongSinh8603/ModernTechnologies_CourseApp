from rest_framework import viewsets, generics
from courses import serializers
from courses.models import Category

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
