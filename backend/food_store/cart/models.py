from django.contrib.auth import get_user_model
from django.db import models

from goods.models import UnitOfGoogs


User = get_user_model()


class Cart(models.Model):
    """Модель корзины."""

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
    )
    goods = models.ManyToManyField(
        UnitOfGoogs,
        related_name='carts',
        through='CartGoods',
    )

    def __str__(self):
        return f'Cart of {self.owner.get_username()}'


class CartGoods(models.Model):
    """Модель связи корзина - продукты."""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    unit_of_goods = models.ForeignKey(
        UnitOfGoogs,
        related_name='cart',
        on_delete=models.CASCADE,
    )
    amount = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.cart} - {self.unit_of_goods}'
