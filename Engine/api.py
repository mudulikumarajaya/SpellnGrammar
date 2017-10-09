from rest_framework.views import APIView
from django.http import HttpResponse
import json
from rest_framework.views import APIView
from django.http import HttpResponse
from .Engine import Engine

class SpellnGrammarAPI(APIView):

    def post(self, request, *args, **kw):
        print("Post method")
        result = Engine.PredicationEngine(request)
        print("Result=",result)
        result = json.dumps(result)
        print("result1:",result)
        return HttpResponse(result)

