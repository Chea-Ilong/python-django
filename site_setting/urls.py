from django.urls import path,include
from .views import PricingPlanViewSet, IconViewSet, TeamMemberViewSet, CustomFontViewSet, InvitationTemplatesViewSet, TemplateColorViewSet, TemplateFontNameViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pricing-plans', PricingPlanViewSet, basename='pricing-plan')
router.register('icons', IconViewSet, basename='icon')
router.register('team-members',TeamMemberViewSet , basename='team-member')
router.register('custom-fonts', CustomFontViewSet, basename='custom-font')
router.register('invitation-templates', InvitationTemplatesViewSet, basename="invitation-templates")
router.register('color-templates', TemplateColorViewSet, basename="color-templates")
router.register('fontname-templates', TemplateFontNameViewSet, basename="fontname-templates")

urlpatterns = [
    path('', include(router.urls)),
    
]
