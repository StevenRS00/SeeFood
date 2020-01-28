from google.appengine.ext import ndb

class restaurant(ndb.Model):
    title= ndb.StringProperty(required=True)
    dish= ndb.GenericProperty(required=True)
    res_img= ndb.GenericProperty(required=True)
    dish_title= ndb.StringProperty(required=True)
    foo= ndb.StringProperty(required=True)