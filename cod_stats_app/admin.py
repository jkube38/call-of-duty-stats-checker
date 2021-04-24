from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cod_stats_app.models import CodUser


# Register your models here.
UserAdmin.fieldsets += (
    'Gamer_Details', {
        'fields': (
            'gamer_tag',
            'platform'
        )
    }
),

admin.site.Register(CodUser, UserAdmin)