from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions

from blog.permissions import IsAdminUserOrReadOnly
from .serializers import SliderSerializer
from .models import Slider


# Create your views here.

class ShowSlider(APIView):
    permission_classes = (IsAdminUserOrReadOnly,)
    def get(self,request, pk):
        if len(pk) == 0:
            query=Slider.objects.all()
            #print(query)
            serializers=SliderSerializer(query,many=True,context={ 'request' : request})
            #print(serializers.data)
            return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request, pk):
        if len(pk) == 0:
            serializers=SliderSerializer(data=request.data)
            print(request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if len(pk) == 0:
            data={
                'message' : 'you have to set a number as pk'
            }
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        query_set = Slider.objects.all()
        ids = []
        for object in query_set:
            ids.append(object.id)
        if int(pk) not in ids:
            data={
                'message' : 'query match does not exists!'
            }
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        query = Slider.objects.get(pk=pk)
        serializer = SliderSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class AddSlider(APIView):
#     def post(self,request):
#         serializers=SliderSerializer(data=request.data)
#         print(request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

