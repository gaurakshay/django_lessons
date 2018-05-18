from django.conf.urls import url

from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    url(r'^post/$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post_new'),
    url(r'^post/edit/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='post_edit'),
]
