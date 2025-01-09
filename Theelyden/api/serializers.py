from rest_framework import serializers
from Dennis.models import *
from teluskolearn.models import *



class roomsserializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'
        
class itemsserializer(serializers.ModelSerializer):
    img = serializers.ImageField()
    
    class Meta:
        model=Product
        fields='__all__'
        
    def get_img(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.img.url)
        return obj.img.url