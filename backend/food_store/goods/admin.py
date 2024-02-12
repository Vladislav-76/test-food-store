from django.contrib import admin
from django.contrib.auth.models import Group

from goods.models import Category, Subcategory, UnitOfGoogs

admin.site.register((Category, Subcategory, UnitOfGoogs))
admin.site.unregister(Group)
