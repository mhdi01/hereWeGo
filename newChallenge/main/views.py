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

from .models import User, Ads, Comments
from .serializers import RegisterSerializer, AdSerializer, ModifyAdSerializer, CreateCommentSerializer \
    , CommentSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class AdsGeneralView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AdSerializer
    queryset = Ads.objects.filter(is_deleted=False).order_by('-created_ts')
    

class RetrieveAdView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AdSerializer
    
    def get_queryset(self):
        try:
            ad = Ads.objects.get(id=self.kwargs['ad_id'])
        except Exception as e:
            print(e)
            raise Http404
        return ad

class CreateAdView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ModifyAdSerializer
    def post(self, request, *args, **kwargs):
        user = self.request.user
        if not 'user' in request.data:request.data['user'] = user.id
        return super().post(request, *args, **kwargs)
    

class UpdateAdView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ModifyAdSerializer
    def get_object(self):
        try:
            return Ads.objects.get(id=self.kwargs['ad_id'])
        except Exception as e:
            print(e)
            raise Http404
        
    def patch(self, request, *args, **kwargs):
        user = self.request.user
        if not 'user' in request.data: request.data['user'] = user.id
        return super().patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        user = self.request.user
        if not 'user' in request.data: request.data['user'] = user.id
        return super().put(request, *args, **kwargs)


class DeleteAdView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serialzer_class = ModifyAdSerializer

    def get_object(self):
        try:
            return Ads.objects.get(id=self.kwargs['ad_id'])
        except Exception as e:
            print(e)
            raise Http404
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=200)
    
class CreateCommentView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateCommentSerializer
    
    def post(self, request, ad_id, *args, **kwargs):
        user = self.request.user
        try:
            ad = Ads.objects.get(id=ad_id)
        except Exception as e:
            print(e)
            raise Http404
        if not 'ad' in request.data: request.data['ad'] = ad.id
        if not 'user' in request.data: request.data['user'] = user.id
        return super().post(request, *args, **kwargs)
    
class ListCommentsView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CommentSerializer
    def get_queryset(self, *args, **kwargs):
        ad_id = self.kwargs['ad_id']
        try:
            ad = Ads.objects.get(id=ad_id)
        except Exception as e:
            print(e)
            raise Http404
        
        return Comments.objects.filter(ad=ad)