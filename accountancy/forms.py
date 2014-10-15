from django.forms import ModelForm, ValidationError

from .models import Account


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['account_type', 'parent', 'description']

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
