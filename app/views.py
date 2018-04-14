from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
from .models import Pat
from .serializers import *
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('This is GET request')
#
#     def post(self, request, *args, **kwargs):
#         return HttpResponse('This is POST request')

# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)

   # logger = logging.getLogger(__name__)
print("helloo Mr. Ajay")
@api_view(['GET', 'POST'])
@csrf_exempt
def Check(request):
    if request.method == 'GET':
        tes = Pat.objects.all()
      #  logger.error("GET DATA SERVER")
        # queryset = self.get_queryset()
        serializer = SnippetSerializer(tes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        #logger.error("POST DATA SERVER")
        # f = open("abc.txt","w+")
        # f.write("Hello World")
        # f.write(print (request.data))
        # f.close()
        #queryset = Pat.objects.all()
        #json_data = JSONParser().parse(request.data)
        student_json = json.loads(request.body.decode("utf-8"))
        serializer = SnippetSerializer(data=student_json)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST'])
@csrf_exempt
def getUser(request):
    if request.method == 'POST':
        user_json = json.loads(request.body.decode("utf-8"))
        user_serializer = UserSerializer(data=user_json)
        print("a")
        if user_serializer.is_valid():
            username = user_serializer.data['emailId']
            password = user_serializer.data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return Response("1")
                return Response("User is not active") 
            return Response("2")       
        else:
             return Response("Invalid serializer")
@api_view(['GET', 'POST'])
@csrf_exempt
def addUser(request):

    if request.method == 'POST':
        user_json = json.loads(request.body.decode("utf-8"))
        user_serializer = UserSerializer(data=user_json)
        if user_serializer.is_valid():
            email = user_serializer.data['emailId']
            password = user_serializer.data['password']
            new_user = User.objects.create_user(username=email, password=password)
            print(new_user)
            new_user.save() 
            return Response("saved to table")
        return Response("Invalid Serializer")
@api_view(['GET', 'POST'])
@csrf_exempt               
def logout1(request):
    logout(request)
    return Response("logged Out successfully")          
    