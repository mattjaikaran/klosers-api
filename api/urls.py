"""
URL configuration for api project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static

from django.views.generic import TemplateView
from core.views import UserViewSet
from sales.views import AwardRecognitionViewSet, CareerStatViewSet, YTDStatViewSet
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from core.views import GoogleLoginView
from dj_rest_auth.jwt_auth import get_refresh_view
from rest_framework_simplejwt.views import TokenVerifyView

router = routers.SimpleRouter()
admin.site.site_header = "Kloser Admin"
admin.site.site_title = "Kloser Admin Panel"
admin.site.index_title = "Welcome to Klosers Admin Panel"

router.register(r"users", UserViewSet)
router.register(r"ytd-stats", YTDStatViewSet)
router.register(r"career-stats", CareerStatViewSet)
router.register(r"awards-recognition-stats", AwardRecognitionViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path("api/accounts/", include("allauth.urls")),  # For allauth URLs
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/google/", GoogleLoginView.as_view(), name="google_login"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", get_refresh_view().as_view(), name="token_refresh"),
    path("api/register/", RegisterView.as_view(), name="rest_register"),
    path("api/login/", LoginView.as_view(), name="rest_login"),
    path("api/logout/", LogoutView.as_view(), name="rest_logout"),
    path("api/user/", UserDetailsView.as_view(), name="rest_user_details"),
]

urlpatterns += (path("api/", include(router.urls)),)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
