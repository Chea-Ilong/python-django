# Generated by Django 5.2.4 on 2025-07-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_invitationtemplates_templatecolor_templatefontname'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitationtemplates',
            name='open_envelope_button',
            field=models.ImageField(blank=True, null=True, upload_to='open_envelope_button'),
        ),
    ]
