from models import Name, Node


class Server:
    userList = []
    nodeList = []

    def __init__(self):
        return

    def add_user(self, user):
        name = Name()
        name.set_name(user)
        self.userList += name

    def add_node(self, _node):
        node = Node()
        node.set_ip(_node)
        self.nodeList += node

    def get_user_list(self):
        return self.userList

    def get_node_list(self):
        return self.nodeList

    def clear_user_list(self):
        self.userList = []

    def clear_node_list(self):
        self.nodeList = []

    @staticmethod
    def get_auth_nodes():
        # List of authority nodes
        return []

