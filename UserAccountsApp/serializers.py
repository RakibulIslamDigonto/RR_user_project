from django.contrib.auth.models import User
from rest_framework import serializers
from UserAccountsApp.models import CustomUser,UserProfile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth', 'created_at', 'update_time')


class UserRegisterSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='profile')
    email = serializers.EmailField(required = True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth', 'created_at', 'update_time')
        extra_kwargs = {
            'first_name':{'required':True},
            'date_of_birth':{'required':True},
        }

    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        password2 = validated_data['password2']
        date_of_birth = validated_data['date_of_birth']
        profile_pop_data = validated_data.pop['profile']

        if password != password2:
            raise ValueError('Password Does not match')
        user = CustomUser.objects.create(email=email, date_of_birth=date_of_birth)  #f_name?
        user.set_password('password')
        user.save()
        UserProfile.objects.create(user=user, **profile_pop_data)
        return user

        
        


        


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'date_of_birth', 'created_at', 'update_time')
        