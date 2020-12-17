from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# 1 在视图文件中定一个类  继承View
# 2 在urls中指定视图函数的格式  view.类视图的名字.as_view()
#     注意 默认情况下没有()  需要手动添加()
# 3 在类视图中定义方法  方法的名字要和请求方式一致
#     注意 该方法的参数是self request
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView

from FbvApp.models import Animal


class AnimalView(View):

    def get(self,request):

        # animal = Animal.objects.first()

        animal_list = Animal.objects.all()

        animals = []

        for animal in animal_list:
            animals.append(animal.to_dict())


        data={
            'msg':'get',
            'status':200,
            # 'animal':animal.to_dict()
            # 'animal_list':animal_list
            'animals':animals
        }

        return JsonResponse(data=data)

    def post(self,request):
        data={
            'msg':'post',
            'status':200
        }

        return JsonResponse(data=data)

    def put(self,request):
        data={
            'msg':'put',
            'status':200
        }

        return JsonResponse(data=data)


    def patch(self,request):
        data={
            'msg':'patch',
            'status':200
        }

        return JsonResponse(data=data)


    def delete(self,request):
        data={
            'msg':'delete',
            'status':200
        }

        return JsonResponse(data=data)

# 单纯跳转到一个页面
class AnimalTemplateView(TemplateView):
    # template_name = 'animal3.html'
    pass

# 跳转到一个页面并且传递数据
class AnimalListView(ListView):
    template_name = 'animal4.html'
    # model = Animal
    queryset = Animal.objects.all()


# 跳转到一个页面并且传递一个数据
class AnimalDetailView(DetailView):
    template_name = 'animal5.html'
    # model = Animal
    queryset = Animal.objects.all()