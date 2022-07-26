"""currency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from converter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin panel url
    path('admin/', admin.site.urls),

    #list of all currencies
    path('', views.show_list, name="list"),

    #user-authantication
    path( 'api-auth/' , include( 'rest_framework.urls' )),
    path( 'login/' , include( 'dj_rest_auth.urls' ), name="signin"),
    path( 'registration/' , include( 'dj_rest_auth.registration.urls' ), name="signup"),

    # historical exchange rates page
    path('historical/', views.show_historical, name="historical"),

    # live rates page
    path('live/', views.show_live, name="live"),

    #converting currencies
    path('index/', views.index, name="index"),

    # path( '<int:pk>/' , DetailTodo . as_view()),
]