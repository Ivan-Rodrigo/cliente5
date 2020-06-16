from rest_framework import routers,serializers,viewsets

from Example2.models import Example2

class Example1Serializer2(serializers.ModelSerializer):
    class Meta:
        model = Example2
        fields = ('__all__')