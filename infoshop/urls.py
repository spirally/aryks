from django.conf.urls import url
from . import views

app_name = 'infoshop'

urlpatterns = [
    url(r'^$', views.ProductList, name='ProductList'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.ProductList, name='ProductListByCategory'),
    url(r'^(?P<id>\d+)/(?P<alias>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
]
