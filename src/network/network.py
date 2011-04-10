import classes
import display.manager

network = classes.Network()

def get_info_on_node(x, y):
    if network.check_collision(x, y):
        print(' * Node at (%s,%s) has %s goop' % (x, y, network.get_node(x, y).goop))
        for n in network.get_node(x, y).neighbors:
            print(' * Neighbor @ (%s, %s)' % (n.x, n.y))

def balance_nodes():
    network.balance()
