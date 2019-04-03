from django.conf.urls import url
from .views import profile
app_name = 'Candidate'
urlpatterns = [
    url(r'^(?P<PinCode>[0-9]{6})/(?P<UniqueKey>[a-zA-Z0-9_.-]+)/$', profile, name='profile'),
]