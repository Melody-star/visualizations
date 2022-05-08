from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods

from .models import PersonNum
from .models import Classroom
from .models import News
from .models import IotEquipment
from .models import ControlPass
from .models import CarSystem
import json
from django.http import JsonResponse

@require_http_methods(["GET"])
def personnum(request):
    response={}
    try:
        new_data = PersonNum.objects.filter()
        response['list'] = json.loads(serializers.serialize("json",new_data))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def classroom(request):
    response={}
    try:
        new_data = Classroom.objects.filter()
        response['list'] = json.loads(serializers.serialize("json",new_data))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def news(request):
    response = {}
    try:
        new_data = News.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", new_data))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def iotequipment(request):
    response = {}
    try:
        new_data = IotEquipment.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", new_data))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
         response['msg'] = str(e)
         response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def controlsystem(request):
    response = {}
    try:
        new_data = CarSystem.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", new_data))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)








