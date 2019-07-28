from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class RegistrationSerializer(serializers.ModelSerializer):


    password= serializers.CharField(max_length=128,
    min_length=8,write_only=True)

    token = serializers.CharField(max_length=255,
    read_only=True)

    class Meta:
        model = User

        fields = ['last_name','first_name','sex',
        'email','date_birth','password','token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255,write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email',None)

        password = data.get('password',None)

        if email is None:
            raise serializers.ValidationError('An email field is required.')
        
        user = authenticate(username=email,password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('User has been deactivated.')
        
        return {
            'email':user.email,
            'last_name':user.last_name,
            'token':user.token
        }

class UserSerializer(serializers.ModelSerializer):
    """Handle seralization and deserialization of User objects."""

    password = serializers.CharField(max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email','last_name','first_name','password','token')

        read_only_fields = ('token',)

    def update(self,instance, validated_data):
        """Update some informations about the user."""

        password = validated_data.pop('password',None)

        for (key,value) in validated_data.items():
            setattr(instance,key,value)
        
        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
