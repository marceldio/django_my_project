from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        print(f'You have new message from {name}({tel}): {message}')
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        message = request.POST.get('message')
        print(f'You have new message from {name}({tel}): {message}')
    return render(request, 'main/contact.html')


def card(request):
    return render(request, 'main/card.html')
