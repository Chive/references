from django.contrib import admin
from hvad.admin import TranslatableAdmin
from references.models import Reference

class ReferenceAdmin(TranslatableAdmin):
    fieldsets = [
        ('donor', {'fields': ['donor_name','donor_title','donor_logo','donor_detail_img']}),
        ('date', {'fields': ['pub_date']})
    ]

admin.site.register(Reference, ReferenceAdmin)
