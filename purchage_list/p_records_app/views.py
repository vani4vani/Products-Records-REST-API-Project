from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import *
from .serializers import ProductItemSerializer
from .models import ProductItem


# Create your views here.

class ProductItemViews(APIView):

     def get(self, request, id=None):
        if id:
            item = ProductItem.objects.get(id=id)
            serializer = ProductItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ProductItem.objects.all()
        serializer = ProductItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

     def post(self, request):
        serializer = ProductItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

     def patch(self, request, id=None):
        item = ProductItem.objects.get(id=id)
        serializer = ProductItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request, id=None):
        item = get_object_or_404(ProductItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
