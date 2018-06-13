from socmd.Mainframe import Mainframe
from socmd.constants import PORT_DEFAULT
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Host')
parser.add_argument('--port', help='Port')
parser.add_argument('--commands', help='Commands directory')
args = parser.parse_args()


def run():
    host = args.host if args.host else 'localhost'
    port = int(args.port) if args.port else PORT_DEFAULT
    commands_dir = args.commands if args.commands else None

    try:
        mainframe = Mainframe(host, port, commands_dir)
        mainframe.setDaemon(True)
        mainframe.start()

        while True:
            mainframe.join(1)

    except KeyboardInterrupt:
        mainframe.killed = True
        mainframe.socket.close()

        return True
