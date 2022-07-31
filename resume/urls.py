from xml.etree.ElementInclude import include
from django.urls import path

from . import views

urlpatterns = [
    # pages
    path('', views.index, name='index'),
    path('signin', views.signin_page, name='signin_page'),
    path('signup', views.signup_page, name='signup_page'),
    path('error', views.error_page, name='error_page'),

    # API's
    path('login', views.login_user, name='login_user'),
    path('register', views.register_user, name='register_user'),
]

authorised_urls = [
    path('print-resume/', views.print_pdf_resume, name='print_pdf_resume'),
    path('view-resume/', views.view_pdf_resume, name='view_pdf_resume'),
]

urlpatterns.extend(authorised_urls)