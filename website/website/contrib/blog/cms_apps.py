from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .cms_appconfig import BlogAppConfig
from .urls import urlpatterns


@apphook_pool.register
class BlogApphook(CMSConfigApp):
    name = _('Blog')
    app_name = 'blog'
    app_config = BlogAppConfig

    def get_urls(self, page=None, language=None, **kwargs):
        return urlpatterns
