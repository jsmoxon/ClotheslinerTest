from django.db import models


class Feedback(models.Model):
    subject = models.CharField(max_length =200)
    message = models.CharField(max_length = 10000)
    sender = models.EmailField()
    
    def __unicode__(self):
        return self.subject
    
    


