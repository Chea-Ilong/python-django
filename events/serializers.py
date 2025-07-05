from rest_framework import serializers
from authentications.models import User
from authentications.serializers import UserSerializer
from .models import Events, EventSponsor, EventPhoto

class EventSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSponsor 
        fields = '__all__'

class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    admin = serializers.StringRelatedField(read_only=True)
    team_members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    event_sponsors = EventSponsorSerializer(many=True, read_only=True)
    event_photos = EventPhotoSerializer(many=True, read_only=True)
    # visit_count = serializers.ReadOnlyField()
    # count_guests_not_coming = serializers.ReadOnlyField()
    # count_comments = serializers.ReadOnlyField()
    # count_reviews = serializers.ReadOnlyField()

    class Meta:
        model = Events
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['admin'] = user
        return super().create(validated_data)