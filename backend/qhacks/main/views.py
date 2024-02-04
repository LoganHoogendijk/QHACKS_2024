from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from .models import *
# from main.resnet9 import ResNet9
from main.fix import ImageClassifier
from .test import get_model_results
from .recommend import recommender
from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfmiddleware': csrf_token})

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
            user_profile = UserProfile.objects.get(user=user)
            serializer = UserProfileSerializer(user_profile)
            return Response({'message': 'Login successful', 'user': serializer.data})
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
            with transaction.atomic():
                user = serializer.save()
                user_profile_exists = UserProfile.objects.filter(user=user).exists()
                if not user_profile_exists:
                    UserProfile.objects.create(user=user, name=user.username)
                login(request, user)
                return Response({'user': user.id}, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer 

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer 

    def perform_create(self, serializer):
        curr_user = getattr(self.request, 'user', None)
        user_profile = UserProfile.objects.get(user=curr_user)
        crop = serializer.save()
        user_profile.crops.add(crop)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LeafViewSet(viewsets.ModelViewSet):
    queryset = Leaf.objects.all()
    serializer_class = LeafSerializer 

    def perform_create(self, serializer):
        crop_id = self.request.data.get('crop')
        curr_user = getattr(self.request, 'user', None)
        user_profile = UserProfile.objects.get(user=curr_user)
        crop = user_profile.crops.get(id=crop_id)
        leaf = serializer.save()
        crop.leaves.add(leaf)
        return leaf

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save the leaf object
        leaf = self.perform_create(serializer)

        # call the AI model
        res = get_model_results(leaf.image.url)
        print(res)
        # take the results and call OPENAI
        
        recommendations = None
        if res["Healthy"] == 1:
            recommendations = recommender(res["Plant Type"])
        else:
            recommendations = recommender(plant=res["Plant Type"], disease=res["Disease"])

        # Create recommendation objects based on its response
        for recommendation in recommendations:
            recommendation = Recommendation.objects.create(content=recommendation)
            # link the recommendation objects to the leaf object
            leaf.recommendations.add(recommendation)

        
        # return recommendations, and model output
        return Response({"recommendations":recommendations, "output": res}, status=status.HTTP_200_OK)

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer


