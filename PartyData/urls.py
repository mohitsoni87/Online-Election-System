from django.conf.urls import url
from .views import detailView
app_name = 'PartyData'
urlpatterns = [
    url(r'^(?P<UniqueKey>[a-zA-Z0-9_.-]+)/$', detailView, name='PartyData'),
   # url(r'^(?P<username>[A-Za-z0-9_.-]+)/add/$', cart, name = 'add_to_cart'),
   # url(r'^(?P<username>[A-Za-z0-9_.-]+)/(?P<pk>[0-9]+)/delete/$', Cart_delete, name = 'Cart_delete'),
]