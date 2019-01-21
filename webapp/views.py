""" view of webapp """
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.conf import settings
from webapp.forms import SignUpForm, KycForm
from webapp.token import account_activation_token
from main.models import UserDetails, Kyc
from webapp.decorators import user_is_valid
from webapp.py_solc.ERC20 import IcoToken
from webapp.py_solc.crowd_sale import CrowdSale
from webapp.py_solc.buyToken import BuyTokens

token = IcoToken()
crowdsale = CrowdSale()
buyToken = BuyTokens()
# Create your views here.

class HomePageView(TemplateView):
    """ home page view """
    template_name = 'home.html'


class SignUpView(View):
    """ Registration View """

    def get(self, request):
        """ Get Method for Registration """
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        """ POST Method for Registration """
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile = UserDetails()
            profile.user = user
            profile.mobile_number = form.cleaned_data["mobile_number"]
            profile.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
        else:
            return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    """ Account account_activation_email sent """
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    """ Activate the user Account """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')


def send_verfication_code(otp, username, request):
    """ send Verification code """
    subject = 'Thank you for registering to our site'
    message = 'This is youe one time password for login' + str(otp)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [username]
    send_mail(subject, message, email_from, recipient_list)


class OTPVerificationView(View):
    """ Otp Verification View """
    @method_decorator(user_is_valid)
    def dispatch(self, *args, **kwargs):
        return super(OTPVerificationView, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'otp_verify.html')

    def post(self, request):
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        user_detail = UserDetails.objects.get(user_id=user_id)
        sms_verify_token = request.POST.get('sms_verify_token')
        if user_detail.sms_verify_token == sms_verify_token:
            try:
                kyc, created = Kyc.objects.get_or_create(user_id=user_id)
                if kyc.is_approved is True:
                    login(request, user, backend='main.backend.EmailBacked')
                    return redirect('dashboard')
                else:
                    login(request, user, backend='main.backend.EmailBacked')
                    return redirect('kyc_form')
            except ObjectDoesNotExist:
                return redirect('kyc_form')
        else:
            return redirect('otp_verify_token')


class LoginPageView(View):
    """ Login View """

    def get(self, request):
        """ Get Method for Login """
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        otp = get_random_string(6, allowed_chars='0123456789')
        up = get_object_or_404(UserDetails, user=user)
        up.sms_verify_token = otp
        up.save()
        if user:
            send_verfication_code(otp, username, request)
            request.session['user_id'] = user.id
            return redirect('otp_verify_token')
        else:
            return HttpResponse("Invalid login details supplied.")


class KycView(LoginRequiredMixin, View):
    """ kyc """

    def get(self, request):
        form = KycForm()
        return render(request, 'kyc_form.html', {'form': form})

    def post(self, request):
        form = KycForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.session.get('user_id')
            kyc, created = Kyc.objects.get_or_create(user_id=user_id)
            kyc.id_proof = form.cleaned_data["id_proof"]
            kyc.address_proof = form.cleaned_data["address_proof"]
            kyc.save()
            return HttpResponse("Submitted")


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        ts = token.token_instance.totalSupply()
        convert_str = str(ts)
        convert_str.split()
        token_supply = convert_str[0:9]

        return render(request, 'dashboard.html', {
            'token': token.token_instance,
            'crowdsale': crowdsale.crowdsale_instance,
            'crowdsale_address':crowdsale.crowdsale_contract_address,
            'token_supply':token_supply
        })


class LogoutView(LoginRequiredMixin, RedirectView):
    """ Logout """
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AboutPageView(TemplateView):
    """ About Us """
    template_name = 'about.html'
