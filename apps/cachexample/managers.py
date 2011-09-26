from django.db import models
from cachemodel import models as cachemodels


class BookManager(cachemodels.CacheModelManager):
    @cachemodels.cached_method()
    def listings_cached(self, category=None, page=1, limit=10):
        qs = self.all()
        if category:
            qs.filter(category=category)
        offset = (page-1)*limit
        return qs[offset:offset+limit]

    @cachemodels.cached_method('popular-books-for-homepage')
    def popular(self, limit=5):
        return self.filter(is_active=True).order_by('-popularity')[:limit]

    def warm_cache(self):
        super(BookManager, self).warm_cache()

        # make sure popular books are available for context processor
        self.popular()

        # 'foobar' is a popular book, always cache it
        foobar = self.get_cached(slug='foobar')
        foobar.warm_cache()

        # warm the first 3 pages of listings for each category
        from cachexample.models import Category
        for category in Category.objects.all():
            for i in range(1,3):
                self.listings_cached(category=category, page=i)


