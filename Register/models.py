# from django.db import models
# from django.contrib.auth.models import User

# from rest_framework import serializers

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.CharField()
#     password = serializers.CharField()


#     def create(self, validate_data):
#         instance = User()

#         instance.username = validate_data.get('username')
#         instance.email = validate_data.get('email')
#         instance.password = validate_data.get('password')
#         instance.set_password(validate_data.get('password'))
#         instance.save()
#         return instance


#     def validate_username(self,data):
#         users = User.objects.filter(username = data)
#         if len(users) !=0:
#             raise serializers.ValidationError("Usuario Existente")
#         else :
#             return data

    