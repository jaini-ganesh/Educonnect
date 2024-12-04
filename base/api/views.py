from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Room
from .serializers import RoomsSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
        'GET api/',
        'GET api/rooms/',
        'GET api/rooms/:id',
    ]
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms=Room.objects.all()
    serializer=RoomsSerializer(rooms,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request,pk):
    rooms=Room.objects.get(id=pk)
    serializer=RoomsSerializer(rooms,many=False)
    return Response(serializer.data)
    