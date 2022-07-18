from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.core import serializers
from . import models
from . import serializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET', 'POST'])
def all(request):
	if request.method == 'GET':
		boards = list(models.Board.objects.all().values())
		return JsonResponse(boards, safe=False)
	elif request.method == 'POST':
		serialized = serializer.BoardSerializer(data=request.data)
		if (serialized.is_valid()):
			print(serialized.data)
		print(request.data)
		return JsonResponse({"received":True})
