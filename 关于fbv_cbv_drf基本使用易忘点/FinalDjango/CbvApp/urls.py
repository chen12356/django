from django.conf.urls import url

from CbvApp import views

urlpatterns=[
    # view
    url(r'^animal2/',views.AnimalView.as_view()),
    # templateview
    url(r'^animal3/',views.AnimalTemplateView.as_view(template_name='animal3.html')),
    #listView
    url(r'^animal4/',views.AnimalListView.as_view()),
    # DetailView
    url(r'^animal5/(?P<pk>\d+)/',views.AnimalDetailView.as_view()),
]