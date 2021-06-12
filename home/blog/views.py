from .serializers import Blogserializer
from django.db.models import query
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import  User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Blogmodel

class loginview(APIView):    
    def post(self,request):
        response= {}
        response['status'] = 500
        response['message'] ='something went wrong'
        try:
            data=request.data

            if data.get('username') is None:
                response['message']= 'username not found'
                raise Exception('username not found')

            if data.get('password') is None:
                response['message']='password not found'
                raise Exception('password not found')
           
            check_user=User.objects.filter(username=data.get('username')).first
            if check_user is None:
                response['message']= 'invalid username not found'
                raise Exception('invalid username not found')
            user_log=authenticate(username=data.get('username'),password=data.get('password'))
            if user_log:
               response['status']= 200
               response['message'] ='welcome'

            
            else:
                response['message']= 'invalid password not found'
                raise Exception('invalid password not found')

        except Exception as e:
            print(e) 

        

        return Response(response)          
