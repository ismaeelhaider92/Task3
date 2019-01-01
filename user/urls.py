from django.urls import path
from user import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    # path("/home", views.home, name=""),
    path("user/home/", views.home, name="home"),
    path(r"user/signup", views.sign_up, name="sign_up"),
    url(r'user/login/$', auth_views.LoginView.as_view(template_name="signin.html"), name='login'),
    url(r'logout/$', auth_views.LoginView.as_view(template_name='signin.html'), name='logout'),
]