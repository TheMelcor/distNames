from models import Node
import requests
from distributedNames.serializers import NodeSerializer, NameSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import time


class Server:

    def __init__(self):
        return

    @staticmethod
    def get_auth_nodes():
        # List of authority nodes
        return []

    @staticmethod
    def request_nodes(nodelist):
        # r = request.get(nodelist[i] + '/nodes/')
        # for each node in list, run request
        # check response data and add anything that isn't stored in db
        # if any data in db isn't received from another server, check if notFound is true
        # if notFound is true, delete it from db
        # else, set notFound to true
        if nodelist is not None:
            for i in nodelist:
                r = requests.get(nodelist[i] + '/nodes/')
                data = JSONParser().parse(r)
                serializer = NodeSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.error, status=400)

    @staticmethod
    def request_names(nodelist):
        if nodelist is not None:
            for i in nodelist:
                r = requests.get(nodelist[i] + '/list/')
                data = JSONParser().parse(r)
                serializer = NameSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=201)
                return JsonResponse(serializer.error, status=400)

    @staticmethod
    def run():
        n = Server.get_auth_nodes()

        Server.request_nodes(n)
        x = True
        while x:
            nl = Node.objects.all()
            Server.request_nodes(nl)
            Server.request_names(nl)
            time.sleep(600)
