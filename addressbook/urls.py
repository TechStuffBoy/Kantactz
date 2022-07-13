from django.urls import path
from . import views

urlpatterns = [
    path('home/', view=views.HomeView.as_view(), name='home'),
    path('', view=views.ContactList.as_view(), name='contact-list')
]