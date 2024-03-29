from rest_framework import viewsets, generics, status, parsers
from courses import serializers, paginators
from courses.models import Category, Course, Lesson, User
from rest_framework.decorators import action
from rest_framework.views import Response

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries

    @action(methods=['get'], detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)

        return Response(serializers.LessonSerializer(lessons, many=True, context={'request': request}).data, status=status.HTTP_200_OK)

class LessonViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]