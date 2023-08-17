from rest_framework import serializers
from . import models

# We change UserSerializer bc we are  using AbstractUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["id", "name", "email", "password"]
        extra_kwargs = {
            'password': {'write_only': True} # To not show the password in the response
        }
        
    # To save the password hashed
    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
