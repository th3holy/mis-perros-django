from django.contrib import admin

from .models import huerfano
# Register your models here
class huerfanoAdmin(admin.ModelAdmin):
    readonly_fields = ('Created','Update' )



admin.site.register(huerfano,huerfanoAdmin)