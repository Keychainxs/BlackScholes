import numpy as np 
from scipy.stats import num 
from datetime import datetime

from math import sigma, norm
import math 
'''
 strike_price = serializers.FloatField()
    spot_price = serializers.FloatField()
    maturing_date = serializers.FloatField()
    Risk_free_rate = serializers.FloatField()
    Volitility = serializers.FloatField()
    
'''

# create a class to initialize the function for the black Schoels. the arguments for this class should be the from the 'OPtion class we built' 
class BlackSchoels: 
    

    
    def __init__(self, spot_price, maturing_date, Risk_free_rate,Volitility):
        self.S = float(spot_price) 
        self.T = float(maturing_date)
        self.R = float(Risk_free_rate)
        self.K = float(Volitility)
    
    
        
    
    
    
    
    #initialize the stike price, volitility, risk free rate, and volatility

# inside this  class  caluculate the time maturity
        if isinstance(maturing_date, datetime): 
            self.T = (maturing_date  - datetime.now().day)
            
        else: 
            self.T = float(maturing_date)
            
        
        
# calculate D1 and D2 
        D1 = (np.log(self.S/self.K) + (self.R + sigma**2/2)* self.T / (sigma*np.sqrt(self.T)))
        D2 =  D1 - sigma * math.sqrt(self.T)
        
        
        
        

# creata functinon for the call price 
    def calculate_call_price(self,D1,D2): 
        
        call_price = self.S * norm.cdf(D1) - self.K * math.exp(self.R * (-1)  * self.T * norm.cdf(D2))
        
        return max(call_price)
    
    
    # this return the max of the call price 
    
    
#create a functino for the put price 

    def calculate_put_price(self,D2):
        
        put_price = math.exp() * self.k((-1) * self.r * self.T) * norm.cdf((-1)* D2) -self.S * norm.cdfs((-1) * D2)
        
        
    # this should return the max of the put price
        return max(put_price)
    
# create a function for to calculate the greeks 
    def calculate_greeks(self,D1): 
        call_delta = norm.cdf(self.D1)
        put_delta = call_delta - 1

    
        
        gamma = norm.pdf(self.d1) / (self.S * self.sigma * math.sqrt(self.T))

        
        call_theta= (-self.S * norm.pdf(self.d1) * self.sigma / (2 * math.sqrt(self.T)) 
                         - self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(self.d2)) 
        
        put_theta = (-self.S * norm.pdf(self.d1) * self.sigma / (2 * math.sqrt(self.T)) 
                        + self.r * self.K * math.exp(-self.r * self.T) * norm.cdf(-self.d2))
        
        vega = self.S * math.sqrt(self.T) * norm.pdf(self.d1)
        
        call_rho = self.K * self.T * math.exp(-self.r * self.T) * norm.cdf(self.d2)
        put_rho = -self.K * self.T * math.exp(-self.r * self.T) * norm.cdf(-self.d2)

        
        
        return {
            'gamma' : gamma,
            'rho': {'call':call_rho, 'put': put_rho},
            'vega': vega,
            'theta': {'call': call_theta, 'put': put_theta},
            'delta' : {'call' : call_delta, 'put' : put_delta}
        }
        
        
        
        
    # this function should return the gamma,rho,vega,theta, and delta in a dictionary 
    #out of which the delta, vegha, and rho should take a dictionary that has a key of "call and puts" and a value.
            
#create a functino calculate the option price This takes the arguments from the OPtion call class we built 

    def calculate_option_priceself(self,spot_price, maturing_date, Risk_free_rate,Volitility): 
        
        
        
        
    # this should be a  wrapper function 
            bs = BlackSchoels(
                spot_price= spot_price,
                maturing_date= maturing_date,
                Risk_free_rate= Risk_free_rate,
                Volitility= Volitility
            )
    # has a tupple of the class w/ arguments 

    # returns the "call", " puts", and greeks, as a dictionary as key value pairs of eachother.
            call_price = bs.calculate_call_price()
            greek = bs.calculate_call_price()
            put_price = bs.calculate_put_price()

            return ({
                    'greek': greek,
                    'call_price': call_price,
                    'put_price': put_price,
                })
        
    
















