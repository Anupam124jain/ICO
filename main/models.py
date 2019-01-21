"""
    Mode of Main Application
"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
# Create your models here.


class UserDetails(models.Model):
    """docstring forUserDetails."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    sms_verify_token = models.CharField(max_length=10, null=True, blank=True)
    wallet_address = models.CharField(max_length=100, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        """ Meta data for User Details """
        db_table = 'user_details'
        verbose_name_plural = 'User\'s Detail'


class Kyc(models.Model):
    """docstring forKyc."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_proof = models.FileField(upload_to='id_proof')
    address_proof = models.FileField(upload_to='address_proof')
    timestamp = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        """ Meta data for Kyc Model """
        db_table = 'kyc'
        verbose_name_plural = "Manage KYC"


class WhitePaper(models.Model):
    """ Docstring for whitepages """
    title = models.CharField(max_length=200)
    whitepaper = models.FileField(upload_to='whitepapers')
    is_active = models.BooleanField(default=False)

    class Meta:
        """ Meta of White Paper """
        verbose_name = "WhitePaper"
        verbose_name_plural = "White Papers"

    def __str__(self):
        return self.title


class FlatPagesModel(FlatPage):
    """ Docstring for FlatePageModel """
    pass

    class Meta:
        """ Meta application """
        verbose_name_plural = 'CMS'
