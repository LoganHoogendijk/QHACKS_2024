from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # Replace with your actual serializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def signin(self, request):
        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if authentication was successful
        if user:
            # Log in the user
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=401)

    @action(detail=False, methods=['post'])
    def signout(self, request):
        # Log out the user
        logout(request)
        return Response({'message': 'Logout successful'})

    @action(detail=False, methods=['post'])
    def register(self, request):
        # Use your UserRegistrationSerializer for registration data
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            # Create a new user
            user = serializer.save()

            # Log in the new user
            login(request, user)

            return Response({'message': 'Registration successful'}, status=201)
        else:
            return Response(serializer.errors, status=400)

    # ... other actions ...

# Your UserRegistrationSerializer needs to be defined here
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Adjust fields as needed
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user with a hashed password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
