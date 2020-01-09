from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from educationApp.models import Datas
from educationApp.services import NameMatcherService, DataService
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
import json
@csrf_exempt
@require_http_methods(["POST"])
def search(request):
    jsonBody = json.loads(request.body)
    dataService = DataService()
    datas = dataService.getAllIndex(jsonBody['words'])
    render = render_to_string('education_data_list.html',{'datas': datas})
    return HttpResponse(render)

@require_http_methods(["GET"])
def getDatas(request):
    dataService = DataService()
    datas = dataService.getDatas(request.GET['name'])
    render = render_to_string('education_data.html', {'datas': datas.datas})
    return HttpResponse(render)
    #print(type(datas.datas))
    #return HttpResponse(json.dumps(datas.datas, ensure_ascii=False),
    #       content_type="application/json")
    
'''
@require_http_methods(["GET"])    
def test(request):
    list = [{id: 1, 'name': 'Jack1'}, {id: 2, 'name': 'Rose2'}]
    render = render_to_string('education_data_list.html',{'students': list})
    return HttpResponse(render)
'''
