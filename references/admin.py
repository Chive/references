from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from references.models import Reference

class ReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('donor', {'fields': ['donor_name','donor_title','donor_logo','donor_detail_img']}),
        ('date', {'fields': ['pub_date']})
    ]

admin.site.register(Reference, ReferenceAdmin)
