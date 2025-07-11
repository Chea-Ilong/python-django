# Generated by Django 5.2.4 on 2025-07-05 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('site_setting', '0002_invitationtemplates_templatecolor_templatefontname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='events.events')),
            ],
            options={
                'ordering': ['event', 'date'],
                'unique_together': {('event', 'date')},
            },
        ),
        migrations.CreateModel(
            name='AgendaDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='en', help_text='e.g: kh, en, cn', max_length=10)),
                ('agenda_detail', models.CharField(blank=True, max_length=100, null=True)),
                ('time_text', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda_detail', to='events.agenda')),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_setting.icon')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='host_avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='events.events')),
            ],
        ),
        migrations.CreateModel(
            name='HostNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='en', max_length=10)),
                ('host_name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_a_name', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_b_name', models.CharField(blank=True, max_length=100, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host_names', to='events.host')),
            ],
        ),
    ]
