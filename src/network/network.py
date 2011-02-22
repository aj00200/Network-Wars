import classes
import thread

network = classes.Network()
nodes = []
nodes.append(classes.Node(0,0))
nodes.append(classes.Node(1,0))
nodes[0].add_neighbor(nodes[1])
nodes[1].add_neighbor(nodes[0])

def get_info_on_node(x, y):
    for node in nodes:
        if (node.x == x) and (node.y == y):
            print(' * Node at (%s,%s) has %s goop' % (x, y, node.goop))

def input_loop():
    while True:
        type = raw_input('Command: ')
        if (type == 'pro'):
            x = input('x: ')
            y = input('y: ')
            tmp = classes.Producer(x, y)
            for node in nodes:
                if (node.x - x < 1) or (node.x -1 > -1):
                    if (node.y - y < 1) or (node.y -y > -1):
                        if (not node.x == x) or (not node.y == y):
                            node.add_neighbor(tmp)
                            tmp.add_neighbor(node)
                            nodes.append(tmp)
        elif (type == 'node'):
            x = input('x: ')
            y = input('y: ')
            tmp = classes.Node(x, y)
            for node in nodes:
                if (node.x - x < 1) or (node.x -1 >-1):
                    if (node.y - y < 1) or (node.y -y > -1):
                        if (not node.x == x) or (not node.y== y):
                            node.add_neighbor(tmp)
                            tmp.add_neighbor(node)
                            nodes.append(tmp)
