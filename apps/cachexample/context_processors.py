from cachexample.models import *

def categories(request):
    return {
        'CATEGORIES': Category.objects.all(),
    }

def popular_books(request):
    return {
        'POPULAR_BOOKS': Book.objects.popular(),
    }
