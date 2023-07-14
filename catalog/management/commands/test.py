# myapp/management/commands/fill.py
from django.core.management import BaseCommand
from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # pk_1 = Category.objects.get(pk=1)
        # pk_2 = Category.objects.get(pk=2)
        # pk_3 = Category.objects.get(pk=3)
        Product.objects.all().delete()
        product_list = [
            {'name': 'Смартфон', 'description': 'Asus', 'category': 'телефоны', 'purchase_price': '15000'},
            {'name': 'Планшет', 'description': 'apple', 'category': 'планшеты', 'purchase_price': '690000'},
            {'name': 'Ноутбук', 'description': 'Asus', 'category': 'ноутбуки', 'purchase_price': '70000'}
        ]
        product_create = []
        for product_item in product_list:
            product_create.append(Product(**product_item))
        Product.objects.bulk_create(product_create)
