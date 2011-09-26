from cachexample.models import Book

def popular_books(request):
    return {
        'POPULAR_BOOKS': Book.objects.popular(),
    }
