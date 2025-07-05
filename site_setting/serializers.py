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


class TemplateColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateColor
        fields = "__all__"

class TemplateFontNameSerializer(serializers.ModelSerializer):
    font_name = serializers.CharField(source='font.name', read_only=True)
    font_file = serializers.CharField(source='font.font_file', read_only=True)
    class Meta:
        model = TemplateFontName
        fields = ['id', 'language', 'font', 'font_name', 'font_file']  
             
class InvitationTemplatesSerializer(serializers.ModelSerializer):
    template_colors = TemplateColorSerializer(many=True, read_only=True)
    template_font_name = TemplateFontNameSerializer(many=True, read_only=True)
    package_plan = PricingPlanSerializer(read_only=True)
    class Meta:
        model = InvitationTemplates
        fields = "__all__"