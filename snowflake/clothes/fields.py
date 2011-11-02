from django.db import models

class DisplayedFloatField(models.FloatField):
	__metaclass__ = models.SubfieldBase
	def to_python(self, value):
		if value - int(value) != 0:
			return value
		return int(value)

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^clothes\.fields\.DisplayedFloatField"])