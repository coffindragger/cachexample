from django.conf.urls.defaults import patterns, include, url
from cachexample.views import BookDetailView

urlpatterns = patterns('',

    url(r'^(?P<slug>[^/]+)/$', BookDetailView.as_view(), name='book_detail'),
)
