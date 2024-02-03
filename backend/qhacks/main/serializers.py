from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Leaf, Recommendation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


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
        return user

class LeafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaf
        fields = "__all__"

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields= "__all__"