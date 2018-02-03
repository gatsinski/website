from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from djangocms_text_ckeditor.fields import HTMLField
from parler.models import TranslatableModel, TranslatedFields

from .managers import PostManager


class Post(TranslatableModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=_('Author'))
    created_at = models.DateTimeField(_('Created at'),
                                      auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'),
                                      auto_now=True)
    is_published = models.BooleanField(_('Published'),
                                       default=False)

    translations = TranslatedFields(
        title=models.CharField(_('Title'), max_length=254),
        slug=models.SlugField(_('Slug')),
        excerpt=models.CharField(_('Excerpt'), max_length=2000, blank=True),
        content=HTMLField(_('Content'))
    )

    objects = PostManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.created_at.year,
            'month': '%02d' % self.created_at.month,
            'day': '%02d' % self.created_at.day,
        }
        return reverse('blog:post_detail', kwargs=kwargs)
