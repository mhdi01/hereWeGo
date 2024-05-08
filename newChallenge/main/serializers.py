from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import NotAcceptable

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
        email = validated_data['email']
        email_qs = User.objects.filter(email=(email).lower()).first()
        if email_qs:
            raise serializers.ValidationError({"password": "این ایمیل قبلا استفاده شده است"})
        user = User.objects.create(
            email=(email).lower()
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'is_active', 'is_authorized', 'created_ts', 'is_deleted')


class AdSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Ads
        fields = ('id', 'user', 'title', 'content', 'created_ts', 'is_deleted', 'is_active')

class ModifyAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('id', 'user', 'title', 'content', 'created_ts', 'is_deleted', 'is_active')


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user', 'ad', 'content', 'created_ts', 'is_deleted')   

    def create(self, validated_data):
        cm_query = Comments.objects.filter(user=validated_data['user'], ad=validated_data['ad']).first()
        if cm_query: raise NotAcceptable(detail='عملیات موردنظر مجاز نیست. کامنت تکراری')
        return super().create(validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    ad = AdSerializer()
    class Meta:
        model = Comments
        fields = ('id','user', 'ad', 'content', 'created_ts', 'is_deleted')