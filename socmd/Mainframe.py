from socmd.MainframeConnection import MainframeConnection
from threading import Thread
import socket


'''
Handles incoming connections from clients
'''


class Mainframe(Thread):

    def __init__(self, host, port, commands_dir):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socket = None
        self.killed = False
        self.connections = []
        self.commands_dir = commands_dir

    def broadcast(self, data):
        for connection in self.connections:
            if not connection.socket:
                self.connections.remove(connection)
                continue

            connection.socket.send(data)

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

        c = None

        while not self.killed:
            self.socket.listen(5)
            print('Waiting for connections...')

            c, addr = self.socket.accept()
            print('Got connection from', addr)

            connection = MainframeConnection(
                socket=c,
                mainframe=self,
                commands_dir=self.commands_dir
            )
            connection.setDaemon(True)
            connection.start()
            self.connections.append(connection)

        return True
