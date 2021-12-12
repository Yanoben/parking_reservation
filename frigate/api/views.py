from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import Parking_place
from .serializers import BookingsSerializer


@api_view(['GET', 'POST'])
def bookings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            serializer = BookingsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    bookings = Parking_place.objects.all()
    serializer = BookingsSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def bookings_detail(request, park_id):
    booking = get_object_or_404(Parking_place, id=park_id)
    role = request.user.role
    if request.user.is_authenticated:
        if request.method == 'GET':
            serializer = BookingsSerializer(booking)
            return Response(serializer.data)
        if role == 'Manager':
            if request.method == 'PUT' or request.method == 'PATCH':
                serializer = BookingsSerializer(booking,
                                                data=request.data,
                                                partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
            elif request.method == 'DELETE':
                booking.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_403_FORBIDDEN)
