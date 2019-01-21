from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from django.contrib.flatpages.models import FlatPage
from main.models import FlatPagesModel
# Register your models here.


admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(FlatPage)
admin.site.register(FlatPagesModel)
