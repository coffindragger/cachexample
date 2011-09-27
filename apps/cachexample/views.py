from cachexample.models import Book
from cachemodel.views.generic import CachedDetailView
from django.views.generic import ListView

from cachexample.models import *

class BookDetailView(CachedDetailView):
    context_object_name = "book"
    model = Book
    template_name = 'book/detail.html'


class BookListingView(ListView):
    model = Book
    template_name = 'book/listing.html'
    def get_context_data(self, **kwargs):
        category = self.kwargs.get('category_slug', None)
        if category is not None:
            category = Category.objects.get_cached(slug=category)
        page = 1
        return {
            'object_list': Book.objects.listings_cached(category=category, page=page),
        }
        pass
