from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

#--------------------------------------api----------------------------------------------------
import serial
import json

class Synchronize(APIView):

    def get(self,request):
        print(request.data)
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
        ser.write(b"syn\n")
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                break

        JSON=json.loads(line)

        url="http://127.0.0.1:8000/product_list/"
        token='7b45fd9cbbc8341c8ccec7258d8e42d1311845b0'
        my_headers={"Authorization":"Token "+token}
        my_data={}
        # r=requests.post(url,headers=my_headers,data=my_data)
        r=requests.get(url)
        return 'get'

class SetPrice(APIView):

    def get(self,request):
        print(request.data)
        return 'get'

class SetStock(APIView):

    def get(self,request):
        print(request.data)
        return 'get'

class Rest(APIView):

    def get(self,request):
        print(request.data)
        return 'get'

class Start(APIView):

    def get (self,request):
        print(request.data)
        return 'get'