from rest_framework import serializers
from authentications.models import User
from authentications.serializers import UserSerializer
from .models import Events, EventSponsor, EventPhoto,Host,HostNames,Agenda, AgendaDetail, InvitationText,InvitationSubText,WeddingGiftPaymentMethod
from site_setting.serializers import InvitationTemplatesSerializer 

class WeddingGiftPaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingGiftPaymentMethod
        fields = '__all__'
        
class InvitationSubTextSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = InvitationSubText
        fields = '__all__'
        
class InvitationTextSerializer(serializers.ModelSerializer):
    
    invitation_sub_text = InvitationSubTextSerializer(many=True, read_only=True)
    class Meta: 
            model = InvitationText
            fields = ['language', 'date_text', 'time_text', 'location_text', 'invitation_sub_text']
class HostNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostNames
        fields = '__all__'

class HostSerializer(serializers.ModelSerializer):
    host_names = HostNamesSerializer(many=True, read_only=True)

    class Meta:
        model = Host
        fields = ['id', 'event', 'avatar', 'created_at', 'host_names']
        
class AgendaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaDetail
        fields = '__all__'
        
class AgendaSerializer(serializers.ModelSerializer):
    agenda_detail = AgendaDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Agenda
        fields = ['id', 'event', 'date', 'agenda_detail']


class EventSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSponsor 
        fields = ['id', 'name', 'logo']

class EventPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPhoto
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    admin = serializers.StringRelatedField(read_only=True)
    team_members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Events
        fields = ['id','team_members', 'admin', 'title', 'date','venue_name','category', 'is_publish']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['admin'] = user
        return super().create(validated_data)
    

class EventsDetailSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    team_members = UserSerializer(many=True, read_only=True)
    event_sponsors = EventSponsorSerializer(many=True, read_only=True)
    event_photos = EventPhotoSerializer(many=True, read_only=True)
    host = HostSerializer(many=True, read_only=True)
    agenda = AgendaSerializer(many=True, read_only=True)
    invitation_template = InvitationTemplatesSerializer(read_only=True)
    invitation_texts = InvitationTextSerializer(many=True, read_only=True) 
    wedding_gift_methods = WeddingGiftPaymentMethodSerializer(many=True, read_only=True)
    class Meta:
        model = Events
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['admin'] = user
        return super().create(validated_data)
    


