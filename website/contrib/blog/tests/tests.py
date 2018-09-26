from django.test.utils import override_settings
from django.utils.text import slugify
from django.contrib.auth.models import User

from cms.test_utils.testcases import CMSTestCase

from ..models import Post


class BlogTestCase(CMSTestCase):

    def setUp(self):
        self.user = User.objects.create(username='john_doe')
        title = 'Lorem ipsum dolor sit amet'
        self.post = Post.objects.create(
            title=title,
            slug=slugify(title),
            author=self.user,
            content=(
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                'Curabitur ac ipsum ut mauris viverra placerat. Etiam com '
                'odo justo vitae leo fermentum, ac tempor lectus elentum. '
                'Integer vitae lacus et ante aliquet fringilla. Suspendis '
                'se id ipsum malesuada, porta dui vitae, feugiat dui quis.'
            ),
            is_published=True
        )

    @override_settings(ROOT_URLCONF='website.contrib.blog.tests.urls')
    def test_post_url_reverse(self):
        kwargs = {
            'slug': self.post.slug,
            'year': '%04d' % self.post.created_at.year,
            'month': '%02d' % self.post.created_at.month,
            'day': '%02d' % self.post.created_at.day,
        }
        url = self.post.get_absolute_url()
        self.assertEqual(url, '/blog/{}/{}/{}/{}/'.format(kwargs['year'],
                                                          kwargs['month'],
                                                          kwargs['day'],
                                                          kwargs['slug']))
