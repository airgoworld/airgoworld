from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateHotelBookingSerializer, GetHotelBookingSerializer
from .models import HotelBooking
from django.shortcuts import get_object_or_404

class CreateHotelBookingView(APIView):
    def post(self, request):
        serialized_data = CreateHotelBookingSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelBookingsView(APIView):
    def post(self, request):
        hotel_bookings = HotelBooking.objects.all()
        serialized_data = GetHotelBookingSerializer(hotel_bookings, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

class HotelBookingDetailsView(APIView):
    def post(self, request, *args, **kwargs):
        hotel_booking_id = kwargs.get('id')
        hotel_booking = get_object_or_404(HotelBooking, id=hotel_booking_id)
        serialized_data = GetHotelBookingSerializer(hotel_booking)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
