from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.listing,name='listing'),
    #url(r'^(?P<categorie_id>[0-9]+)/$',views.detail,name='detail'),
    #'^search/\?query=(?P<query>[A-Z][a-z]+)/$'
    url(r'^search/$',views.search,name='search'),
]