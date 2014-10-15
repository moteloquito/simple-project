from django.conf.urls import patterns, include, url

from .views import AccountListView, AccountDetailView, AccountCreateView, AccountUpdateView


urlpatterns = patterns(
    'accountancy.views',

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
)
