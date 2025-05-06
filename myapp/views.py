from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Product

@permission_classes([IsAuthenticated])
def index(request):
    return render(request, 'index.html', {'user': request.user})

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'profile.html')

def home(request):
    products = Product.objects.all()
    return render(request, 'home/home.html', {'products': products})

def login(request):
    return render(request, 'auth/signin.html')

def chat(request):
    return render(request, 'chat/chat.html')