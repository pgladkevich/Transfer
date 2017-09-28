from django import forms
from .models import Transfer
from django.forms.formsets import TOTAL_FORM_COUNT
from django.forms.formsets import BaseFormSet

class TransferForm(forms.Form):
	
	source_slot = forms.CharField(max_length=255)
	source_well = forms.CharField(max_length=255)
	volume = forms.FloatField()
	destination_slot = forms.CharField(max_length=255)
	destination_well = forms.CharField(max_length=255)

class RequiredFormSet(BaseFormSet):
	def total_form_count(self):
		"""Returns the total number of forms in this FormSet."""
		if self.data or self.files:
			return self.management_form.cleaned_data[TOTAL_FORM_COUNT]
		else:
			if self.initial_form_count() > 0:
				total_forms = self.initial_form_count()
			else:
				total_forms = self.initial_form_count() + self.extra
			if total_forms > self.max_num > 0:
				total_forms = self.max_num
			return total_forms
	
	def __init__(self, *args, **kwargs):
		super(RequiredFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted = False

	