from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вам поступило новое сообщение: "{message}"\nname: {name}, phone: ({phone})')
    return render(request, 'catalog/contacts.html')

