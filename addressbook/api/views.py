from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response

from .serializers import ContactSerializer
from ..models import Contact


class ContactList(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'api-contact-list'

class ContactDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'api-contact-detail'

class ApiRoot(GenericAPIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return(
            Response( {
                'contacts' : reverse(ContactList.name, request=request)
            })
        )