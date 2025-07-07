from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import EventsSerializer
from .models import Events
from django.core.exceptions import PermissionDenied
from django.db.models import Q

# Create your views here.
class IsAdminOrTeamMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.admin or request.user in obj.team_members.all()

class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeamMember]

    def get_queryset(self):
        return Events.objects.filter(
            Q(admin=self.request.user) | Q(team_members=self.request.user)
        ).distinct()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(admin=self.request.user)
        else:
            raise PermissionDenied("You must be logged in to create an event.")