from django.contrib import admin
from .models import PricingPlan, TeamMember, Icon, CustomFont, TemplateFontName, TemplateColor, InvitationTemplates

# Register your models here.

admin.site.register(PricingPlan)  
admin.site.register(TeamMember)
admin.site.register(Icon)
admin.site.register(CustomFont)
admin.site.register(InvitationTemplates)
admin.site.register(TemplateFontName)
admin.site.register(TemplateColor)