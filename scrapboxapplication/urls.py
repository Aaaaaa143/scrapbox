"""
URL configuration for scrapboxapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from scrapbox import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scrapbox/register/',views.SignUpView.as_view(),name="signup"),
    path('scrapbox/signin/',views.SignInView.as_view(),name="signin"),
    path('scrapbox/index/',views.IndexView.as_view(),name="index"),
    path('scrapbox/profile/update/<int:pk>/',views.UserProfileView.as_view(),name="profile"),
    path('scrapbox/profile/<int:pk>/',views.ProfileDetailView.as_view(),name="profile_detail"),
    path('scrapbox/<int:pk>/',views.ScrapDetailView.as_view(),name="scrap-detail"),
    path('scrapbox/delete/<int:pk>/',views.ScrapDeleteView.as_view()),
    path('scrapbox/update/<int:pk>/',views.ScrapUpdateView.as_view(),name="update"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
