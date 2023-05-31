from django.contrib import admin
from .models import Contact

"""
class Images(admin.ModelAdmin):
    readonly_fields = ('id',)
"""

# Register your models here.
admin.site.register(Contact)
