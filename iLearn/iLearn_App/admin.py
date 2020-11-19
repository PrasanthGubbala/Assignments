from django.contrib import admin
from django.contrib.auth.models import User, Group

from iLearn_App.models import TecherRegistration,ParentRegistration

admin.site.register(TecherRegistration)
admin.site.register(ParentRegistration)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "iLearn"
# admin.site.site_title = ""
admin.site.index_title = "Teachers Registration"