from django.urls import path
from addressbook.api import views as views_v1

urlpatterns = [
    path('contacts/', view=views_v1.ContactList.as_view(), name=views_v1.ContactList.name),
    path('contacts/<int:pk>', view=views_v1.ContactDetail.as_view(), name=views_v1.ContactDetail.name),
]