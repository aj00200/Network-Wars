'''Chat interface for Network Wars'''
import irc

# Lobby Functions
def get_messages():
    '''Get all messages from the game channel'''
    return connection.get_messages()
def send_message(message):
    '''Sends a message to a predefined channel'''
    pass
def get_open_games():
    '''Returns a list of nicks who have an open game'''
    pass

# Game Functions
def start_game(nick):
    '''Attempt to connect to nick to start a game'''
    pass

def get_game_messages():
    '''Get all messages from a game'''
    pass

def send_game_message():
    '''Send a message to the other player'''
    pass

def quit_game():
    '''Tell the other player that you quit'''
    pass

def request_ip():
    '''Request the IP and port to estabish a UDP connection'''
