from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages


from .models import Contact

# Create your views here.
class HomeView(TemplateView):
    template_name = 'addressbook/home.html'

class ContactList(ListView):
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Contact.objects.filter(
                Q(name__icontains=query) | 
                Q(number__icontains=query) |
                Q(email__icontains=query) |
                Q(email2__icontains=query)
            ).filter(creator=self.request.user)
        else:
            return super().get_queryset().filter(creator=self.request.user)

class ContactDetail(DetailView):
    model = Contact
    context_object_name = 'contact'


class ContactCreate(CreateView):
    model = Contact
    fields = ['name' , 'number', 'country_code', 'email', 'email2']
    action = 'Add'

    def get_success_url(self):
        return reverse('contact-list')
    
    def form_valid(self, form):
        messages.success(self.request,'Contact Created!')
        form = form.save(commit=False)
        form.creator = self.request.user # Update the user here
        return super().form_valid(form)

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['name' , 'number', 'country_code', 'email', 'email2']
    action = 'Edit'

    def get_success_url(self):
        return reverse(
            "contact-detail",
            kwargs={'pk':self.kwargs['pk']}
        )
    
    def return_to_list_view(self):
        return reverse('contact-list')
    
    def form_valid(self, form):
        messages.success(self.request, f"Contact Updated!")
        return super().form_valid(form)


class ContactDelete(DeleteView):
    model = Contact
    success_message = "Contact deleted successfully!"

    def get_success_url(self):
        return reverse('contact-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    
    



