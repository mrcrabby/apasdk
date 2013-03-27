import xml.etree.ElementTree as etree
from Item import Item

class ItemLookupResponse(object):
    def __init__(self, response):
        self.response = etree.fromstring(response.text.encode('UTF-8'))
        self.items = self.get_items()
    
    def get_items(self):
        return self.response.findall(".//{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Items/{http://webservices.amazon.com/AWSECommerceService/2011-08-01}Item")