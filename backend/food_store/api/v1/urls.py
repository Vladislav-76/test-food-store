from django.urls import path

from api.v1.views import CategoryListView, GoodsListView


urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('goods/', GoodsListView.as_view()),
]