from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySereializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySereializer
    queryset = Category.objects.all()
