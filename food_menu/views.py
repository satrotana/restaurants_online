from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import *
from .serializer import *
from django.contrib.auth.models import User

@api_view(['GET'])
def village(request):
    if request.method == 'GET':
        obj = tblvillages.objects.all()
        serializer = VillageSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def villageDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tblvillages.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = VillageSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def district(request):
    if request.method == 'GET':
        obj = tbldistrict.objects.all()
        serializer = DistrictSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def districtDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tbldistrict.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = DistrictSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def communce(request):
    if request.method == 'GET':
        obj = tblcommunce.objects.all()
        serializer = CommunceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def communceDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tblcommunce.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = CommunceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def province(request):
    if request.method == 'GET':
        obj = tblprovince.objects.all()
        serializer = ProvinceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def provinceDetail(request,uniqid):
    if request.method == 'GET':
        try:
            obj = tblprovince.objects.filter(uniqid__startswith=uniqid)
        except:
            pass
        serializer = ProvinceSerializer(obj, many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def supplyer(request):
    if request.method == 'GET':
        obj = tblsupplyer.objects.all()
        serializer = SupplyerSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupplyerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            newObj = tblsupplyer.objects.get(id = serializer.data['id'])
            serializer1 = SupplyerSerializer(newObj)
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def supplyerDetail(request,search):
    try:
        obj = tblsupplyer.objects.get(id = search)
    except tblsupplyer.DoesNotExist:
        return Response(data={'message':'data not found'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = SupplyerSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupplyerDetailSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message':'supplyer successfully updated'})
    elif request.method == 'DELETE':
        obj.delete()
        return Response(data={'message':'supplyer successfully deleted'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def customer(request):
    if request.method == 'GET':
        obj = tblcustomer.objects.all()
        serializer = CustomerSerializer(obj, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            newObj = tblcustomer.objects.get(id = serializer.data['id'])
            serializer1 = CustomerSerializer(newObj)
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def customerDetail(request,id):
    try:
        obj = tblcustomer.objects.get(id = id)
    except tblcustomer.DoesNotExist:
        return Response(data={'message':'data not found'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = CustomerSerializer(obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerDetailSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'message':'customer successfully updated'})
    elif request.method == 'DELETE':
        obj.delete()
        return Response(data={'message':'customer successfully deleted'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

