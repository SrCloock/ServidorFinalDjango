from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Empresa, Videojuego
from .serializers import EmpresaSerializer, VideojuegoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class VideojuegoViewSet(viewsets.ModelViewSet):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class EmpresaListView(ListView):
    model = Empresa

class EmpresaDetailView(DetailView):
    model = Empresa

class EmpresaCreateView(CreateView):
    model = Empresa
    fields = ['nombre', 'descripcion']

class EmpresaUpdateView(UpdateView):
    model = Empresa
    fields = ['nombre', 'descripcion']

class VideojuegoListView(ListView):
    model = Videojuego

class VideojuegoDetailView(DetailView):
    model = Videojuego

class VideojuegoCreateView(CreateView):
    model = Videojuego
    fields = ['nombre', 'empresa', 'descripcion']

class VideojuegoUpdateView(UpdateView):
    model = Videojuego
    fields = ['nombre', 'empresa', 'descripcion']
