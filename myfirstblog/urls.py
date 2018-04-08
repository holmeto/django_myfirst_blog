"""myfirstblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^category/$', views.category_html, name='category_html'),
    #url(r'^tag/$', views.Tag_html, name='Tag_html'),
    url(r'^blog/$', views.get_all_blogs, name='get_all_blogs'),
    url(r'^comment/$', views.Comment_html, name='Comment_html'),
    url(r'^detail/(\d+)/$',views.blog_get_detail,name='blog_get_detail'),
    url(r'^comment/(\d+)/$',views.comment_get_detail,name='comment_get_detail'),
    url(r'^write/$',views.write_blog,name='write_blog'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^allblogs/$', views.present_all_blogs, name='present_all_blogs'),
]
