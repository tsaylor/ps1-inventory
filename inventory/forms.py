from django import forms
from inventory.models import Item
from django.contrib.admin.widgets import AdminDateWidget

class ItemForm(forms.ModelForm):
	donation_date = forms.DateField(widget=AdminDateWidget())
	class Meta:
		model = Item
