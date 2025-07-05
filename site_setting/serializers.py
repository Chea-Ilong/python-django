from rest_framework import serializers
from .models import PricingPlan, TeamMember, Icon, CustomFont, InvitationTemplates, TemplateColor, TemplateFontName

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = "__all__"
    
class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"
        
class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = "__all__"
        
class CustomFontSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomFont
        fields = "__all__"

class InvitationTemplatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationTemplates
        fields = "__all__"

class TemplateColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateColor
        fields = "__all__"

class TemplateFontNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateFontName
        fields = "__all__"       