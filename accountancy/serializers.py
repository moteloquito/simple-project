from django.forms import widgets

from rest_framework import serializers

from accountancy.models import Account, ACCOUNT_TYPE_CHOICES


class AccountSerializer(serializers.ModelSerializer):

    class Meta():
        model = Account
        fields = ('id', 'description', 'account_type', 'parent')
