from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.models import ApprovalForUser


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = ApprovalForUser
        fields = ['username', 'password',
                  'email', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):

        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError(
                {'Error': 'password does not match'})

        if ApprovalForUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'email': 'email already exist'})

        account = ApprovalForUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        account.password = password
        account.save()

        return account


class UserApprovalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApprovalForUser
        exclude = ['password']


class UserApprovalSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApprovalForUser
        exclude = ['password']
