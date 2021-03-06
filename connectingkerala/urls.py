"""connectingkerala URL Configuration

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
from django.conf.urls import url
from django.conf.urls import include
from .views import LoginView
from members.urls import members_router

urlpatterns = [
    url(r'^admin_login', LoginView.as_view(actions={'post': 'admin_login'}), name='admin_login'),
    url(r'^login', LoginView.as_view(actions={'post': 'login'}), name='login'),
    url(r'^levels', include('levels.urls', namespace='levels')),
    url(r'^groups', include('groups.urls', namespace='groups')),
    # url(r'^members', include(members_router.urls, namespace='members'))
    url(r'^members', include('members.urls', namespace='members')),
    url(r'^config', include('config.urls', namespace='config')),
]
