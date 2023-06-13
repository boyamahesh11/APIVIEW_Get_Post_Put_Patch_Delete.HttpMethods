from django.shortcuts import render

from app.models import *
from app.serializers import *
from rest_framework.response import Response
#from rest_framework.decorators import api_view,permission_classes
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.

#@permission_classes([IsAuthenticated])
class ProductCrud(APIView):
    def get(self,request,id):
        pqs=Product.objects.all()
        pjd=ProductSerializers(pqs,many=True)
        return Response(pjd.data)

    def post(self,request,id):
        pmsd=ProductSerializers(data=request.data)
        if pmsd.is_valid():
            pmsd.save()
            return Response({'messege':'Product is created'})
        else:
            return Response({'failed':'Product is not created'})
            
    def put(self,request,id):
        id=request.data['id']
        po=Product.objects.get(id=id)
        upo=ProductSerializers(po,data=request.data)
        if upo.is_valid():
            upo.save()
            return Response({'messege':'product is updated'})
        return Response({'Failed':'product is not updated'})

    def patch(self,request,id):
        id=request.data['id']
        po=Product.objects.get(id=id)
        po.Pname=request.data['Pname']
        po.save()
        return Response({'sucess':'data is partially update'})


    def delete(self,request,id):
        Product.objects.get(id=id).delete()
        return Response({'Sucess':'Product is deleted'})