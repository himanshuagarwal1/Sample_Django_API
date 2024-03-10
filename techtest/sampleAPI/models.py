from django.db import models

# Create your models here.

class Client(models.Model):
    """ A client personal details
    """
    name = models.CharField(max_length=120, )
    contact_number = models.IntegerField(blank = False)
    contact_email = models.EmailField(blank = False)
    status = models.BooleanField(default = True)