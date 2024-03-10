
from marshmallow import validate
from marshmallow import fields
from marshmallow import Schema
from marshmallow.decorators import post_load
from .models import Client

class ClientSeralizer(Schema):
    
    class Meta(object):

        model = Client

    id = fields.Integer()
    name = fields.String()
    contact_number= fields.Integer()
    contact_email= fields.String()
    status= fields.Boolean()

    @post_load
    def update_or_create(self, data, *args, **kwargs):
        
        
        client, _ = Client.objects.update_or_create(
            id=data.pop("id", None), defaults=data
        )
       
        return client