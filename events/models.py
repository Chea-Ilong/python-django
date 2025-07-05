from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from site_setting.models import PricingPlan, InvitationTemplates

# Create your models here.
class Events(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events_as_team_member', blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    venue_name = models.CharField(max_length=200, blank=True, null=True)
 
    google_map_embed_link = models.TextField(blank=True, null=True)
    youtube_embed_link = models.TextField(blank=True, null=True)
    video_message_embed_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
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

    def visit_count(self):
        return self.visits.count()
    
    visit_count.short_description = "Visit Count"

    def count_guests_coming(self):
        return self.rsvp_set.filter(attending=True).count()
    
    def count_guests_not_coming(self):
        return self.rsvp_set.filter(attending=False).count()
    
    def count_comments(self):
        return self.comments.count()
    
    def count_reviews(self):
        return self.reviews.count()
    
    def str(self):
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