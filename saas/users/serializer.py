from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser


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
    hostel = serializers.CharField(
        max_length=30,
        allow_null=False,
        allow_blank=False,
        help_text="User's hostel"
    )
    room_name = serializers.CharField(
        max_length=10,
        allow_null=False,
        allow_blank=False,
        help_text="User's room name"
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
            "hostel",
            "room_name",
            "is_seller",
            "is_buyer"
        ]

    def validate(self, attrs: dict) -> dict:
        """
        Validate request JSON
        """
        all_hostels = ['jaja', 'biobaku', 'eni_njoku', 'mariere']
        if attrs.get('hostel') not in all_hostels:
            raise ValidationError("Invalid hostel")

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
