from django.conf.urls import url, include

urlpatterns = [
    url(r'^blog/', include('website.contrib.blog.urls', namespace='blog')),
]
