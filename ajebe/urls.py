"""ajebe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.generic import TemplateView

# Admin site config
# admin.site.site_header = "PyShop aJeBe"
admin.site.site_title = "Admin AJeBe"

urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    # apps-api
    re_path('api/(?P<version>(v1|v2))/carriers/', include('carriers.urls')),
    # rest-framework
    path('auth/', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # admin site,
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
]
