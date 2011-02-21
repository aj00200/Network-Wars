class Node():
    '''A Basic Network Node'''
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
        self.goop -= 2
        node.goop += 2

    def get_goop_levels(self):
        '''Return the current ammount of goop'''
        return self.goop

    def add_neighbor(self, node):
        '''Add a node to the neighbors list'''
        self.neighbors.append(node)

class Producer(Node):
    '''A network node that produces goop'''
    def balance(self):
        self.goop += 5
        Node.balance(self)
