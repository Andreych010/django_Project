from django.urls import path
from catalog.views import home, contacts, products
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path("contacts/", contacts, name="contacts"),
    path("products/", products, name="products")
    # path("contacts/", contacts, name="contacts")

]

# from django.urls import path
#
# from catalog.apps import CatalogConfig
# from catalog.views import contacts, home, products, product_card
#
# app_name = CatalogConfig.name
#
# urlpatterns = [
#     path('contacts/', contacts, name='contacts'),
#     path('', home, name='home'),
#     path('products/', products, name='products'),
#     path('product_card/<pk>/', product_card, name='product_card'),
# ]