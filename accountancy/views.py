from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Account


class AccountListView(ListView):
    model = Account


class AccountDetailView(DetailView):
    model = Account


class AccountCreateView(CreateView):
    model = Account
    fields = ['account_type', 'parent', 'description']
    def get_success_url(self):
        return reverse_lazy('account_detail', args=[self.object.pk])


class AccountUpdateView(UpdateView):
    model = Account
    fields = ['account_type', 'parent', 'description']
    def get_success_url(self):
        return reverse_lazy('account_detail', args=[self.object.pk])
