from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from .constants import CONTACT_ICON_CHOICES, FACEBOOK


class ContactContainerPluginModel(CMSPlugin):
    pass

    class Meta:
        verbose_name = _('Contact Container')
        verbose_name_plural = _('Contact Containers')


class ContactPluginModel(CMSPlugin):
    icon = models.CharField(_('Icon'),
                            max_length=254,
                            default=FACEBOOK,
                            choices=CONTACT_ICON_CHOICES)
    text = models.CharField(_('Text'),
                            max_length=254)
    link = models.CharField(_('Link'),
                            max_length=254)


    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.text
