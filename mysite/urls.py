"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
from django.urls import include
from rest_framework_swagger.views import  get_swagger_view

from blog.views import blog_page, blog_api


schema_view = get_swagger_view(title='rest API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^movies/', include('movies.urls')),
    url(r'^score/', include('score.urls')),
    url(r'^rest-api/', include('rest_framework.urls')),
    url(r'^rest-swagger/', schema_view),

    url(r'^blog/', blog_page),
    url(r'api/blog/', blog_api.as_view()),
    url(r'user/', include('user_manager.urls')),
    url(r'board/', include('post_service.urls'))
]
