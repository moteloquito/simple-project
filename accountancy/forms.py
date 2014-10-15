from django.forms import DateField, ModelForm, ValidationError
from django.forms.widgets import DateInput

from .models import Account, Book


class CustomDateInput(DateInput):
    input_type = 'date'


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['account_type', 'parent', 'description']
        exclude = ['root']

    def clean(self):
        cleaned_data = super(AccountForm, self).clean()
        account_type = cleaned_data.get('account_type')
        parent = cleaned_data.get('parent')

        if account_type:
            if account_type == 'ROOT':
                if parent:
                    raise ValidationError('El tipo raiz no permite padre',
                                          code='error1')
            else:
                if not parent:
                    raise ValidationError('Debe indicar una cuenta padre',
                                          code='error2')


class BookForm(ModelForm):
    valid_from = DateField(widget=CustomDateInput())
    valid_to = DateField(widget=CustomDateInput())

    class Meta:
        model = Book
        fields = ['description', 'valid_from', 'valid_to']

    def save(self, commit=True, *args, **kwargs):
        instance = super(BookForm, self).save(commit=False, *args, **kwargs)
        if not hasattr(instance, 'root'):
            root = Account(account_type='ROOT', description='Root account')
            root.save()
            instance.root = root
        if commit:
            instance.save()
        return instance
        
        
    
