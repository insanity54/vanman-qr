import logging
import os

logging.basicConfig(level=logging.DEBUG)

# get config

print("env home: %s" % os.environ.get('VANMANHQ_PORT'))
print("env home: %s" % os.environ.get('VANMANHQ_ADDRESS'))

server_address = os.getenv('VANMANHQ_ADDRESS', 'localhost')
server_port = int(os.getenv('VANMANHQ_PORT', 9000))





from socketIO_client import SocketIO

with SocketIO(server_address, server_port) as socketIO:
    "emit to the server"
    socketIO.emit('greets')
    socketIO.wait(seconds=1)

    

