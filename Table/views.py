from django.http import HttpResponse
from django.template import loader
from Table.models import AuthUser
from Table.models import FlowsRuleset
from Table.models import FlowsFlowcategorycount
from Table.models import FlowsFlow
import json
from django.core import serializers
from django.http import JsonResponse

# from django.core import serializers


def index(request):
    # template = loader.get_template('table/index.html')
    template = loader.get_template('index.html')
    data = AuthUser.objects.all()

    context = {
        'data': data,
    }

    return HttpResponse(template.render(context, request))


def choice(request):
    template = loader.get_template('choice.html')
    model = FlowsRuleset.objects.filter(flow=18)
    ''' data = FlowsFlowcategorycount.objects.raw("SELECT id, result_key,category_name,SUM(count) AS count,"
                                              "MAX(result_name) AS result_name FROM flows_flowcategorycount "
                                              "WHERE (flow_id = 18 AND result_key "
                                              " IN ('division', 'q5', 'district', 'designation', 'q6', 'q9', 'q8', 'q10', 'q7', 'q4'))"
                                              " GROUP BY result_key, category_name")
'''

    data = FlowsFlowcategorycount.objects.filter(flow=18);
    '''for key, value in model.items:
        for e in value:
            query = FlowsFlowcategorycount.objects.raw('select SUM(count) AS "count" from flows_flowcategorycount where category_name=' + e.get('young') + ' and result_key=' + key.get('Adult'))
'''

    myData = {}
    #query = {}
    countResponse = {}


    for element in (model):
        tempData = json.loads(element.rules)
        options = []
        for item in tempData:
            options.append(item['category']['base'])

        myData[element.label] = options

    for item in data:
        tempvar = item.result_name + item.category_name

        if tempvar in countResponse:
            countResponse[tempvar] = countResponse[tempvar] + 1
        else:
            countResponse[tempvar] = 1

    context = {
        'model': myData,
        'data': data,
        'countResponse':countResponse,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(serializers.serialize('json',countResponse),content_type="application/json")


def analyse(request, flow_id):
    template = loader.get_template('analyse.html')
    f = int(flow_id)
    model = FlowsFlowcategorycount.objects.raw('SELECT * FROM flows_flowcategorycount where flow_id=' + str(f))


    countable={}
    temp= {}




    for item in model:
        count = 0
        temp = item.category_name
        for d in temp:
            if item==d:
                count = count+1
                countable = count

    context = {
        'model': model,
        'f': f,
        'temp':temp,
        'countable':countable,

    }


    return HttpResponse(template.render(context, request))


def test(request):
    template = loader.get_template('test.html')
    model = FlowsFlow.objects.all()

    context = {
     'model':model,
    }


    return HttpResponse(template.render(context, request))


def getFormParam(request):
    #template = loader.get_template('getFormParam.html')
    model = FlowsRuleset.objects.filter(flow=request.POST.get('flow'))

    return HttpResponse(serializers.serialize('json',model),content_type="application/json")


def getFormParamChoice(request):

    model = FlowsRuleset.objects.filter(flow=request.POST.get('flow')).filter(label=request.POST.get('question'))

    data = FlowsFlowcategorycount.objects.filter(flow=request.POST.get('flow'));

    myData = {}
    countResponse = {}

    for item in data:
        tempvar = item.result_key + item.category_name
        tempvar = tempvar.lower()
        if tempvar in countResponse:
            countResponse[tempvar] = countResponse[tempvar] + 1
        else:
            countResponse[tempvar] = 1


    for element in (model):
        tempData = json.loads(element.rules)
        options = {}
        for item in tempData:
            tempvar = element.label+item['category']['base']
            tempvar = tempvar.lower()
            if tempvar in countResponse:
                options[item['category']['base']] = countResponse[tempvar]
            else:
                options[item['category']['base']] = 0

        myData[element.label] = options



    context = {
        'model': myData,
        'data': data,
        'countResponse': countResponse,
    }

    s1 = json.dumps(myData)


    return JsonResponse(json.loads(s1))
    # return HttpResponse(serializers.serialize('json',countResponse),content_type="application/json")