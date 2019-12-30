from django.shortcuts import render
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic.edit import FormView

from main import models
from main import forms 


class ProductListView(ListView):
    template_name = "main/product_list.html"
    paginate_by = 4

    def get_queryset(self):
        tag = self.kwargs['tags']
        self.tag = None
        if tag != "all":
            self.tag = get_object_or_404(model.ProductTag, slug=tag)
        
        if self.tag:
            product = models.Product.objects.active().filter(tags=self.tag)
        
        else:
            products = models.Product.objects.active()

        return products.order_by("name")
        


class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)