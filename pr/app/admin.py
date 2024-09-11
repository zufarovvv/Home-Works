from django.contrib import admin

from app.models import Parrent, Child, IceCream

# Register your models here.

admin.site.register(IceCream)
admin.site.register(Child)
admin.site.register(Parrent)
