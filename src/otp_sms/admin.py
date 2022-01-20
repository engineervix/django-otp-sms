from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import CustomSMSDevice


class CustomSMSDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_sms.models.CustomSMSDevice`.
    """
    fieldsets = [
        ('Identity', {
            'fields': ['user', 'name', 'confirmed'],
        }),
        ('Configuration', {
            'fields': ['number'],
        }),
    ]
    raw_id_fields = ['user']


try:
    admin.site.register(CustomSMSDevice, CustomSMSDeviceAdmin)
except AlreadyRegistered:
    # Ignore the useless exception from multiple imports
    pass
