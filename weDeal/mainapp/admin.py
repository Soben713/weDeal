from django.contrib import admin

from mainapp.models import Deal


class DealAdmin(admin.ModelAdmin):
    pass


admin.site.register(Deal, DealAdmin)
