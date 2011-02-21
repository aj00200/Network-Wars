import socket
import asyncore
import asynchat
import re
import ssl

connections = {}
class Connection(asynchat.async_chat):
    re001 = re.compile('\.* 001')
    def __init__(self, address, port, use_ssl):
        # Setup Asynchat
        asynchat.async_chat.__init__(self)

        self.data = ''
        self.ssl = use_ssl
        self.__address__ = address
        self.set_terminator('\r\n')

        # Setup Socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if use_ssl:
            try:
                self.ssl_sock = ssl.wrap_socket(self.sock)
                self.ssl_sock.connect((address, port))
                self.set_socket(self.ssl_sock)
            except ssl.SSLError, e:
                print(' * SSL Error')
                raise ssl.SSLError(e)
            except socket.error, e:
                print('There was an error connecting to %s' % address)
                return
        else:
            try:
                self.sock.connect((address, port))
            except socket.error, e:
                print('There was an error connecting to %s' % address)
                return
            self.set_socket(self.sock)

    def handle_error(self):
        raise

    def handle_connect(self):
        print(' * Connected')
        self.push('NICK NW%s\r\nUSER NetWars NW NW :Network Wars\r\n' % (random.randint(0,999999)))

    def get_data(self):
        r = self.data
        self.data = ''
        return r

    def found_terminator(self):
        data = self.get_data()
        command = data.split(' ', 2)[1]
        print('Recv: %s' % data)
        if data[:4] == 'PING':
            self.push('PONG %s\r\n' % data[5:])

        elif command ==  'PRIVMSG':
            nick = data[1:data.find('!')]
            channel = data[data.find('MSG')+4:data.find(' :')]
            if channel == self.channel:
                # Queue the message for read

        elif command ==  'NOTICE':
            nick = data[1:data.find('!')]
            channel = data[data.find('ICE')+4:data.find(' :')]
            if channel == self.channel:
                # Queue the notice for read

        elif command ==  'JOIN':
            nick = data.split('!')[0][1:]
            if nick.find('#') == -1:
                channel = data[data.find(' :#')+2:]
                host = data[data.find('@')+1:data.find(' JOIN ')]
                user1 = data[data.find('!'):data.find('@')]
                user = user1.replace("!", "")
                # Joined a channel, should we part it?

        elif re.search(self.re001, data):
            self.push('JOIN %s\r\n' % self.channel)

    def collect_incoming_data(self, data):
        self.data += data
def connect(address, port = 6667, use_ssl = False):
    '''Connect to an IRC network
    address - The network address of the IRC network
    port - On optional argument that specifies the port to connect on
    ssl - A boolean argument specifying wether or not to use SSL'''
    connections[address] = Connection(address, port, use_ssl)
