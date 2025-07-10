from rest_framework import serializers
from django.db import models
from django.core.validators import FileExtensionValidator


class PricingPlan(models.Model):
    
    name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    features = models.TextField(help_text="Add features separated by a comma, e.g., 'Feature1, Feature2, Feature3'")
    purchase_link = models.URLField(blank=True, null=True, help_text="Link to purchase the plan")

    def get_features_list(self):
        """Return features as a list."""
        return [feature.strip() for feature in self.features.split(",")]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='team_profile', blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    telegram_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class CustomFont(models.Model):
    """
    Stores custom fonts that can be uploaded and used in invitation templates.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="A unique name for the font, e.g., 'Roboto', 'Open Sans'."
    )
    font_file = models.FileField(
        upload_to='fonts/',
        validators=[FileExtensionValidator(allowed_extensions=['ttf', 'otf', 'woff', 'woff2'])],
        help_text="Upload a font file (TTF, OTF, WOFF, WOFF2)."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Custom Font"
        verbose_name_plural = "Custom Fonts"
        ordering = ['name']

class Icon(models.Model):
    """
    Stores icons that can be selected for agenda items.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="A unique name for the icon, e.g., 'Conference', 'Dinner'."
    )
    # Storing SVG code directly is flexible. You can also use an ImageField or FileField.
    svg_code = models.TextField(
        help_text="Paste the SVG code or image tag for the icon."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Icon"
        verbose_name_plural = "Icons"
        ordering = ['name']

class InvitationTemplates(models.Model):
    name = models.CharField(max_length=100)
    package_plan = models.ForeignKey(PricingPlan, on_delete=models.SET_NULL, blank=True, null=True)
    #
    open_envelope_button = models.ImageField(upload_to= 'open_envelope_button', null =True, blank=True)
    basic_decoration_photo = models.ImageField(upload_to='basic_decorations_photo', null=True, blank=True)
    basic_backgorund_photo = models.ImageField(upload_to='basic_background_photo', null=True, blank=True)
    # Standard Assets
    standard_cover_video = models.FileField(upload_to='standard_cover_video', null=True, blank=True)
    standard_background_video = models.FileField(upload_to='standard_background_video', null=True, blank=True)

    def __str__(self):
        return self.name
    
class TemplateColor(models.Model):
    invitation_template = models.ForeignKey(InvitationTemplates, on_delete=models.CASCADE, related_name='template_colors')
    hex_color_code = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.invitation_template.name} = {self.hex_color_code}"
    
class TemplateFontName(models.Model):
    invitation_template = models.ForeignKey(InvitationTemplates, on_delete=models.CASCADE, related_name='template_font_name')
    language = models.CharField(max_length=20, default='en', help_text='e.g: kh,en,cn')
    font = models.ForeignKey(CustomFont, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.invitation_template.name} - {self.font.name} ({self.language})"