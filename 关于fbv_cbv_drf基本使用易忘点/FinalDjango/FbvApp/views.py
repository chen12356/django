from django.http import JsonResponse
from django.shortcuts import render



# 查询 是get请求方式
# 添加 是post请求方式
# 修改 是put/patch请求方式
# 删除 是delete请求方式




# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from FbvApp.models import Animal


def findAnimal(request):

    if request.method == 'GET':
        # animal = Animal.objects.last()


        animal_list = Animal.objects.all()


        animals = []

        for animal in animal_list:
            animals.append(animal.to_dict())

        data = {
            'msg':'ok',
            'status':200,
            # 'animal':animal.to_dict()
            'animals':animals
        }


        return JsonResponse(data=data,json_dumps_params={'ensure_ascii':False})

@csrf_exempt
def findAnimal1(request):

    if request.method == 'GET':
        data={
            'msg':'get',
            'status':200
        }
        return JsonResponse(data=data)

    if request.method == 'POST':
        data = {
            'msg': 'post',
            'status': 200
        }
        return JsonResponse(data=data)

    if request.method == 'PUT':
        data = {
            'msg': 'put',
            'status': 200
        }
        return JsonResponse(data=data)

    if request.method == 'PATCH':
        data = {
            'msg': 'patch',
            'status': 200
        }
        return JsonResponse(data=data)


    if request.method == 'DELETE':
        data = {
            'msg': 'delete',
            'status': 200
        }
        return JsonResponse(data=data)


