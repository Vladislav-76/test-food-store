from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


from api.v1.serialaizers import CategorySerializer, GoogsSerializer
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

