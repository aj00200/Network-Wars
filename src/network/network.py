import classes
import display.manager

network = classes.Network()
nodes = []
nodes.append(classes.Producer(0,0))
nodes.append(classes.Node(1,0))
nodes[0].add_neighbor(nodes[1])
nodes[1].add_neighbor(nodes[0])
for node in nodes:
    network.add_node(node)
    display.manager.draw_node(node)

def get_info_on_node(x, y):
    for node in nodes:
        if network.check_collision(x, y):
            print(' * Node at (%s,%s) has %s goop' % (x, y, network.get_node(x, y).goop))

def balance_nodes():
    for node in nodes:
        node.balance()
