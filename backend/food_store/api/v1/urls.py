from django.urls import include, path

from api.v1.routers import CustomCartRouter
from api.v1.views import CartViewSet, CategoryListView, GoodsListView


router = CustomCartRouter()
router.register('cart', CartViewSet, basename='cart')

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('goods/', GoodsListView.as_view()),
    path('', include(router.urls)),
]