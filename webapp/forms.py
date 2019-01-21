""" forms of registration and kyc """
from django import forms
from django.contrib.auth.models import User
from main.models import Kyc


class SignUpForm(forms.ModelForm):
    """ Registration Form """
    use_required_attribute = False
    first_name = forms.CharField(
        max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(
        label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(
        label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    mobile_number = forms.CharField(max_length=15, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'mobile_number',
                  'email', 'password', 'password1')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already exists")
        return email

    def clean_mobile_number(self):
        super(SignUpForm, self).clean()
        mobile_number = self.cleaned_data.get('mobile_number')
        if len(mobile_number) < 9:
            raise forms.ValidationError(
                "not valid")
        return mobile_number

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password1")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class KycForm(forms.ModelForm):
    """ Redirec user to this form if KYC is not done """
    class Meta:
        """ add id and address fields for kyc purpose """
        model = Kyc
        fields = ['id_proof', 'address_proof']
