from rest_framework import generics, mixins, viewsets, permissions

from .models import Product
from .serializers import ProductSerializer


class ProductMixins(
  # viewsets.GenericViewSet,
  # mixins.ListModelMixin,
  # mixins.RetrieveModelMixin,
  # mixins.CreateModelMixin,
  # mixins.UpdateModelMixin,
  # mixins.DestroyModelMixin,
  # generics.GenericAPIView
  viewsets.ModelViewSet
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'
  authentication_classes = [auth]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  # def get(self, request, *args, **kwargs):
  #   pk = kwargs.get('pk')
  #   if pk:
  #     return self.retrieve(request, *args, **kwargs)
  #   return self.list(request, *args, **kwargs)

  # def post(self, request, *args, **kwargs):
  #   return self.create(request, *args, **kwargs)

  def perform_create(self, serializer):
    data = serializer.validated_data
    content = data.get('content')
    if not content:
      content = "this is from model view set"
    serializer.save(content=content)
  
  # def put(self, request, *args, **kwargs):
  #   return self.update(request, *args, **kwargs)

  # def patch(self, request, *args, **kwargs):
  #   return self.partial_update(request, *args, **kwargs)

  # def destroy(self, request, *args, **kwargs):
  #   return self.destroy(request, *args, **kwargs)

product_mixins = ProductMixins

# class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer

# product_rud_view = ProductDetailAPIView.as_view()

# class ProductListCreateAPIView(generics.ListCreateAPIView):
#   queryset = Product.objects.all()
#   serializer_class = ProductSerializer
  
#   def perform_create(self, serializer):
#     data = serializer.validated_data
#     title = data.get('title')
#     content = data.get('content') or None
#     if content is None:
#       content = title
#     serializer.save(content=content)

# product_list_create_view = ProductListCreateAPIView.as_view()
