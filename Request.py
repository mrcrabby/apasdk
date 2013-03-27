from urllib import urlencode, quote_plus
import base64
import hmac
import hashlib
import time
import requests

class Request(object):
    def __init__(self, conf):
        self.conf = conf
        self.params = { 
                     'Service': 'AWSECommerceService', 
                     'AWSAccessKeyId': conf.access_key_id, 
                     'AssociateTag': 'givemegeekcom-20', 
                     'Timestamp': self.timestamp()
                     }
    
    def sort_parameters(self):
        keys = self.params.keys()
        keys.sort()
        
        return zip(keys, map(self.params.get, keys))
        
    def string_to_sign(self, params):
        return "GET\n" + self.conf.endpoint_url + "\n" + self.conf.endpoint_path + "\n" + urlencode(params)
    
    def sign_string(self, string_to_sign):
        signature = hmac.new(key=self.conf.secret_access_key, msg=string_to_sign, digestmod=hashlib.sha256).digest()
        signature = base64.encodestring(signature).strip()
        
        return quote_plus(signature)
    
    def timestamp(self):
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    
    def request_uri(self):
        sorted_params = self.sort_parameters()
        return "http://%s%s?%s&Signature=%s" % (self.conf.endpoint_url, self.conf.endpoint_path, urlencode(sorted_params), self.sign_string( self.string_to_sign( sorted_params ) ))
    
    def send_request(self):
        self.response = requests.get(self.request_uri())
    
    def get_response(self):
        return self.response