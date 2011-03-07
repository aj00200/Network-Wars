import display.manager
import network.network
import network.classes
from math import floor

def handle_click(x, y):
    '''Do something when the user clicks'''
    if True: # Setup a range that specifys the map
        x = int(floor(x/10))
        y = int(floor(y/10))

        if network.network.network.check_collision(x, y):
            network.network.get_info_on_node(x, y)

        else:
            node = network.classes.Node(x, y)
            network.network.network.add_node(node)
            display.manager.draw_node(node)
