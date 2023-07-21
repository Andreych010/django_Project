from django.shortcuts import render
import os
# from lib2to3.fixes.fix_input import context
from catalog.models import Product, Category


# from config import settings

def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категории'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вам поступило новое сообщение: "{message}"\nname: {name}, phone: ({phone})')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)

# def contacts(request):
#     context = {'title': 'Контакты'}
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get("message")
#         print(f'You have new message from {name}({phone}): {message}')
#
#     return render(request, 'catalog/contacts.html', context)
#
#
# def home(request):
#
#     return render(request, 'catalog/home.html')
# #
#
# def products_3(request):
#     context = {
#         'object_list': Product.objects.all()[:3],
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/products.html', context)
#
#
def products(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Товары'
    }
    return render(request, 'catalog/products.html', context)

#
#
# def product_card(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object': product_item,
#     # context = {
#     #     'object_list': Product.objects.all(),
#         'title': 'Карточка товара'
#     }
#     return render(request, 'catalog/product_card.html', context)
#
#
# def index(request):
#     path = settings.MEDIA_ROOT
#     img_list = os.listdir(path + '/products')
#     context = {'images': img_list}
#     return render(request, "catalog/products.html", context)
