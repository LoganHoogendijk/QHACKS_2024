from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Leaf, Recommendation, Crop, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password'] 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        UserProfile.objects.create(user=user)
        return user
    
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = "__all__"


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = "__all__"

class LeafSerializer(serializers.ModelSerializer):

    recommendations = RecommendationSerializer(many=True, required=False)

    class Meta:
        model = Leaf
        fields = ['image', 'recommendations']
