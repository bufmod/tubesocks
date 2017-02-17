import random
import time
from ws4py.client import WebSocketBaseClient
from pyspectator.computer import Computer

update_server = WebSocketBaseClient('ws://127.0.0.1/ws')
update_server.connect()
html_io = {
    0: 'text1',
    1: 'slider1',
    2: 'slider2',
}

for i in range(200000):
    time.sleep(.001)
    update_server.send('{\"id\": \"%s\", \"data\": \"%s\"}' % (html_io[1], Computer().processor.load))
    update_server.send('{\"id\": \"%s\", \"data\": \"%s\"}' % (html_io[2], Computer().processor.temperature))

update_server.close_connection()
