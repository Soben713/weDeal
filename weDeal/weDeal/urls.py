"""weDeal URL Configuration

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
from django.conf.urls import url, static
from django.contrib import admin

from mainapp import views
from weDeal import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name="home"),
    url(r'^add-deal/', views.add_deal, name="add-deal"),
    url(r'^auth/', views.authentication_view, name="auth"),
    url(r'^deals/', views.deals_view, name="deals"),
    url(r'^deal/(?P<pk>[-\w]+)/', views.DealView.as_view(), name="deal"),
    url(r'^logout/', views.logout_view, name='logout'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
