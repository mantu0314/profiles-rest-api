from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework import filters
from profiles_api import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=['Follwing are the features of rest api',
                 'function are(delete,update,patch)',
                 'Gives you the most control over the logic']

        return Response({"messaage":"Hello","an_apiview":an_apiview})

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            message=serializer.validated_data.get("name")
            msg=f"Hello {message}"
            return Response({"msg":msg})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,

            )
    def put(self,request,pk=None):
        return Response({"metthod","put"})

    def patch(self,request,pk=None):
        return Response({"method","patch"})

    def delete(self,request,pk=None):
        return  Response({"method","delete"})


class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer

    def list(self,request):
        list=['Function perform by viewset(create,delete,update,partial update)',
        'is generally used in database',
        'better than APIVIEW']

        return Response({"message":"hello","list":list})


    def create(self,request):
        """ create the data """
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            message=serializer.validated_data.get('name')
            msg=f'Hello {message}'
            return Response({"mess":msg})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self,request,pk=None):
        """ Getting data from the database """

        return Response({"http_meesage":"get"})

    def update(self,request,pk=None):
        """ Updating the data in the database """

        return Response({"http_message":"PUT"})

    def partial_update(self,request,pk=None):
        """parital update of dataa inside the database"""
        return Response({"http_message":"Patch"})

    def destroy(self,request,pk=None):
        """ deletetion of the data from the databaase """
        return Response({"http_message":"delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('email','name',)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES














# Create your views here.
