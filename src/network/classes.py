import libs.matrix
import display.pipes

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
        display.pipes.draw_pipe(self.x, self.y, node.x, node.y)

class Producer(Node):
    '''A network node that produces goop'''
    def balance(self):
        self.goop += 0.0001
        Node.balance(self)

class Network():
    '''Used to create a network of nodes for
    each player inside of the game'''
    def __init__(self):
        self.network = libs.matrix.Matrix(66,50) # 64x48
        #   larger to avoid IndexError when searching nearby
        self.nodes = []

        # Create some starter nodes
        self.add_node(Producer(5, 5))
        self.add_node(Node(7, 5))

    def check_collision(self, x, y):
        '''Check if there is an object on
        the (x,y) point'''
        if self.network[x][y] == 0:
            return False
        else:
            return True

    def balance(self):
        '''Calls the balance method for each
        node inside the network'''
        for node in self.nodes:
            node.balance() 

    def add_node(self, node):
        '''Add the node, node, to the network'''
        if not self.check_collision(node.x, node.y):
            self.network[node.x][node.y] = node
            self.nodes.append(node)
            display.manager.draw_node(node)

            # Find its neighbors
            for neighbor in self.get_neighbors(node.x, node.y):
                node.add_neighbor(neighbor)
                neighbor.add_neighbor(node)

    def get_neighbors(self, x, y):
        '''Return a list of all the nodes which are within 2
        blocks of the search coordinate (but not the one on
        the search cordinate.'''
        neighbors = []
        # 0 is nonexistant node (empty space)
        for xn in range(-2, 3): # Need to go over by 1 for range
            for yn in range(-2, 3):
                if self.get_node(x + xn, y + yn):
                    neighbors.append(self.get_node(x + xn, y + yn))
        neighbors.remove(self.get_node(x, y)) # Remove origional node
        return neighbors
    def get_node(self, x, y):
        return self.network[x][y]
