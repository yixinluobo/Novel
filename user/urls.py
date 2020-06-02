from django.conf.urls import url

from user import views

urlpatterns = [
    url(r"^register/$", views.RegisterAPIView.as_view()),
    url(r"^login/$", views.LoginAPIView.as_view()),
]