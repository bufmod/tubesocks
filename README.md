# tubesocks

###Websocket examples using cherrypy, ws4py, and webix:

This repository contains various examples of websocket implementations using cherrypy and ws4py.  The static content has
been mostly constructed with Webix and javascript / jquery.
 
The examples have only been tested in python 3.5 and Windows 7.

###Examples:
1. sync:

Run sync/server.py.  Open several browsers pointed to http://127.0.0.1.  Changes made in one session are updated in all 
others.

2.  system_monitor (under construction):

Run system_monitor/server.py as admin.  Open browser to http://127.0.0.1 and see system performance values.  Also 
requires pyspectator.