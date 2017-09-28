from django.shortcuts import render

from .forms import TransferForm, RequiredFormSet
from .models import Transfer
from django.views.generic.edit import FormView
from django.forms.formsets import TOTAL_FORM_COUNT, formset_factory
from django.shortcuts import redirect,render

#Homepage
def home(request):
	"""
	The homepage view. This will be removed once it is integrated into the sampleman application
	or expanded so that Transfer will be a versatile standalone application

	"""
	return render(request,'transfer01/home.html')

class BulkTransferView(FormView):

	template_name='transfer01/transfer.html'
	TransferAddMoreFormSet = formset_factory(TransferForm, max_num=20, formset=RequiredFormSet)

	def get(self, request, *args, **kwargs):
		context = {}
		context['transfers_addmore_formset'] = self.TransferAddMoreFormSet()
		return self.render_to_response(context)




