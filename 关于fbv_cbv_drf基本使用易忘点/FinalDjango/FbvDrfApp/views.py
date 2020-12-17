from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from FbvDrfApp.models import BathCenter
from FbvDrfApp.serializers import BathCenterSerializer


def findBathCenter(request):


    if request.method == 'GET':

        # bathcenter = BathCenter.objects.first()

        bathcenters = BathCenter.objects.all()

        bathcenterSerializer = BathCenterSerializer(bathcenters,many=True)

        data = {
            'msg':'get',
            'status':200,
            'bathcenter':bathcenterSerializer.data
        }


        return JsonResponse(data=data,json_dumps_params={'ensure_ascii':False})