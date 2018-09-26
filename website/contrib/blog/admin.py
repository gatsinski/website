from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from aldryn_apphooks_config.admin import BaseAppHookConfig
from parler.admin import TranslatableAdmin
from django_object_actions import DjangoObjectActions

from .models import Post
from .forms import PostAdminForm
from .cms_appconfig import BlogAppConfig


@admin.register(Post)
class PostAdmin(DjangoObjectActions, TranslatableAdmin):
    form = PostAdminForm
    list_filter = ('author',
                   'created_at',
                   'updated_at',
                   'is_published')
    list_display = ('title',
                    'author',
                    'created_at',
                    'updated_at',
                    'is_published')
    list_per_page = 15
    search_fields = ('title', 'author', 'slug')
    actions = ['publish']
    change_actions = ('publish', 'unpublish')

    def get_prepopulated_fields(self, request, obj=None):
        # Can't use `prepopulated_fields` because it of the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'slug': ('title',)
        }

    def publish(self, request, obj):
        obj.is_published = True
        obj.save()
    publish.short_description = _('Publish')

    def unpublish(self, request, obj):
        obj.is_published = False
        obj.save()
    publish.short_description = _('Unpublish')

    def get_change_actions(self, request, object_id, form_url):
        actions = super(PostAdmin, self).get_change_actions(request,
                                                            object_id,
                                                            form_url)
        actions = list(actions)
        if not request.user.is_superuser:
            return []

        obj = self.model.objects.get(pk=object_id)
        if obj.is_published:
            actions.remove('publish')
        else:
            actions.remove('unpublish')
        return actions


@admin.register(BlogAppConfig)
class BlogAppConfigAdmin(BaseAppHookConfig, admin.ModelAdmin):
    pass
