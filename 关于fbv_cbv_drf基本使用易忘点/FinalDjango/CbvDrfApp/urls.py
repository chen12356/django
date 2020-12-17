from django.conf.urls import url

from CbvDrfApp import views

urlpatterns=[
    url(r'^testWomen/',views.WomenView.as_view())
]