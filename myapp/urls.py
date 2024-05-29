from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.index, name='index.info'),
    path('course/<int:course_id>', views.course_info, name='course_info'),
    path('contact', views.contact, name='contact.info'),
]






