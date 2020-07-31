from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response

class HelloApiView(APIView):

    def get(self,request,format=None):
        an_apiview=['Follwing are the features of rest api',
                 'function are(delete,update,patch)',
                 'Gives you the most control over the logic']

        return Response({"messaage":"Hello","an_apiviw":an_apiview})             
# Create your views here.
