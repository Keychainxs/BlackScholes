from rest_framework import serializers



class UserSerializer(serializers.Serializer): 
    username = serializers.CharField(max_length = 100); 
    email = serializers.EmailField(); 
    password = serializers.CharField(write_only = True);
    
        
    



class OptionCalculationsSerializers(serializers.Serializer):
    strike_price = serializers.FloatField()
    spot_price = serializers.FloatField()
    maturing_date = serializers.FloatField()
    Risk_free_rate = serializers.FloatField()
    Volitility = serializers.FloatField()
    
    
    
