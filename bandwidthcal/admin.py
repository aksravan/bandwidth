from django.contrib import admin
from .models import Device, Activity, Result

admin.site.register(Result)

class ActivityAdmin(admin.StackedInline):
    model = Activity

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    inlines = [ActivityAdmin]

    class Meta:
       model = Device

@admin.register(Activity)
class CompanyStudentsAdmin(admin.ModelAdmin):
    pass
