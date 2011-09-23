from django.db import models
from cachemodel import models as cachemodels


class BookManager(cachemodels.CacheModelManager):
    @cachemodels.cached_query
    def cached_listings(self, category=None, page=1, limit=10):
        qs = self.all()
        if category:
            qs.filter(category=category)
        offset = (page-1)*limit
        return qs[offset:offset+limit]

    @cachemodels.cached_query
    def popular(self, limit=5):
        return self.filter(is_active=True).order_by('-denorm_popularity')[:limit]
