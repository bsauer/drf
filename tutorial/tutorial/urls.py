"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.auth.models import User
from wrestling.models import Wrestler, Promotion

from quick.views import UserView
from wrestling.views import WrestlerView
from wrestling.views import PromotionView

from rest_framework.routers import DefaultRouter 
router = DefaultRouter()
router.register('users', UserView) 
#router.register('wrestlers', WrestlerView) 
#router.register('promotions', PromotionView) 

ListCreateMapper = {'get':'retrieve',
                    'post':'create'
}
RetrieveUpdateDestroyMapper = {
                               'get':'retrieve',
                               'patch':'update',
                               'delete':'destroy',
                               'put':'update'
}

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^promotions/$', PromotionView.as_view(ListCreateMapper)),
    url(r'^promotions/(?P<pk>[0-9]+)/$', PromotionView.as_view(RetrieveUpdateDestroyMapper)),
    url(r'^promotions/(?P<pk>[0-9]+)/wrestlers/$', WrestlerView.as_view(ListCreateMapper)),
    url(r'^promotions/(?P<promotion_pk>[0-9]+)//wrestlers/(?P<pk>[0-9]+)$', WrestlerView.as_view(RetrieveUpdateDestroyMapper)),
]
