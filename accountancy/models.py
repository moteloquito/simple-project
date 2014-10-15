from django.db import models
from django.utils.translation import ugettext as _


ROOT = 'ROOT'
ASSETS = 'ASSE'
LIABILITIES = 'LIAB'
OBLIGATIONS = 'OBLI'

ACCOUNT_TYPE_CHOICES = (
    (ROOT, _('account_type_root')),
    (ASSETS, _('account_type_assets')),
    (LIABILITIES, _('account_type_liabilities')),
    (OBLIGATIONS, _('account_type_obligations')),
)


class Account(models.Model):
    description = models.CharField(max_length=128,
                                   verbose_name=_('account_description'))
    account_type = models.CharField(max_length=4,
                                    choices=ACCOUNT_TYPE_CHOICES,
                                    verbose_name=_('account_type'))
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='childs',
                               verbose_name=_('account_parent'))

    class Meta():
        verbose_name = _('account')
        verbose_name_plural = _('account_plural')

    def __str__(self):
        return u'%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description
    

class Book(models.Model):
    description = models.CharField(max_length=128,
                                   verbose_name=_('book_description'))
    valid_from = models.DateField(verbose_name=_('book_valid_from'))
    valid_to = models.DateField(verbose_name=_('book_valid_to'))
    root = models.ForeignKey(Account, null=False, blank=False,
                             verbose_name=_('book_root'))

    class Meta():
        verbose_name = _('book')
        verbose_name_plural = _('book_plural')

    def __str__(self):
        return u'%s' % self.description

    def __unicode__(self):
        return u'%s' % self.description
