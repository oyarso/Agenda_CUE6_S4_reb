from django.shortcuts import render 
# Create your views here. 
from django.http import HttpResponse 
def index2(request): 
    return HttpResponse("Bienvenidos a mi sitio de libros")
def index(request): 
    return HttpResponse("Bienvenidos a mi sitio")