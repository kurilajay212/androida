from rest_framework import serializers
from .models import Pat,user
    #, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pat
        fields = ('user_name', 'user_email', 'user_password')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=('emailId','password') 