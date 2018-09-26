
from django.forms import Textarea

from parler.forms import TranslatableModelForm

from .models import Post


class PostAdminForm(TranslatableModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'author',
            'excerpt',
            'content',
            'is_published'
        ]
        widgets = {
            'excerpt': Textarea(),
        }
