from django.shortcuts import render

# Create your views here.

def home(request):
    """Главная страница"""
    context = {
        'title': 'Главная',
        'page_title': 'Добро пожаловать в DJ Project 2'
    }
    return render(request, 'website/home.html', context)

def about(request):
    """Страница о нас"""
    context = {
        'title': 'О нас',
        'page_title': 'О нашей команде'
    }
    return render(request, 'website/about.html', context)

def services(request):
    """Страница услуг"""
    context = {
        'title': 'Услуги',
        'page_title': 'Наши услуги'
    }
    return render(request, 'website/services.html', context)

def contact(request):
    """Страница контактов"""
    context = {
        'title': 'Контакты',
        'page_title': 'Свяжитесь с нами'
    }
    return render(request, 'website/contact.html', context)