from django.urls import path

from api.v1.views import CategoryListView


urlpatterns = [
    path('categories/', CategoryListView.as_view()),
]