from django.shortcuts import render
from rest_framework import viewsets, status

from plant.models import Plant

from plant.serializers import PlantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# class Plantdetails(viewsets.ModelViewSet):
#     queryset=Plant.objects.all()
#     serializer_class = PlantSerializer
@api_view(['GET','POST'])
def plantlist(request):
    if(request.method=="GET"):
        plants=Plant.objects.all()
        p=PlantSerializer(plants,many=True)
        return Response(p.data)
    elif(request.method=="POST"):
        p=PlantSerializer(data=request.data)
        if p.is_valid():
            p.save()
            return Response(p.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def plantdetail(request,pk):
    try:
        plant=Plant.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method=='GET'):
        p=PlantSerializer(plant)
        return Response(p.data)
    elif(request.method=='PUT'):
        p=PlantSerializer(plant,data=request.data)
        if(p.is_valid()):
            p.save()
            return Response(p.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='DELETE'):
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

