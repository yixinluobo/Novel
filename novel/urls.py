from django.conf.urls import url

from novel import views

urlpatterns = [
    url(r'^novels/$', views.NovelListAPI.as_view()),
    url(r'^brand/novels/$', views.BrandListAPI.as_view()),
    url(r'^novel/(?P<pk>.*)$', views.NovelAPIView.as_view()),
    url(r'^chapter/(?P<pk>.*)$', views.ChapterListAPIView.as_view()),

]
