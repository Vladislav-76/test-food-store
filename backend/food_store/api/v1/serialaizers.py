from rest_framework import serializers

from goods.models import Category, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    """Сериализатор подкатегории."""

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug_name', 'image')


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор категории."""

    subcategories = SubcategorySerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug_name', 'image', 'subcategories')
