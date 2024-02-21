from rest_framework import serializers
from .models import Content, ContentRate


class ContentSerializer(serializers.ModelSerializer):
    rates_count = serializers.IntegerField(source='content_rates_count')
    rates_avg = serializers.FloatField(source='content_rates_avg')
    user_rate = serializers.SerializerMethodField()
    
    class Meta:
        model = Content
        fields = '__all__'
        
    
    def get_user_rate(self, obj):
        user = self.context.get('request').user
        content_rates = obj.content_rates
        user_rate = content_rates.filter(user=user)
        if user_rate.exists():
            return user_rate.first().rate
        
        
        
class ContentRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContentRate
        fields = '__all__'
        read_only_fields = ('user',)
        
    
    def create(self, validated_data):
        user = self.context.get('request').user
        content_rate = ContentRate.submit(user=user, **validated_data)
        return content_rate
    