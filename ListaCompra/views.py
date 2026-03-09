from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, ShoppingList, ShoppingListItem
from .serializers import (ProductSerializer, ShoppingListSerializer, ShoppingListItemSerializer)

# ==============================
# SHOPPING LISTS

@api_view(["POST"])
def CreateListView(request):

    if request.method == 'POST':
        serializer = ShoppingListSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetListView(request):

    if request.method == 'GET':
        try:
            lists = ShoppingList.objects.all().order_by("-created_at")
        except ShoppingList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingListSerializer(lists, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def CompleteListView(request, list_id):

    if request.method == 'PATCH':
        try:
            shopping_list = ShoppingList.objects.get(pk=list_id)
        except ShoppingList.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        shopping_list.completed = True
        shopping_list.save()

        serializer = ShoppingListSerializer(shopping_list)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# ==============================
# PRODUCTS

@api_view(["POST"])
def CreateProductView(request):

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetProductsView(request):

    if request.method == 'GET':
        search = request.query_params.get("search")

        try:
            products = Product.objects.all().order_by("name")
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if search:
            products = products.filter(name__icontains=search)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


# ==============================
# SHOPPING LIST ITEMS

@api_view(["POST"])
def AddProductToListView(request):

    if request.method == 'POST':
        serializer = ShoppingListItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetListItemsView(request, list_id):

    if request.method == 'GET':
        try:
            items = ShoppingListItem.objects.filter(shopping_list_id=list_id)
        except ShoppingListItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingListItemSerializer(items, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PATCH"])
def UpdateListItemView(request, item_id):

    if request.method == 'PATCH':
        try:
            item = ShoppingListItem.objects.get(id=item_id)
        except ShoppingListItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingListItemSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def DeleteListItemView(request, item_id):

    if request.method == 'DELETE':
        try:
            item = ShoppingListItem.objects.get(id=item_id)
        except ShoppingListItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_400_BAD_REQUEST)