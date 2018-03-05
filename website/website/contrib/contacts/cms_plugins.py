from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


@plugin_pool.register_plugin
class ContactContainerPluginPublisher(CMSPluginBase):
    model = models.ContactContainerPluginModel
    module = _('Contacts')
    name = _('Contact Container')
    render_template = 'contacts/contact_container.html'
    allow_children = True
    child_classes = ('ContactPluginPublisher',)


@plugin_pool.register_plugin
class ContactPluginPublisher(CMSPluginBase):
    model = models.ContactPluginModel
    module = _('Contacts')
    name = _('Contact')
    render_template = 'contacts/contact.html'
    require_parent = True
    parent_classes = ('ContactContainerPluginPublisher',)
