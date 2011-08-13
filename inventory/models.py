from django.db import models
from django.contrib.auth.models import User

POWER_CHOICES = (
    ('120v', '120v'),
    ('240v', '240v'),
    ('3phase', '3 phase'),
)

class Item(models.Model):
	name = models.CharField(max_length=50, blank=True, help_text="What we call it")
	manufacturer = models.CharField(max_length=50, blank=True)
	model_name = models.CharField(max_length=50, blank=True)
	model_number = models.CharField(max_length=50, blank=True)
	serial_number = models.CharField(max_length=50, blank=True)
	photo1 = models.FileField(upload_to='photos/%Y/%m/%d', blank=True)
	photo2 = models.FileField(upload_to='photos/%Y/%m/%d', blank=True)
	photo3 = models.FileField(upload_to='photos/%Y/%m/%d', blank=True)
	replacement_cost = models.IntegerField(blank=True, null=True, help_text="What it costs to replace with a brand new unit")
	donor = models.CharField(max_length=50, blank=True)
	donation_date = models.DateField(blank=True, null=True)
	donation_notes = models.TextField(blank=True)
	voltage = models.CharField(max_length=10, choices=POWER_CHOICES, blank=True, default="120v")
	amps_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	watts_rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	supplies_needed = models.TextField(blank=True, help_text="Consumables and associated stuff used with the item")
	general_notes = models.TextField(blank=True)

	def __unicode__(self):
		return self.name
