from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serialzers import GameSerializer
from .models import Game
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here. 

@csrf_exempt

def game_read(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondat=JSONParser().parse(stream)
        id=pythondat.get('id',None)
        if id is not None:
            game=Game.objects.get(id=id)
            serializer=GameSerializer(game)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        game=Game.objects.all()
        serializer=GameSerializer(game, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt  

def game_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializers=GameSerializer(data=pythondata)
        if serializers.is_valid():
            serializers.save()
            res={'message': 'Data created', "success" : True}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data=JSONRenderer().render(serializers.errors) 
        return HttpResponse(json_data, content_type='application/json')  
    
@csrf_exempt

def game_update(request):
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        game=Game.objects.get(id=id)
        serializers=GameSerializer(game, data=pythondata, partial=True)
        if serializers.is_valid():
            serializers.save()
            res={'mag': 'Data Updated!!'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data=JSONRenderer().render(serializers.errors) 
        return HttpResponse(json_data, content_type='application/json')  

@csrf_exempt
def game_delete(request):
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        game=Game.objects.get(id=id)
        game.delete()
        res={'mag': 'Data deleled ?'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
        #return JSONRenderer(res, safe=False)

@csrf_exempt       
def get_all_games(request):
    if request.method=='GET':
        game=Game.objects.all()
        serializer=GameSerializer(game, many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')




