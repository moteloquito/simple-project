from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import AccountForm, BookForm
from .models import Account, Book


class AccountListView(ListView):
    model = Account


class AccountDetailView(DetailView):
    model = Account


class AccountCreateView(CreateView):
    model = Account
    fields = ['account_type', 'parent', 'description']
    form_class = AccountForm

    def get_success_url(self):
        return reverse_lazy('account_detail', args=[self.object.pk])


class AccountUpdateView(UpdateView):
    model = Account
    fields = ['account_type', 'parent', 'description']

    def get_success_url(self):
        return reverse_lazy('account_detail', args=[self.object.pk])


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = ['description', 'valid_from', 'valid_to']
    form_class = BookForm

    def get_success_url(self):
        return reverse_lazy('book_detail', args=[self.object.pk])


class BookUpdateView(UpdateView):
    model = Book
    fields = ['description', 'valid_from', 'valid_to']
    form_class = BookForm

    def get_success_url(self):
        return reverse_lazy('book_detail', args=[self.object.pk])
