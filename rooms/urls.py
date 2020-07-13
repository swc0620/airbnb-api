from rest_framework.routers import DefaultRouter
from django.urls import path
from . import viewsets
# from . import views

router = DefaultRouter()
router.register("", viewsets.RoomViewSet, basename="room")

app_name = "rooms"

urlpatterns = router.urls

# urlpatterns = [
    # path("list/", views.list_rooms, name="list"),

    # path("list/", views.ListRoomsView.as_view()),
    # path("<int:pk>/", views.SeeRoomView.as_view()),
# ]
