from django.db.models import F
from rest_framework import serializers

from cart.models import Cart
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
        images_url = [
            unit_of_goods.image_small.url,
            unit_of_goods.image_average.url,
            unit_of_goods.image_big.url,
        ]
        return [
            request.build_absolute_uri(image_url)
            for image_url in images_url
        ]


class CartSerializer(serializers.ModelSerializer):
    """ Сериализатор корзины."""

    owner = serializers.StringRelatedField()
    goods = serializers.SerializerMethodField()
    total_amount = serializers.SerializerMethodField()
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'owner', 'goods', 'total_amount', 'total_sum')

    def get_goods(self, cart):
        return cart.goods.values(
            'id',
            'name',
            'price',
            amount=F('cart__amount'),
        )

    def get_total_amount(self, cart):
        return sum(cart.goods.values_list(F('cart__amount'), flat=True))

    def get_total_sum(self, cart):
        price_amount = cart.goods.values_list('price', F('cart__amount'))
        return sum(price * amount for price, amount in price_amount)
