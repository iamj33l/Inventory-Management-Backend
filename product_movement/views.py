from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ProductMovement
from .serializers import ProductMovementSerializer, ProductMovementDisplaySerializer


@api_view(['GET'])
def product_movement_list(request):
    movements = ProductMovement.objects.all()
    serializer = ProductMovementDisplaySerializer(movements, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_movement_detail(request, pk):
    try:
        movement = ProductMovement.objects.get(pk=pk)
    except ProductMovement.DoesNotExist:
        return Response({'error': 'Product movement not found'}, status=404)

    serializer = ProductMovementSerializer(movement)
    return Response(serializer.data)

@api_view(['POST'])
def product_movement_create(request):
    serializer = ProductMovementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def product_movement_update(request, pk):
    try:
        movement = ProductMovement.objects.get(pk=pk)
    except ProductMovement.DoesNotExist:
        return Response({'error': 'Product movement not found'}, status=404)

    serializer = ProductMovementSerializer(movement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def product_movement_delete(request, pk):
    try:
        movement = ProductMovement.objects.get(pk=pk)
    except ProductMovement.DoesNotExist:
        return Response({'error': 'Product movement not found'}, status=404)

    movement.delete()
    return Response(status=204)