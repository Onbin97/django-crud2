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
    
    def get(self, request):
        owner_lst = Owner.objects.all()
        result = []
        
        for owner in owner_lst:
            dog_result  = []
            dog_lst     = Dog.objects.filter(owner = owner)

            for dog in dog_lst:
                dog_result.append({
                    "dog_id" : dog.id,
                    "dog_name" : dog.name,
                    "dog_age" : dog.age
                })

            result.append({
                "이름"   : owner.name,
                "email" : owner.email,
                "나이"   : owner.age,
                "키우는 강아지" :  dog_result, 
            })
        return JsonResponse ({"result":result}, status = 200)


class Dogsregister(View):
    def post(self, request):
        data    = json.loads(request.body)
        owner   = Owner.objects.get(name = data["owner_name"])
        Dog.objects.create(
            name  = data["name"],
            age   = data["age"],
            owner = owner

        )
        return JsonResponse({"message" : "dog_created"}, status=201)
    
    def get(self, request):
        dog_lst = Dog.objects.all()
        
        dog_result = []
        for dog in dog_lst:
            dog_result.append({
                "이름"     : dog.name,
                "나이"     : dog.age,
                "주인 이름" : Owner.objects.get(id = dog.owner_id).name
            })

        return JsonResponse({"message": dog_result}, status=200)
            

    
    
        
