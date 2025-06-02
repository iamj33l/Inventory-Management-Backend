from rest_framework.decorators import api_view
from rest_framework.response import Response

from location.models import Location
from location.serializers import LocationSerializer


@api_view(['GET'])
def location_list(request):

    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def location_detail(request, pk):

    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({'error': 'Location not found'}, status=400)

    serializer = LocationSerializer(location)
    return Response(serializer.data)

@api_view(['POST'])
def location_create(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def location_update(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({'error': 'Location not found'}, status=404)

    serializer = LocationSerializer(location, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def location_delete(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return Response({'error': 'Location not found'}, status=404)

    location.delete()
    return Response(status=204)