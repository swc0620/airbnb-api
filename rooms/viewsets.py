from rest_framework import viewsets
from .models import Room
from .serializers import BigRoomSerializer

# viewset will automatically give us the url, so we do not need to assign the urls.
# viewset will also automatically paginate, and also automatically let us handle GET, POST, PUT, DELETE.
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer