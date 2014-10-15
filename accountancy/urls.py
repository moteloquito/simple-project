from django.conf.urls import patterns, include, url

from .views import AccountListView, AccountDetailView, AccountCreateView, AccountUpdateView, BookListView, BookDetailView, BookCreateView, BookUpdateView


urlpatterns = patterns(
    'accountancy.views',

    # Account
    url(r'^account/$',
        AccountListView.as_view(),
        name='account_list'),

    url(r'^account/view/(?P<pk>[\w-]+)$',
        AccountDetailView.as_view(),
        name='account_detail'),

    url(r'^account/create$',
        AccountCreateView.as_view(),
        name='account_create'),

    url(r'^account/update/(?P<pk>[\w-]+)$',
        AccountUpdateView.as_view(),
        name='account_update'),

    # Book
    url(r'^book/$',
        BookListView.as_view(),
        name='book_list'),

    url(r'^book/view/(?P<pk>[\w-]+)$',
        BookDetailView.as_view(),
        name='book_detail'),

    url(r'^book/create$',
        BookCreateView.as_view(),
        name='book_create'),

    url(r'^book/update/(?P<pk>[\w-]+)$',
        BookUpdateView.as_view(),
        name='book_update'),
)
