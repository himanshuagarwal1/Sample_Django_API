import json

from django.views.generic import View
from .models import Client
from techtest.utils import json_response
from .seralizers import ClientSeralizer
from marshmallow import ValidationError

class ClientListView(View):

   def get(self, request, *args, **kwargs):
        
        return json_response(ClientSeralizer().dump(Client.objects.all(), many=True))
   
   def post(self, request, *args, **kwargs):        
     
        try:           
            client = ClientSeralizer().load(request.POST)            
        except ValidationError as e:
            return json_response(e.messages, 400)
        except ValueError as v:
            return json_response(v.messages , 500)
        return json_response(ClientSeralizer().dump(client), 201)

       


class ClientView(View):

    def dispatch(self, request, client_id, *args, **kwargs):
        
        try:
            self.client = Client.objects.get(id=client_id)            
        except Client.DoesNotExist:
            return json_response({"error": "No Client matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.client.id)
        return super(ClientView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):       
        
        return json_response(ClientSeralizer().dump(self.client))
    
    def put(self, request, *args, **kwargs):

        try:
            self.Client = ClientSeralizer().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(ClientSeralizer().dump(self.Client))
        
    def delete(self, request, *args, **kwargs):
        self.client.delete()
        return json_response()

    