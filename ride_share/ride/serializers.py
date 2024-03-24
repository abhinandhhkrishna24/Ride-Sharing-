from rest_framework import serializers
from .models import User ,Ride

class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError("This username already exists. Please try another one.")

        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Both passwords must match.")

        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}



class RideSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ride
        fields= '__all__'

    