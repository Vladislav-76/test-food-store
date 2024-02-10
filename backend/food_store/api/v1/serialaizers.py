from rest_framework import serializers

from goods.models import Category, Subcategory, UnitOfGoogs


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


class GoogsSerializer(serializers.ModelSerializer):
    """Сериализатор единицы товара."""

    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = UnitOfGoogs
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'subcategory',
            'price',
            'images',
        )

    def get_category(self, unit_of_goods):
        return {
            'name': unit_of_goods.subcategory.category.name,
            'slug_name': unit_of_goods.subcategory.category.slug_name,
        }

    def get_subcategory(self, unit_of_goods):
        return {
            'name': unit_of_goods.subcategory.name,
            'slug_name': unit_of_goods.subcategory.slug_name,
        }

    def get_images(self, unit_of_goods):
        request = self.context.get('request')
        images_url =  [
            unit_of_goods.image_small.url,
            unit_of_goods.image_average.url,
            unit_of_goods.image_big.url,
        ]
        return [
            request.build_absolute_uri(image_url)
            for image_url in images_url
        ]
