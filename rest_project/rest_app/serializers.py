from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueTogetherValidator

from .models import BookModel #, User
from django.contrib.auth.forms import UserCreationForm

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"
        #exclude = ['user_id' , 'publish_date']
''' 
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        #model=UserCreationForm
        fields = ['username', 'password']
'''

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style = {'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'}, help_text=(
        "Enter the same password as before, for verification."))
    class Meta():
            model = User
            fields = ['username', 'password', 'confirm_password']

