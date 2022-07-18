from rest_framework import serializers
from . import models

class BoardSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=True, max_length=50)
	description = serializers.CharField(max_length=100)
