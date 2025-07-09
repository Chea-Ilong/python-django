from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import EventsSerializer, EventsDetailSerializer
from .models import Events
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from django.db.models import Q

# Create your views here.
class IsAdminOrTeamMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.admin or request.user in obj.team_members.all()
    

class EventsViewSet(viewsets.ModelViewSet):
    
    permission_classes = [permissions.IsAuthenticated, IsAdminOrTeamMember]

    def get_queryset(self):
        user = self.request.user
        queryset = Events.objects.filter(
            Q(admin=user) | Q(team_members=user)
        ).distinct()
        
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EventsSerializer
        elif self.action in ['retrieve', 'update', 'partial_update']:
            return EventsDetailSerializer
        return EventsDetailSerializer

    def list(self, request):
     queryset = self.get_queryset()
     serializer = self.get_serializer(queryset, many=True)
     return Response(serializer.data)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to create an event.")
        serializer.save(admin=self.request.user)
        
      