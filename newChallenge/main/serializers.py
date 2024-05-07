from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Ads, Comments
from .validators import CustomPasswordValidator

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message='ایمیل وارد شده قبلا استفاده شده است')]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[CustomPasswordValidator()])
    class Meta:
        model = User
        fields = ('password', 'email')
        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True}
        }

    def create(self, validated_data):
        email_qs = User.objects.filter(email=(validated_data['email']).lower()).first()
        if email_qs:
            raise serializers.ValidationError({"password": "این ایمیل قبلا استفاده شده است"})
        user = User.objects.create(
            email=(validated_data['email']).lower()
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_authorized', 'created_ts', 'is_deleted')


class AdSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Ads
        fields = ('user', 'title', 'content', 'created_ts', 'is_deleted', 'is_active')
