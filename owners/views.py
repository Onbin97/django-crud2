import email
import json

from django.http import JsonResponse
from django.views import View

from owners.models import *

class Ownersregister(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name    = data["name"],
            email   = data["email"],
            age     = data["age"],
        )
        return JsonResponse({"message" : "success"}, status = 201)

class Dogsregister(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.get(name = data["owner_name"])
        Dog.objects.create(
            name    = data["name"],
            age     =  data["age"],
            owner   = owner

        )
        return JsonResponse({"message" : "dog_created"}, status=201)

    
    
        
