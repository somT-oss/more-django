from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import AuthenticationFailed

from .models import CustomUser

from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class CreateCustomUserserializers(serializers.ModelSerializer):
    first_name = serializers.CharField(
        max_length=50,
        allow_null=False,
        allow_blank=False,
        help_text="User's first name"
    )
    last_name = serializers.CharField(
        max_length=50,
        allow_null=False,
        allow_blank=False,
        help_text="User's last name"
    )
    email = serializers.EmailField(
        help_text="User's email"
    )
    password = serializers.CharField(
        max_length=16,
        allow_null=False,
        allow_blank=False,
        help_text="User's password"
    )
    is_seller = serializers.BooleanField(
        default=False,
        help_text="True; if user is seller, else; False"
    )
    is_buyer = serializers.BooleanField(
        default=False,
        help_text="True; if user is buyer, else; False"
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "is_seller",
            "is_buyer"
        ]

    def validate(self, attrs: dict) -> dict:
        """
        Validate request JSON
        """
        if attrs.get('is_seller') and attrs.get('is_buyer'):
            raise ValidationError('You cannot be both a buyer and seller')

        return attrs

    def create(self, validated_data) -> CustomUser:
        """
        Create user from validated JSON
        """
        user = CustomUser.objects.create_user(
            **validated_data
        )
        user.save()
        return user


class CustomUsersLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password"
        ]

class ForgotPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = [
            'email'
        ]

class ResetPasswordSerializer(serializers.Serializer):
    id_base64 = serializers.CharField(max_length=16)
    token = serializers.CharField(max_length=254)
    new_password = serializers.CharField(max_length=16)
    confirm_password = serializers.CharField(max_length=16)

    class Meta:
        fields = [
            'id_base64',
            'token',
            'new_password',
            'confirm_password',
        ]
    
    def validate(self, attrs):
        try:
            token = attrs.get('token')
            id_base64 = attrs.get('id_base64')
            new_password = attrs.get('new_password')
            confirm_password = attrs.get('confirm_password')

            user_id = force_str(urlsafe_base64_decode(id_base64))
            user = get_object_or_404(CustomUser, user_id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            
            if new_password != confirm_password:
                raise ValidationError('Password mismatch')

            if user.check_password(raw_password=new_password):
                raise ValidationError('New password cannot be the same as old password')

            user.set_password(new_password)
            user.save()

        except Exception as e:
            raise e
        return attrs
