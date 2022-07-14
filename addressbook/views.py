from itertools import islice
from django.db import IntegrityError

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Contact


# Create your views here.
class HomeView(TemplateView):
    template_name = 'addressbook/home.html'

class ContactList(LoginRequiredMixin,  ListView):
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 3

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


class ContactDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Contact
    context_object_name = 'contact'

    def test_func(self):
        obj = self.get_object(id=self.kwargs['pk'])
        return obj.creator == self.request.user


class ContactCreate(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name' , 'number', 'country_code', 'email', 'email2']
    action = 'Add'

    def get_success_url(self):
        return reverse('contact-list')
    
    def return_to_list_view(self):
        return reverse('contact-list')
    
    def form_valid(self, form):
        messages.success(self.request,'Contact Created!')
        form = form.save(commit=False)
        form.creator = self.request.user # Update the user here
        return super().form_valid(form)
    

class ContactUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
    
    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user


class ContactDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_message = "Contact deleted successfully!"

    def get_success_url(self):
        return reverse('contact-list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user
    
    
# Upload CSV file view
def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES["csv_file"] # gives file_name.csv
        if not csv_file.name.endswith('.csv'):
            messages.error(request,'File is not CSV type')
            return HttpResponseRedirect(reverse("contact-list"))

        # Read the contents from csv file
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        lines = (line.strip() for line in lines)
        lines = islice(lines, 1, None) # Skip the headers

        # Now create or update the data
        for line in lines:
            fields = line.split(',')
            try:
                _, created = Contact.objects.update_or_create(
                    name = fields[0],
                    number = fields[1],
                    country_code = fields[2],
                    email = fields[3],
                    email2 = fields[4],
                    creator = request.user
                )
            except IntegrityError as e:
                messages.warning(request, f"{line} already there.. Please correct and try again!")

        messages.success(request, 'Successfully created/updated all the entries')
        return HttpResponseRedirect(reverse("contact-list"))
       


