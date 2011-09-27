from django.db import models
from cachemodel import models as cachemodels

from cachexample.managers import *


class Category(cachemodels.CachedTable):
#class Category(models.Model):
    name = models.CharField(max_length=1024)
    slug = models.SlugField()
    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('category_listing', [], {'category_slug': self.slug})


class Author(cachemodels.CacheModel):
#class Author(models.Model):
    name = models.CharField(max_length=1024)
    bio = models.TextField()
    objects = AuthorManager()

    def __unicode__(self):
        return self.name


class Book(cachemodels.CacheModel):
#class Book(models.Model):
    is_active = models.BooleanField()
    slug = models.SlugField()
    name = models.CharField(max_length=1024)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    popularity = models.IntegerField(default=0, editable=False)
    objects = BookManager()

    def __unicode__(self):
        return self.name

    def warm_cache(self):
        super(Book, self).warm_cache()
        self.author_cached
        self.related_books() # make sure related books query is warmed

    @models.permalink
    def get_absolute_url(self):
        return ('book_detail', [], {'slug': self.slug})

    @cachemodels.cached_method
    def related_books(self, how_many=5):
        return Book.objects.filter(models.Q(category=self.category_cached) | models.Q(author=self.author_cached)).exclude(pk=self.pk)[:how_many]

    @cachemodels.denormalized_field('popularity')
    def calc_popularity(self):
        return Comment.objects.filter(book=self).count()





class Comment(cachemodels.CacheModel):
#class Comment(models.Model):
    book = models.ForeignKey(Book)
    body = models.TextField()



#class Homepage(cachemodels.CacheModel):
#    is_active = models.BooleanField()
#    name = models.CharField()
#
#    @cachemodels.cached_method
#    def featured_books(self):
#        return self.homepagebook_set.all()
#
#
#class HomepageBook(cachemodels.CacheModel):
#    homepage = models.ForeignKey(Homepage)
#    book = models.ForeignKey(Book)
#
#
