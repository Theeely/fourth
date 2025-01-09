
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Dennis.models import *
from .serializers import *
from teluskolearn.models import *

@api_view(['GET'])
def getRoute(request):
    routes=[
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serializer=roomsserializer(rooms,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request,pk):
    rooms=Room.objects.get(id=pk) 
    serializer=roomsserializer(rooms,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getItems(request):
    items=Product.objects.all() 
    serializer=itemsserializer(items,many=True,context={'request':request})#
    return Response(serializer.data)