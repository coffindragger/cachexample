from cachexample.models import Book
from cachemodel.views.generic import CachedDetailView

class BookDetailView(CachedDetailView):
    context_object_name = "book"
    model = Book
    template_name = 'book/detail.html'
