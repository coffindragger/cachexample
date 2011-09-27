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
        try:
            page = int(self.request.GET.get('page','1'))
        except ValueError:
            page = 1

        limit = 10

        num_objects = Book.objects.listings_count(category=category)
        object_list = Book.objects.listings_cached(category=category, page=page, limit=limit)

        return {
            'object_list': object_list,
            'paginator': {
                'count': num_objects,
                'num_pages': num_objects / 10,
            },
            'page_obj': {
                'object_list': object_list,
                'number': page,
                'has_next': page < (num_objects / 10),
                'has_previous': page > 1,
                'next_page_number': page+1,
                'previous_page_number': page-1,
            }
        }
        pass
