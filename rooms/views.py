from rest_framework.generics import ListAPIView, RetrieveAPIView
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer, BigRoomSerializer

# Class-based Views
class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

# class ListRoomsView(APIView):
#     def get(self, request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms, many=True)
#         return Response(serializer.data)

# Function-based Views
# set api to only allow GET request
# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     # many=True lets serializer to understand 'queryset of rooms' and just a room
#     serialized_rooms = RoomSerializer(rooms, many=True)
#     return Response(data=serialized_rooms.data)

class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
