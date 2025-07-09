from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from authentications.models import User
from authentications.serializers import UserSerializer
from .models import PricingPlan, TeamMember, Icon, CustomFont, InvitationTemplates, TemplateFontName, TemplateColor
from .serializers import PricingPlanSerializer, TeamMemberSerializer, IconSerializer, CustomFontSerializer, InvitationTemplatesSerializer, TemplateColorSerializer, TemplateFontNameSerializer
# Create your views here.

class PricingPlanViewSet(viewsets.ModelViewSet):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
        
    
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    
  
class IconViewSet(viewsets.ModelViewSet):
    queryset = Icon.objects.all()
    serializer_class = IconSerializer
    

class CustomFontViewSet(viewsets.ModelViewSet):
    queryset = CustomFont.objects.all()
    serializer_class = CustomFontSerializer


class InvitationTemplatesViewSet(viewsets.ModelViewSet):
    queryset = InvitationTemplates.objects.all()
    serializer_class = InvitationTemplatesSerializer

class TemplateColorViewSet(viewsets.ModelViewSet):
    queryset = TemplateColor.objects.all()
    serializer_class = TemplateColorSerializer


class TemplateFontNameViewSet(viewsets.ModelViewSet):
    queryset = TemplateFontName.objects.all()
    serializer_class = TemplateFontNameSerializer
    
class SearchUserByEmailViewSet(viewsets.ViewSet):
    """
    Search users by email for adding as team members
    """
    def list(self, request):
        email = request.query_params.get('email', None)
        if not email:
            return Response({"error": "Email parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise NotFound(detail="User with this email does not exist.")