from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from .models import Profile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = fields


class RegistrationSerializer(serializers.ModelSerializer):
    consent = serializers.BooleanField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'password', 'consent')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8},
            'email': {'required': True},
        }

    def validate_email(self, value):
        value = value.lower()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(
                "Un compte existe déjà avec cet e-mail."
            )
        return value

    def validate_password(self, value):
        django_validate_password(value)
        return value

    def validate_consent(self, value):
        if not value:
            raise serializers.ValidationError("Le consentement est obligatoire.")
        return value

    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop('consent')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(
            user=user,
            email=user.email,
            consentement_date=timezone.now(),
        )
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id', 'user', 'genre', 'datenaissance', 'pays', 'province',
            'ville', 'Adresse', 'email', 'date_Inscription', 'telephone',
            'consentement_date',
        )
        read_only_fields = ('id', 'user', 'date_Inscription', 'consentement_date')