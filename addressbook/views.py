from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Contact

# Create your views here.
class HomeView(TemplateView):
    template_name = 'addressbook/home.html'

class ContactList(ListView):
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)