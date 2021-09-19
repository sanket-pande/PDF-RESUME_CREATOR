from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('print-resume/', views.print_pdf_resume, name='print_pdf_resume'),
]