from django.db import models

class UserPant(models.Model):
    designer = models.CharField(max_length=200, null=True, blank=True)
    style = models.CharField(max_length=200, null=True, blank=True)
    label_waist = models.FloatField(null=True, blank=True, default=1)
    label_inseam = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    inseam = models.FloatField(null=True, blank=True)
    front_rise = models.FloatField(null=True, blank=True)
    back_rise = models.FloatField(null=True, blank=True)
    cuff = models.FloatField(null=True, blank=True)
    thigh = models.FloatField(null=True, blank=True)
    knee = models.FloatField(null=True, blank=True)
    hips = models.FloatField(null=True, blank=True)
    outseam = models.FloatField(null=True, blank=True)
	
    def __unicode__(self):
       	a = "" if self.designer is None else self.designer
       	b = "" if self.style is None else self.style
       	c = "" if self.label_waist is None else self.label_waist
       	d = "" if self.label_inseam is None else self.label_inseam
       	return a+" "+b+" "+str(c)+" "+str(d) if a+b+str(c)+str(d) !="" else "Some pants"
		
		
