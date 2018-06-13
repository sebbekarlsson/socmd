from threading import Thread
from socmd.Receiver import Receiver
import socket
import json


class ClientService(Thread):

    def __init__(
        self,
        host,
        port,
        daemon=True
    ):
        Thread.__init__(self)

        self.host = host
        self.port = port
        self.killed = False
        self.receiver = Receiver(self)

    def send_command(self, msg):
        return self.socket.send(json.dumps({
            'command': msg
        }))

    def run(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print('Connected to', self.host)

        self.receiver.setDaemon(True)
        self.receiver.start()

        while not self.killed:
            cli_input = raw_input()
            self.send_command(cli_input)
