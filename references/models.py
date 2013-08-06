from django.db import models
from time import time

def give_file_name(instance, filename):
    return '/'.join(['references', instance.user.username, time.time() + '_' + filename])

class Reference(models.Model):
    donor_name = models.TextField()
    donor_logo = models.ImageField(upload_to=give_file_name)
    donor_detail_img = models.ImageField(upload_to=give_file_name)
    donor_title = models.TextField()
    reference_text = models.TextField()