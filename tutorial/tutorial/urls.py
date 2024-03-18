"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin   # imports the admin module from Django's contrib package, which provides functionality for the Django admin interface.
from django.urls import path,include  #imports the path function and the include function from Django's urls module. The path function is used for defining URL patterns, and the include function is used for including other URL patterns from different modules

urlpatterns = [
    path('admin/', admin.site.urls), # defines a URL pattern using the path function. It specifies that requests to the /admin/ endpoint should be handled by the Django admin interface. The admin.site.urls value is provided as the view for the URL pattern, which includes the URLs configured for the Django admin interface.

    path('api/', include ('tasks.urls')),  #defines a URL pattern using the path function. It specifies that requests to the /api/ endpoint should be included from the tasks.urls module. The include function is used to include URL patterns from another module (tasks.urls), which is typically used for including URLs related to API endpoints.
]
