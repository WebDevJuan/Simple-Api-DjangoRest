from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    # Cualquier cliente va a poder realizar un petición al servidor con AllowAny
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


