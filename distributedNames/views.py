from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from distributedNames import serializers
from distributedNames.models import Name
from distributedNames.models import Node
from distributedNames.serializers import NameSerializer
from distributedNames.serializers import NodeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .forms import NameForm


def index(request):
    return HttpResponse("hey guys")


def add(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            serializer = NameSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            return HttpResponseRedirect('/')

    else:
        form = NameForm()

    return render(request, 'templates/register.html', {'form': form})


@csrf_exempt
def name_list(request):
    if request.method == 'GET':
        names = Name.objects.all()
        serializer = NameSerializer(names, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NameSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)


@csrf_exempt
def node_list(request):
    if request.method == 'GET':
        nodes = Node.objects.all()
        serializer = NodeSerializer(nodes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NodeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.error, status=400)
