from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='profileapp-about'),
    path('publications/', views.publications, name='profileapp-publications'),
    path('contact/', views.contact, name='profileapp-contact'),

]