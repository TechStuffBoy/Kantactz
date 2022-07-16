from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Contact

User = get_user_model()

class ContactSerializer(serializers.ModelSerializer):

    # If we uncomment the below one, then we will get the username as 'creator', but it will eagerly query the database
    # creator = serializers.SlugRelatedField(queryset=User.objects.all(),
	# 	slug_field='username')

    creator = serializers.ReadOnlyField(source='creator.username')
    
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