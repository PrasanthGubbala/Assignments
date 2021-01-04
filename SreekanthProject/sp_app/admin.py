from django.contrib import admin
from django.contrib.auth.models import Group,User
# from sp_app.models import User as user
from sp_app.models import Projects


admin.site.unregister(Group)
admin.site.unregister(User)

# admin.site.register(user)
admin.site.register(Projects)



