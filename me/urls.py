from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name = 'index'),
    url(r'^post-add/$',views.PostCreate.as_view(),name = 'post_edit'),
    url(r'^post-list/$',views.PostList.as_view(),name = 'post_list'),

    ]
