# core/views.py

from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Project, Loan, BlogPost
from .serializers import UserSerializer, ProjectSerializer, LoanSerializer, BlogPostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
def home(request):
    return render(request, "home.html")
def about_us(request):
    return render(request, "about_us.html")
def services(request):
    return render(request, "services.html")
def about_us(request):
    return render(request, "about_us.html")