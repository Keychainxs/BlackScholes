from django.urls import path
from .views import TestMongoConnection,TestModelView,RegisterView,LoginView,CalculateOptionView


urlpatterns = [
    path('test-connection/',TestMongoConnection.as_view(), name='test-connection'),
    path('test-model/', TestModelView.as_view(), name='test-model'),
    path('register/',RegisterView.as_view(), name ='register-view'),
    path('login/',LoginView.as_view(), name = 'login-view'),
    path('calculate',CalculateOptionView.as_view(), name = 'calculate-view'),
    
]





