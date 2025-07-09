from django.urls import path,include
from .views import PricingPlanViewSet, IconViewSet, TeamMemberViewSet, CustomFontViewSet, InvitationTemplatesViewSet,SearchUserByEmailViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pricing-plans', PricingPlanViewSet, basename='pricing-plan')
router.register('icons', IconViewSet, basename='icon')
router.register('team-members',TeamMemberViewSet , basename='team-member')
router.register('invitation-templates', InvitationTemplatesViewSet, basename="invitation-templates")
router.register('custom-fonts', CustomFontViewSet, basename='custom-font')
router.register('search', SearchUserByEmailViewSet, basename='search-user-by-email')
urlpatterns = [
    path('', include(router.urls)),
    
]
            