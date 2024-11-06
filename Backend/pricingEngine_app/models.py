from mongoengine import Document, StringField, DateTimeField, EmailField, FloatField,ReferenceField,BooleanField
from django.utils import timezone



class TestModel(Document):
    name = StringField(max_length=200, required=True)
    created_at = DateTimeField(default=timezone.now)

    meta = {
        'collection': 'test_collection'
    }   
        
class User(Document):
    username = StringField(max_length=150, unique=True, required=True)
    email = EmailField(unique=True, required=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=timezone.now)
    is_active = BooleanField(default=True)
    is_verified = BooleanField(default=False)

    meta = {
        'collection': 'users'
    }

class OptionCalculation(Document):
    user = ReferenceField(User)
    spot_price = FloatField(required=True)
    strike_price = FloatField(required=True)
    time_to_maturity = FloatField(required=True)
    risk_free_rate = FloatField(required=True)
    volatility = FloatField(required=True)
    call_price = FloatField()
    put_price = FloatField()
    calculation_date = DateTimeField(default=timezone.now)

    meta = {
        'collection': 'calculations',
    }
    
    
    
''' 
class UserProfile(Document):
    user = ReferenceField(User, unique=True, required=True)
    subscription_type = StringField(
        choices=['FREE', 'PREMIUM', 'PROFESSIONAL'],
        default='FREE'
    )
    last_login_ip = StringField()
    last_login_date = DateTimeField()

    meta = {
        'collection': 'user_profiles'
    }
'''