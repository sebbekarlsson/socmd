from socmd.constants import MSGLEN
from threading import Thread
import json
import importlib


'''
Holds a clients connection
'''


class MainframeConnection(Thread):

    def __init__(self, socket, mainframe, commands_dir):
        Thread.__init__(self)
        self.socket = socket
        self.mainframe = mainframe
        self.commands_dir = commands_dir
        self.username = None
        self.channel = None

    def run(self):
        while True:
            incoming = self.socket.recv(MSGLEN)

            try:
                data = json.loads(incoming)
            except ValueError:
                self.socket.close()
                self.socket = None

                if self.channel and self.username:
                    self.mainframe.broadcast(json.dumps({
                        'channel': self.channel,
                        'username': self.username,
                        'message': '<leave>{}</leave>'
                        .format(self.username),
                        'notice': True
                    }))

                return False

            if 'command' in data:
                try:
                    module = importlib.import_module(
                        self.commands_dir + '.' + data['command']
                    )
                except ImportError:
                    self.socket.send(json.dumps({
                        'message': 'no such command'
                    }))
                    continue

                resp = module.run()

                self.socket.send(json.dumps({
                    'message': resp
                }))

                continue

            self.mainframe.broadcast(json.dumps(data))
