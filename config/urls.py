"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="main"),
    path("generic/", TemplateView.as_view(template_name="generic.html"), name="generic"),
    path("elements/", TemplateView.as_view(template_name="elements.html"),
         name="elements"),
    path("todo_list/", include('todo_list.urls')),
    path("board/", include('board.urls')),
    path("find/", include('find.urls')),
    # path("chat/", include('chat.urls') ),
    path("community/", include('community.urls')),
    path("maps/", include('map.urls')),
    # path("ranking/", include('ranking.urls') ),
    path("todo_list/", include('todo_list.urls')),
    path("users/", include('user.urls')),
    #path("volunteer/", include('volunteer.urls')),

    # google login
    path("accounts/", include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
