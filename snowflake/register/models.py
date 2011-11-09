from django.db import models

class registrant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __unicode__(self):
        return self.email

    
