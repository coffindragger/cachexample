from django.conf.urls.defaults import patterns, include, url
from cachexample.views import *

urlpatterns = patterns('',

    url(r'^genre/(?P<category_slug>[^/]+)/$', BookListingView.as_view(), name='category_listing'),

    url(r'^(?P<slug>[^/]+)/$', BookDetailView.as_view(), name='book_detail'),
)
