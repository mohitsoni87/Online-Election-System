"""OnlineElectionSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import homepage
from Accounts.views import login_view, logout_view, auth_view, register_view, AccountVerification, ProfileView, RegisterUser
from django.conf import settings
from django.conf.urls.static import static

from SectorParties.views import results
from PartyData.views import detailView
from Election.views import VoteSubmit

app_name = 'OnlineElectionSystem'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='homepage'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^auth/$', auth_view, name='authenticate'),
    url(r'^register/$', register_view, name='register'),
    url(r'^account_verification/(?P<username>[a-zA-Z0-9_.-]+)/(?P<token>[A-Za-z0-9]+)/$', AccountVerification, name ='AccountVerification'),
    url(r'^Profile/$', ProfileView, name='Profile'),
    url(r'^results/$', results, name = 'query_result'),
    url(r'^view_party/', include('PartyData.urls')),
    url(r'^party_results/', include('PartyData.urls')),
    url(r'^OTPVerification/', RegisterUser, name='RegisterUser'),
    url(r'^electionlive/', include('Election.urls')),
    url(r'^submit/(?P<UniqueKey>[a-zA-Z0-9_.-]+)/$', VoteSubmit, name="VoteSubmit"),
    url(r'election_result/', include('ElectionResult.urls')),
    url(r'candidateProfile/', include('Candidate.urls')),
#/(?P<Username>[a-zA-Z0-9_.-]+)/(?P<Token>[A-Za-z0-9]+)/'
]

if settings.DEBUG:              #True if in development mode
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
