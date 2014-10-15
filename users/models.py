from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


ADMINISTRATOR = 'ADMIN'
REGULAR = 'REGUL'
SUPERVISOR = 'SUPER'
AUDITOR = 'AUDIT'

USER_TYPE_CHOICES = (
    (ADMINISTRATOR, _('type_Administrator')),
    (REGULAR, _('type_Regular')),
    (SUPERVISOR, _('type_Supervisor')),
    (AUDITOR, _('type_Auditor')),
)


class CustomUser(models.Model):
    user = models.OneToOneField(User)
    user_type = models.CharField(max_length=5,
                                 choices=USER_TYPE_CHOICES,
                                 default=REGULAR,
                                 verbose_name=_('custom_user_user_type'))

    class Meta():
        verbose_name = _('custom_user')
        verbose_name_plural = _('custom_user_plural')

    def __str__(self):
        return "%s %s (%s)" % (self.user.first_name, self.user.last_name, self.user_type)
