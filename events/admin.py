from django.contrib import admin
import nested_admin
from .models import (
    Events, EventSponsor, EventPhoto,
    Host, HostNames, Agenda, AgendaDetail, InvitationText, InvitationSubText, WeddingGiftPaymentMethod
)

# Add to INSTALLED_APPS in settings.py
# 'nested_admin',
class WeddingGiftPaymentMethodInline(nested_admin.NestedTabularInline):
    model = WeddingGiftPaymentMethod
    extra = 1
# 1. Inline for HostNames under Host
class HostNamesInline(nested_admin.NestedTabularInline):
    model = HostNames
    extra = 1

# 2. Inline for Host under Events (with nested HostNames)
class HostInline(nested_admin.NestedStackedInline):
    model = Host
    extra = 1
    inlines = [HostNamesInline]  # Now nested inlines work!

# 3. Inline for EventSponsor under Events
class EventSponsorInline(nested_admin.NestedTabularInline):
    model = EventSponsor
    extra = 1

# 4. Inline for EventPhoto under Events
class EventPhotoInline(nested_admin.NestedTabularInline):
    model = EventPhoto
    extra = 1

# 5. Inline for AgendaDetail under Agenda
class AgendaDetailInline(nested_admin.NestedTabularInline):
    model = AgendaDetail
    extra = 1

# 6. Inline for Agenda under Events (with nested AgendaDetail)
class AgendaInline(nested_admin.NestedStackedInline):
    model = Agenda
    extra = 1
    inlines = [AgendaDetailInline]

# 7. Inline for InvitationSubText under InvitationText
class InvitationSubTextInline(nested_admin.NestedTabularInline):
    model = InvitationSubText
    extra = 1

# 8. Inline for InvitationText under Events (with nested InvitationSubText)
class InvitationTextInline(nested_admin.NestedStackedInline):
    model = InvitationText
    extra = 1
    inlines = [InvitationSubTextInline]

class EventsAdmin(nested_admin.NestedModelAdmin):
    inlines = [EventSponsorInline, EventPhotoInline, AgendaInline, HostInline, InvitationTextInline, WeddingGiftPaymentMethodInline]

# Registering models
admin.site.register(Events, EventsAdmin)
