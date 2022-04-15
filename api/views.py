from django.shortcuts import render
from django.http import HttpResponse
from .serializer import ProfileSerializers
from django.views.decorators.csrf import csrf_exempt
from .models import Profile 
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view




@csrf_exempt

def create_profile(request):
    if request.method =="POST":
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer = ProfileSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            print('heloo')
            res ={'msg':'Profile was created'}
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response,content_type='application/json')
        json_response=JSONRenderer().render(serializer.errors)    
        return HttpResponse(json_response,content_type='application/json')

    return render(request,'home.html')