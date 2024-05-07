from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden, HttpResponse
from django.http.response import Http404

from rest_framework import authentication, permissions, generics, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from .models import User
from .serializers import RegisterSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
