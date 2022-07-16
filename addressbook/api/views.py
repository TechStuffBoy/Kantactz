from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import ContactSerializer
from ..models import Contact

from . import custompermissions


class ContactList(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'api-contact-list'

    permission_classes = (
        permissions.IsAuthenticated,
        custompermissions.IsCurrentUserOwner
    )

    def get_queryset(self):
        '''Allow only the creator's contacts'''
        return super().get_queryset().filter(creator=self.request.user)

    def perform_create(self, serializer):
        '''Add the authenticated user automatically as a creator'''
        serializer.save(creator=self.request.user)


class ContactDetail(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'api-contact-detail'

    permission_classes = (
        permissions.IsAuthenticated,
        custompermissions.IsCurrentUserOwner
    )

class ApiRoot(GenericAPIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return(
            Response( {
                'contacts' : reverse(ContactList.name, request=request)
            })
        )