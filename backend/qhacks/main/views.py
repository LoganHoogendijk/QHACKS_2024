from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, UserRegistrationSerializer, LeafSerializer, RecommendationSerializer
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def signin(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

    @action(detail=False, methods=['post'])
    def signout(self, request):
        logout(request)
        return Response({'message': 'Logout successful'})


    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'Registration successful'}, status=201)
        else:
            return Response(serializer.errors, status=400)

class LeafViewSet(viewsets.ModelViewSet):
    queryset = Leaf.objects.all()
    serializer_class = LeafSerializer 

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


