from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Contact

User = get_user_model()

class ContactSerializer(serializers.ModelSerializer):
    
    creator = serializers.SlugRelatedField(queryset=User.objects.all(),
		slug_field='username')
    
    class Meta:
        model = Contact
        fields = ('id', 
            'name', 
            'number', 
            'country_code', 
            'email', 
            'email2', 
            'creator', 
            'created_at', 
            'updated_at'
        )