import libs.matrix

class Node():
    '''A Basic Network Node'''
    max_goop = 100
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.hp = 100
        self.goop = 0
        self.neighbors = []

    def balance(self):
        '''Tell a node to balance itself with the rest
        of the network. Either ask for more goop or
        send some out to neighboring nodes'''
        for node in self.neighbors:
            if (node.get_goop_levels() < self.goop):
                self.send_goop_to(node)
        if (self.goop > self.max_goop):
            self.goop = self.max_goop

    def send_goop_to(self, node):
        '''Send goop to a connected node'''
        self.goop -= 0.001
        node.goop += 0.001

    def get_goop_levels(self):
        '''Return the current ammount of goop'''
        return self.goop

    def add_neighbor(self, node):
        '''Add a node to the neighbors list'''
        self.neighbors.append(node)

class Producer(Node):
    '''A network node that produces goop'''
    def balance(self):
        self.goop += 0.001
        Node.balance(self)

class Network():
    '''Used to create a network of nodes for
    each player inside of the game'''
    def __init__(self):
        self.network = libs.matrix.Matrix(64,48)

    def check_collision(self, x, y):
        '''Check if there is an object on
        the (x,y) point'''
        if self.network[x][y] == 0:
            return False
        else:
            return True

    def update(self):
        '''Calls the balance method for each
        node inside the network'''
        pass

    def add_node(self, node):
        '''Add the node, node, to the network'''
        if not self.check_cossision(node.x, node.y):
            self.network[node.x][node.y] = node
