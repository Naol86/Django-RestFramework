from rest_framework.response import Response
from rest_framework.decorators import api_view

import json
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request):
  """
  DRF API view
  """
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
    data = ProductSerializer(instance).data
  return Response(data)

@api_view(["GET"])
def index(request):
  return Response({"data":[{"name":"naol"}, {"name":"hana"}]})