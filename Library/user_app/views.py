from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserApprovalListSerializer, UserApprovalSerializer
from rest_framework.response import Response
from rest_framework import status
from user_app.models import ApprovalForUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your views here.


class Registration_view(APIView):
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['notification'] = 'successfully registered wait for approval'
        return Response(data)


class User_approval_list_view(APIView):
    def get(self, request):
        list_approval = ApprovalForUser.objects.filter(approval=False)

        serializer = UserApprovalListSerializer(list_approval, many=True)
        return Response(serializer.data)


class User_approval_view(APIView):
    def get(self, request, pk):
        try:
            userapproval = ApprovalForUser.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': 'file not found'})
        serializer = UserApprovalSerializer(userapproval)
        return Response(serializer.data)

    def put(self, request, pk):
        userapproval = ApprovalForUser.objects.get(pk=pk)
        serializer = UserApprovalSerializer(userapproval, data=request.data)

        if serializer.is_valid():
            account = serializer.save()

            approveduser = User.objects.create(username=account.username)
            hashed_password = make_password(account.password)
            approveduser.password = hashed_password

            approveduser.save()
            data = {'Notification': 'Approval is given to that user'}
            return Response(data)


class Logout_view(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response({'Logout': 'Successfull'}, status=status.HTTP_200_OK)


# return Response({'Registration': 'Successfull', 'Approval': 'waiting'}, status=status.HTTP_200_OK)
