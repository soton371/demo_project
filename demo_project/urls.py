"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from home.views import *
from vege.views import *

from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # type: ignore

urlpatterns = [
    path('', home, name='home'),
    path('recipe', recipes),
    path('delete-recipe/<id>', delete_recipe),
    path('update-recipe/<id>', update_recipe),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


# for image view http://127.0.0.1:8000/media/recipe/download.jpeg