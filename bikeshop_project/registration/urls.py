from django.conf.urls import url

from .views import MemberFormView, MemberSearchView, MemberSignIn, Members
urlpatterns = [
    url(r'^new/$', MemberFormView.as_view(), name='member_new'),
    url(r'^search/(?P<query>[\w@\.\+]+)/$', MemberSearchView.as_view(), name='member_search'),
    url(r'^edit/(?P<member_id>[0-9]+)/$', MemberFormView.as_view(), name='member_edit'),
    url(r'^signin/$', MemberSignIn.as_view(), name='member_signin'),
    url(r'^$', Members.as_view(), name='members'),
]