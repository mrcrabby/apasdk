class AmazonItem(object):
    def __init__(self, item):
        self.item = item
        self.ns = "{http://webservices.amazon.com/AWSECommerceService/2011-08-01}"

    def get_title(self):
        title = self.item.find( ".//" +  self.xml_ns( ("ItemAttributes", "Title") ) )
        return title.text
    
    def get_price(self):
        formatted_price = self.item.find( ".//" + self.xml_ns( ("Offers", "Offer", "OfferListing", "Price", "FormattedPrice") ) )
        
        if formatted_price == None:
            formatted_price = self.item.find( ".//" + self.xml_ns( ("Items", "Item", "VariationSummary", "LowestPrice", "FormattedPrice")) )
            if formatted_price == None:
                return ""
           
        return formatted_price.text
    
    def get_feature(self):
        features = self.item.findall(".//" + self.xml_ns( ("ItemAttributes", "Feature") ) )
        
        feature_string = ''
        for feature in features:
            feature_string += feature.text + " "
            
        return feature_string
    
    def get_brand(self):
        brand = self.item.find(".//" + self.xml_ns( ("ItemAttributes", "Brand") ) )
        return brand.text
        
    def get_link(self):
        link = self.item.find(".//" + self.xml_ns( ("DetailPageURL",) ) )
        return link.text
    
    def get_images(self, size):
        image_urls = self.item.findall(".//" + self.xml_ns( (size + 'Image', "URL") ) )
        
        image_url_list = list()
        for image_url in image_urls:
            image_url_list.append(image_url.text)
            
        return image_url_list
    
    def get_small_images(self):
        return self.get_images('Small')
    
    def get_medium_images(self):
        return self.get_images('Medium')
    
    def get_large_images(self):
        return self.get_images('Large')
    
    def xml_ns(self, tags):
        search_str = ''
        for tag in tags:
            search_str += self.ns + tag + "/" 
            
        return search_str