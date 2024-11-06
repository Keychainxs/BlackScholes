from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from mongoengine import connect
from django.contrib.auth.hashers import make_password, check_password
from mongoengine.connection import get_db
import logging
import jwt
import datetime
from .models import TestModel, User, OptionCalculation
from serializers import UserSerializer,OptionCalculationsSerializers






class RegisterView(APIView): 
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid(): 
            
            if User.objects(email = serializer.validated_data['email']):
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            
class LoginView(APIView): 
    def post(self,request): 
        email = request.data.get('email')
        password = request.data.get('password')
        
        user= user.objects(email=email).first()
        if user and check_password(password, user.password): 
            token = jwt.encode({
                'user_id': str(user.id),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }, 'your-secret-key', algorithm='HS256')
            
            return Response({'token': token})

        return Response({'error':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
'''   
class CalculateOptionView(APIView): 
    def post(self,request): 
        serializer = OptionCalculationsSerializers(data = request.data)
        
        if serializer.is_valid(): 
            
            data = serializer.validated_data
           
           # call_price, put_price = calculate_option_price( #yet to build 
                #spot_price=data['spot_price'],
                #strike_price=data['strike_price'],
                #maturity_date=data['maturity_date'],
                #risk_free_rate=data['risk_free_rate'],
                #volatility=data['volatility']
            #)
            
            if 'Authorization' in request.headers:
                try:
                    token = request.headers['Authorization'].split(' ')[1]
                    payload = jwt.decode(token, 'your-secret-key', 
                                      algorithms=['HS256'])
                    user_id = payload['user_id']
                    
                    OptionCalculation(
                        user=user_id,
                        **data,
                        calculated_call_price=call_price,
                        calculated_put_price=put_price
                    ).save()
                except:
                    pass  # Continue without saving if token is invalid
            
            return Response({
                'call_price': call_price,
                'put_price': put_price
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
            
            
    pass
 '''
    
    
class TestModelView(APIView):
    def get(self, request):
        try:
            # Create a test document
            test_doc = TestModel(name="test_document").save()
            
            return Response({
                'status': 'success',
                'message': 'Test document created',
                'id': str(test_doc.id)
            })
            
        except Exception as e:
            logging.error(f"Error creating test document: {e}")
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







class TestMongoConnection(APIView):
    def get(self, request):
        try:
            # Test MongoDB connection
            db = get_db()
            db.command('ping')
            
            return Response({
                'status': 'success',
                'message': 'MongoDB connection is working',
                'database': db.name
            })
            
        except Exception as e:
            logging.error(f"MongoDB connection error: {e}")
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)