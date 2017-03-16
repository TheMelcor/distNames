from models import Name, Node
import requests

class Server:

    def __init__(self):
        return

    @staticmethod
    def get_auth_nodes():
        # List of authority nodes
        return []

    def request_nodes(self, nodelist):
        # r = request.get(nodelist[i] + '/nodes/')
        # for each node in list, run request
        # check response data and add anything that isn't stored in db
        # if any data in db isn't received from another server, check if notFound is true
        # if notFound is true, delete it from db
        # else, set notFound to true
        for i in nodelist:
            r = requests.get(nodelist[i] + '/nodes/')


