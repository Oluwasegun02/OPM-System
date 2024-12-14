from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Portfolio, Project
from .serializers import PortfolioSerializer, ProjectSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
