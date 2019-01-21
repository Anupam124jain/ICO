""" urls of webapp """
from django.urls import path, re_path
from webapp import views
from .views import (
    HomePageView,
    AboutPageView,
    LoginPageView,
    LogoutView,
    KycView,
    SignUpView,
    OTPVerificationView,
    Dashboard,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('otp_verify_token/', OTPVerificationView.as_view(),
         name='otp_verify_token'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('kyc_form/', KycView.as_view(), name='kyc_form'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    re_path(r'^account_activation_sent/$', views.account_activation_sent,
            name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
]
