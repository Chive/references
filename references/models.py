from django.db import models
from datetime import datetime
from cms.models.fields import PlaceholderField
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from django.utils.translation import ugettext_lazy as _



def give_file_name(instance, filename):
    return '/'.join(['references', '%s_%s' % (datetime.now(), filename)])

class Reference(models.Model):
    donor_name = models.CharField(max_length=200)
    donor_logo = models.ImageField(upload_to=give_file_name)
    donor_detail_img = models.ImageField(upload_to=give_file_name)
    donor_title = models.CharField(max_length=200)
    reference_text = PlaceholderField('ph_reference_text')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.donor_name

class ReferencePluginModel(CMSPlugin):
    references = models.ManyToManyField(Reference)

######################################################
######################################################
######################################################