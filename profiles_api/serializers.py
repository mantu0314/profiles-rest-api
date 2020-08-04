from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializer to test the name function """
    name=serializers.CharField(max_length=10)
