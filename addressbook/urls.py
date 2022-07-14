from django.urls import path
from . import views

urlpatterns = [
    path('home/', view=views.HomeView.as_view(), name='home'),
    path('', view=views.ContactList.as_view(), name='contact-list'),
    path('<int:pk>/', view=views.ContactDetail.as_view(), name='contact-detail'),
    path('create/', view=views.ContactCreate.as_view(), name='contact-add'),
    path('<int:pk>/edit/', view=views.ContactUpdate.as_view(), name='contact-edit'),
    path('<int:pk>/delete/', view=views.ContactDelete.as_view(), name='contact-delete'),
    path('upload-csv/', view=views.upload_csv, name='upload-csv'),
]