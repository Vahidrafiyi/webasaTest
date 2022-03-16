from django.urls import path
from django.conf.urls import include,url
from .views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile',ProfileView,basename='profile')

urlpatterns=[
    url('',include(router.urls)),
    path('otp/',OTPView.as_view(),name="otp_view"),
    path('otp/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('profilee/<int:pk>/',ProfileApi.as_view()),
    path('profile_edit/<int:pk>/',ProfileEditApi.as_view()),
]
