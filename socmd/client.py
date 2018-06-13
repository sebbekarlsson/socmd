from socmd.ClientService import ClientService
from socmd.constants import PORT_DEFAULT
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--host', help='Host')
parser.add_argument('--port', help='Port')
args = parser.parse_args()


def run():
    host = args.host if args.host else '127.0.0.1'
    port = int(args.port) if args.port else PORT_DEFAULT

    try:
        client = ClientService(
            host,
            port
        )
        client.setDaemon(True)
        client.start()

        while True:
            client.join(1)

    except KeyboardInterrupt:
        client.killed = True
        client.socket.close()

        return True
