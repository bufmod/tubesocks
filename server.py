import os
import json

import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import WebSocket

CLIENTS = set()
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_CONTROLS = dict(
    slider1=50,
    slider2=100,
    text1=""
)


class Synchronize(WebSocket):
    def __init__(self, *args, **kw):
        WebSocket.__init__(self, *args, **kw)
        CLIENTS.add(self)

    def received_message(self, message):
        if str(message) == 'init':
            for id_, data in HTML_CONTROLS.items():
                payload = '{\"id\": \"%s\", \"data": \"%s\"}' % (id_, data)
                self.send(payload)
        else:
            update = json.loads(str(message))
            HTML_CONTROLS[update['id']] = update['data']
            for connection in CLIENTS:
                if connection != self:
                    connection.send(message)

    def closed(self, code, reason=None):
        CLIENTS.remove(self)


class Root(object):
    def ws(self):
        pass
    ws.exposed = True

WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()
cherrypy.quickstart(
    root=Root(),
    script_name='/',
    config={
        'global': {
            'server.socket_host': '127.0.0.1',
            'server.socket_port': 80
        },
        '/': {
            'tools.staticdir.root': CURRENT_DIR,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'static',
            'tools.staticdir.index': 'index.html'
        },
        '/ws': {
            'tools.websocket.on': True,
            'tools.websocket.handler_cls': Synchronize
        },
    }
)
