from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import LevelReading
from .serializers import LevelReadingSerializer


# Create your views here.

@api_view(['GET'])
def get_latest(request):
    readings = LevelReading.objects.all()

    if not readings:
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        latest_reading = readings.order_by("-id")[0]
        serializer = LevelReadingSerializer(latest_reading)
        return Response(serializer.data)

