from django.db import models

class Reference(models.Model):
    donor_name = models.TextField()
    donor_logo = models.ImageField()
    donor_detail_img = models.ImageField()
    donor_title = models.TextField()
    reference_text = models.TextField()