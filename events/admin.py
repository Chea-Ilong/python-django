from django.contrib import admin
from .models import Events, EventSponsor, EventPhoto, Host, HostNames, Agenda, AgendaDetail
# Register your models here.
admin.site.register(Events)
admin.site.register(EventSponsor)
admin.site.register(EventPhoto)
admin.site.register(Host)
admin.site.register(HostNames)
admin.site.register(Agenda)
admin.site.register(AgendaDetail)