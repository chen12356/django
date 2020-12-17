from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from CbvDrfApp.models import Women
from CbvDrfApp.serializers import WomenSerializer


class WomenView(View):


    def get(self,request):

        # women = Women.objects.last()

        womens = Women.objects.all()

        womenserializer = WomenSerializer(womens,many=True)


        data = {
            'msg':'get',
            'status':200,
            'women':womenserializer.data
        }


        return JsonResponse(data=data,json_dumps_params={'ensure_ascii':False})


