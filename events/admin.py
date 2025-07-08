from django.contrib import admin
from .models import (
    Events, EventSponsor, EventPhoto,
    Host, HostNames, Agenda, AgendaDetail, InvitationText, InvitationSubText
)

# 1. Inline for HostNames under Host
class HostNamesInline(admin.TabularInline):
    model = HostNames
    extra = 1

# 2. Inline for Host under Events
class HostInline(admin.StackedInline):
    model = Host
    extra = 1
    inlines = [HostNamesInline]  # Not directly supported like this

# 3. Inline for EventSponsor under Events
class EventSponsorInline(admin.TabularInline):
    model = EventSponsor
    extra = 1

# 4. Inline for EventPhoto under Events
class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 1

# 5. Inline for AgendaDetail under Agenda
class AgendaDetailInline(admin.TabularInline):
    model = AgendaDetail
    extra = 1

# 6. Inline for Agenda under Events
class AgendaInline(admin.StackedInline):
    model = Agenda
    extra = 1

class EventsAdmin(admin.ModelAdmin):
    inlines = [EventSponsorInline, EventPhotoInline, AgendaInline, HostInline]
    list_display = ['title', 'category', 'date', 'venue_name']

class HostAdmin(admin.ModelAdmin):
    inlines = [HostNamesInline]
    list_display = ['event', 'created_at']

class AgendaAdmin(admin.ModelAdmin):
    inlines = [AgendaDetailInline]
    list_display = ['event', 'date']

# Registering models
admin.site.register(Events, EventsAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(AgendaDetail)
admin.site.register(HostNames)
admin.site.register(InvitationText)
admin.site.register(InvitationSubText)