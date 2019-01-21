""" Admin Registration page """
from django.contrib import admin
from main.models import Kyc
from .models import UserDetails
from .models import WhitePaper


# Actions of Admin
def activate_selected(modeladmin, request, queryset):
    queryset.update(is_approved=True)


def deactivate_selected(modeladmin, request, queryset):
    queryset.update(is_approved=False)


# Short Description
activate_selected.short_description = 'Activate selected Items'
deactivate_selected.short_description = 'Deactivate selected Items'


# Register your models here.
class WhitePaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


class KycAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_approved', 'timestamp']
    actions = [activate_selected, deactivate_selected]


admin.site.register(Kyc, KycAdmin)
admin.site.register(UserDetails)
admin.site.register(WhitePaper, WhitePaperAdmin)