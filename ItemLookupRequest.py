from Request import Request
from ItemLookupResponse import ItemLookupResponse
import requests
import xml.etree.ElementTree as etree

class ItemLookupRequest(Request):
    def __init__(self, conf, itemid, idtype, response_group=None, search_index=None):
        super(ItemLookupRequest, self).__init__(conf)
        
        self.params['Operation'] = 'ItemLookup'
        self.params['MerchantId'] = 'All'
        self.params['IdType'] = idtype  
        self.params['ItemId'] = itemid.replace('-', '')
        
        if idtype != 'ASIN' and search_index != None:
            self.params['SearchIndex'] = search_index
        
        if idtype in ['DPCI', 'SKU', 'UPC', 'EAN','ISBN'] and search_index == None:
            raise Exception("You need a search index wih this id type")
        
        if response_group != None:
            self.params['ResponseGroup'] = ','.join(response_group)
            
        self.send_request()
        