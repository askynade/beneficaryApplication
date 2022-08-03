from django.shortcuts import render
from rest_framework import generics
from beneficiaryApplication.serializers import ApplicationSerializer,DistrictSerializer,TalukaSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import *
# Create your views here.


class CreateApplicationAPI(generics.GenericAPIView):
    serializer_class = ApplicationSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
  
            return Response({
                "status":"success",
                "message" : "Successfully Inserted Record.",
                 })
        else:
            # print(serializer)
            # print(serializer.errors)

            return Response({
                "status":"error",
                "message":serializer.errors["non_field_errors"][0]
             
                })





class ApplicationViewSet(ViewSet):
    queryset = Application.objects.all()

    def list(self, request):
        serializer = ApplicationSerializer(self.queryset, many=True)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })

    def retrieve(self, request, pk=None):
        item = get_object_or_404(self.queryset, pk=pk)
        serializer = ApplicationSerializer(item)
        return Response({
                "status":"success",
                "message" : "Successfully Fetched",
                "data":serializer.data
                 })
