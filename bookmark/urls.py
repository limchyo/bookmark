from django.conf.urls import url
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    # 클래스형 뷰는 .as_view()를 붙여주어야 정상 작동이 된다
    url('^$', BookmarkListView.as_view(), name='list'),
    url('^add/$', BookmarkCreateView.as_view(), name='add'),
    url('^detail/(?P<pk>[0-9]+)/$', BookmarkDetailView.as_view(), name='detail'),
    url('^update/(?P<pk>[0-9]+)/$', BookmarkUpdateView.as_view(), name='update'),
    url('^delete/(?P<pk>[0-9]+)/$', BookmarkDeleteView.as_view(), name='delete'),
]
