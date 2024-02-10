from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny


from api.v1.serialaizers import CategorySerializer
from goods.models import Category


class CategoryListView(ListAPIView):
    """Отображение списка категорий с подкатегориями."""

    serializer_class = CategorySerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Category.objects.all()

