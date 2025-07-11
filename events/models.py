from django.db import models
from authentications.models import User
from django.core.validators import FileExtensionValidator
from site_setting.models import PricingPlan, InvitationTemplates
from site_setting.models import Icon

# Create your models here.
class Events(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    team_members = models.ManyToManyField(User, related_name='events_as_team_member', blank=True)
    title = models.CharField(max_length=100 ) #
    description = models.TextField(blank=True, null=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    venue_name = models.CharField(max_length=255, null=True, blank=True)

    
    end_time = models.TimeField(blank=True, null=True) 
 
    google_map_embed_link = models.TextField(blank=True, null=True)
    youtube_embed_link = models.TextField(blank=True, null=True)
    video_message_embed_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_publish = models.BooleanField(default = False )

    invitation_background_music = models.FileField(upload_to='music', validators=[FileExtensionValidator(allowed_extensions=['mp3'])], null=True, blank=True)
    logo_kh = models.ImageField(upload_to='logo', null=True, blank=True)
    logo_en = models.ImageField(upload_to='logo', null=True, blank=True)
    loading_screen = models.ImageField(upload_to='loading_screen', null=True, blank=True)
    event_banner = models.ImageField(upload_to='event_banner', blank=True, null=True)
    # Template Transition Video
    transition_video = models.FileField(upload_to='transition_video', null=True, blank=True)

    package_plan = models.ForeignKey(PricingPlan, on_delete=models.SET_NULL, blank=True, null=True)
    invitation_template = models.ForeignKey(InvitationTemplates, on_delete=models.SET_NULL, null=True, blank=True)

    CATEGORY_CHOICES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('housewarming', 'Housewarming'),
        ('conferences', 'Conferences'),
        ('seminars', 'Seminars'),
        ('concert', 'Concert'),
        ('retreat', 'Retreat'),
        ('other', 'Other')
    ]

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default='wedding'
    )
    
    def __str__(self):
        return self.title


class EventSponsor(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_sponsors')
    name = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='event_sponsor_logo', blank=True, null=True)

    def str(self):
        return f"Event {self.event.title} + Sponsor: {self.name}"
    
class EventPhoto(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='event_photos')
    order = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='event_photo', blank=True, null=True)

    def str(self):
        return f"{self.event.title} - {self.order}"
    
class Host(models.Model):
    event = models.ForeignKey(Events, related_name='host', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='host_avatars/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def str(self):    
        return self.event.title


class HostNames(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, related_name='host_names')
    language = models.CharField(max_length=10, default='en')
    host_name = models.CharField(max_length=100, blank=True, null=True)
    parent_a_name = models.CharField(max_length=100, blank=True, null=True)
    parent_b_name = models.CharField(max_length=100, blank=True, null=True)

    def str(self):    
        return f"Event: {self.host.event.title} - {self.host_name} - ({self.language})"


class Agenda(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='agenda')
    date = models.DateField()
    class Meta:
        unique_together = ('event', 'date')
        ordering = ['event', 'date']

    def str(self):
        return f"{self.event.title} - Day {self.date}"


class AgendaDetail(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='agenda_detail')
    language = models.CharField(max_length=10, default='en', help_text='e.g: kh, en, cn')
    agenda_detail = models.CharField(max_length=100, blank=True, null=True)
    time_text = models.CharField(max_length=100, blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)
    icon = models.ForeignKey(Icon, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.agenda.event} - {self.agenda_detail} - {self.agenda.date} - ({self.language})"
    

class InvitationText(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='invitation_texts')
    language = models.CharField(max_length=10, default='en')
    time_text = models.TextField(blank=True, null=True)
    date_text = models.TextField(blank=True, null=True)
    location_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.event.title} - {self.language} invitation text"


class InvitationSubText(models.Model):
    invitation_text = models.ForeignKey(InvitationText, on_delete=models.CASCADE, related_name='invitation_sub_text')
    sub_text = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.invitation_text.event.title} sub-text ({self.order})"
     

class WeddingGiftPaymentMethod(models.Model):
   
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='wedding_gift_methods')  
    account_number = models.CharField(max_length=100, blank=True, null=True)
    account_name = models.CharField(max_length=100, blank=True, null=True)
    payment_url = models.URLField(blank=True, null=True)
    qr_image = models.ImageField(upload_to='qr_image', blank=True, null=True)

    def __str__(self):
        return f"{self.event.title} - {self.account_name}"
    
