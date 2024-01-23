from django.urls import include, path
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)
from core.views import (
    ForgotPasswordView,
    IntroViewSet,
    LogoutView,
    PasswordResetView,
    ReferenceViewSet,
    RegisterView,
    UserLoginView,
    UserViewSet,
)

from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from sales.views import AwardViewSet, LeaderboardViewSet, StatViewSet


router = DefaultRouter()

admin.site.site_header = "Klosers Admin"
admin.site.site_title = "Klosers Admin Panel"
admin.site.index_title = "Welcome to Klosers Admin Panel"

router.register(r"users", UserViewSet, basename="users")
router.register(r"awards", AwardViewSet)
router.register(r"references", ReferenceViewSet)
router.register(r"stats", StatViewSet)
router.register(r"leaderboard", LeaderboardViewSet)
router.register(r"intros", IntroViewSet)
urlpatterns = [
    # auth
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/login/", UserLoginView.as_view(), name="login"),
    path("api/register/", RegisterView.as_view(), name="sign_up"),
    path(
        "api/forgot-password/",
        ForgotPasswordView.as_view(),
        name="forgot_password",
    ),
    path("api/password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    # below adds api/ prefix to all routes in router
    # router.register
    path("api/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
