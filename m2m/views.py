import json
from platform import release

from django.http import JsonResponse
from django.views import View

from m2m.models import *

class Actorview(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(
            first_name = data["first_name"],
            last_name  = data["last_name"],
            date_of_birth = data["date_of_birth"]
        )

        return JsonResponse({"message": "actor_created"}, status=201)

    def get(self, request):
        actors = Actor.objects.all()
        movies = ActorMovie.objects.all()
        
        result = []

        for actor in actors:
            movie_lst = []
            for movie in movies:
                if movie.actor == actor:
                    movie_lst.append({"제목" : movie.movie.title})
                
            result.append({
                "1. 성" : actor.last_name,
                "2. 이름": actor.first_name,
                "3. 출연작" : movie_lst,
 
            })
        
        return JsonResponse({"actors" : result}, status=200)
    
class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(
            title        = data["title"],
            release_date = data["release_date"],
            running_time = data["running_time"],
        )

        return JsonResponse({"message":"movie_created"})

    def get(self, request):
        movies = Movie.objects.all()
        actors = ActorMovie.objects.all()
        result = []

        for movie in movies:
            actor_lst = []
            for actor in actors:
                if actor.movie == movie:
                    actor_lst.append({
                        "이름" : actor.actor.first_name,
                        "성"  : actor.actor.last_name,
                        })
            
            result.append({
                "제목" : movie.title,
                "상영시간" : movie.running_time,
                "출연진 목록" : actor_lst
            })
        
        return JsonResponse({"movies": result}, status = 200)
        

class Actormovieview(View):
    def post(self, request):
        data  = json.loads(request.body)
        actor = Actor.objects.get(first_name=data["first_name"], last_name=data["last_name"])
        movie = Movie.objects.get(title=data["title"])

        ActorMovie.objects.create(actor=actor, movie=movie)

        return JsonResponse({"message":"created"}, status=201)




