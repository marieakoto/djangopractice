from rest_framework import serializers  #imports serializers from django's modules.

from .models import Task  #imports the'task' module from the current package or module.

class TaskSerializer(serializers.ModelSerializer): #initialises a serializer class that inherits from the modelserializer class.
    class Meta:    #Creates a nested class thta provides metadata for the serializer
        model = Task   #Specifies the model the serializer should serialize
        fields = ['id', 'title', 'description', 'created_at']   # specifies the field that should be present in the serialized representation.


