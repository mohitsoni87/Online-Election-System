from django.conf.urls import url
from .views import ConductElection
app_name = 'Election'
urlpatterns = [
    url(r'^(?P<PinCode>[0-9]{6})/$', ConductElection, name='ConductElection'),

   # url(r'^(?P<username>[A-Za-z0-9_.-]+)/add/$', cart, name = 'add_to_cart'),
   # url(r'^(?P<username>[A-Za-z0-9_.-]+)/(?P<pk>[0-9]+)/delete/$', Cart_delete, name = 'Cart_delete'),
]