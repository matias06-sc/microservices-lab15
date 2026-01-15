from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @method_decorator(cache_page(60*2))  # cache 2 minutos
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
