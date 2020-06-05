from django.db import models

# Create your models here.
class Person(models.Model):
	eid = models.IntegerField()
	name = models.CharField(max_length=50)
	contact = models.IntegerField()
	address = models.CharField(max_length=300)

	def __str__(self):
		return self.name

	class Meta:
		db_table = "person"
		verbose_name_plural = "person"