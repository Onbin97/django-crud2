import json

from django.http import JsonResponse
from django.views import View

from books.models import *

class Bookview(View):
    def get(self, request):
        books  = Book.objects.all()
        results = [{
            "1. 제목" : book.title,
            "2. 출간일": book.release_date,
            "3. 가격" : book.price,
            "4. 저자" : [{
                "이름" : author.name,
                "나이" : author.age,
                "학력" : author.Univ
            } for author in book.to_author.all()]
        } for book in books] 
    
        return JsonResponse({"책" : results}, status=200)

class Authorview(View):
    def get (self, request):
        authors = Author.objects.all()
        results = [{
            "1. 이름": author.name,
            "2. 나이": author.age,
            "3. 학력": author.Univ,
            "출간한 책": [{
                "제목" : book.title,
                "출간일": book.release_date,
                "가격" : book.price,
                
            } for book in author.to_book.all()]
        } for author in authors]

        return JsonResponse({"작가" : results}, status=201)
