from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    CreateModelMixin,
    ListModelMixin
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.v1.serialaizers import (
    CartSerializer,
    CategorySerializer,
    GoogsSerializer
)
from cart.models import Cart,CartGoods
from goods.models import Category, UnitOfGoogs


class CategoryListView(ListAPIView):
    """Отображение списка категорий с подкатегориями."""

    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Category.objects.all()


class GoodsListView(ListAPIView):
    """Отображение списка продуктов с категориями и подкатегориями."""

    serializer_class = GoogsSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return UnitOfGoogs.objects.all()


class CartViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """Операции с корзиной."""

    def list(self, request):
        """Отображение корзины."""
        user = self.request.user
        serializer = CartSerializer(Cart.objects.filter(owner=user), many=True)
        return Response(serializer.data)

    def create(self, request):
        """Добавление, изменение количества, удаление продуктов из корзины."""
        if error := self.validate_goods(request.data):
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        cart = Cart.objects.get_or_create(owner=self.request.user)[0]
        for item in request.data['goods']:
            unit_of_goods = get_object_or_404(UnitOfGoogs, id=item['id'])
            cart_goods = CartGoods.objects.get_or_create(
                cart=cart,
                unit_of_goods=unit_of_goods,
            )[0]
            if (amount := item['amount']) > 0:
                cart_goods.amount = amount
                cart_goods.save()
            else:
                cart_goods.delete()
        queryset = Cart.objects.filter(owner=self.request.user)
        return Response(CartSerializer(queryset, many=True).data)

    def destroy(self, request, pk=None):
        """Очистка корзины."""
        get_object_or_404(Cart, owner=self.request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def validate_goods(data):
        if not isinstance(data, dict) or not 'goods' in data:
            return {'Ошибка': '"goods": "Обязательное поле."'}
        if not all(
            {'id', 'amount'}.issubset(item.keys()) for item in data['goods']
        ):
            return {'Ошибка': 'id, amount: Обязательные поля.'}
        for item in data['goods']:
            if not all(isinstance(value, int) for value in item.values()):
                return {'Ошибка': 'id, amount: Целые числа.'}
