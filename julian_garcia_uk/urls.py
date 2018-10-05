"""julian_garcia_uk URL Configuration

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
from django.urls import path, include
from about.views import index
from about import urls as urls_about
from experience import urls as urls_experience
from portfolio import urls as urls_portfolio
from attending import urls as urls_attending
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', include(urls_about)),
    path('experience/', include(urls_experience)),
    path('portfolio', include(urls_portfolio)),
    path('attending', include(urls_attending)),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
