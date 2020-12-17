from django.conf.urls import url

from FbvApp import views

urlpatterns=[
    url(r'^findAnimal/',views.findAnimal),
    url(r'^findAnimal1/',views.findAnimal1),
]