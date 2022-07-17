from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.
def all(request):
	boards = models.Board.objects.all()
	return HttpResponse(boards)
