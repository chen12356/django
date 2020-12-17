from django.conf.urls import url

from FbvDrfApp import views

urlpatterns = [
    url(r'^findBathCenter/',views.findBathCenter),
]