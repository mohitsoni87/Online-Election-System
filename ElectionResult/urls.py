from django.conf.urls import url
from .views import electionResult
app_name = 'ElectionResult'
urlpatterns = [
    url(r'^(?P<PinCode>[0-9]{6})/$', electionResult, name='ElectionResult'),

   # url(r'^(?P<username>[A-Za-z0-9_.-]+)/add/$', cart, name = 'add_to_cart'),
   # url(r'^(?P<username>[A-Za-z0-9_.-]+)/(?P<pk>[0-9]+)/delete/$', Cart_delete, name = 'Cart_delete'),
]