#!/bin/python

import SimpleHTTPServer
import SocketServer
PORT = 9998

def do_GET(self):
    self.send_response(200)         
    self.send_header('set-cookie', 'blah')           
    self.send_header('duplicate', 'tyu7778')           
    self.send_header('duplicate', '99999tewq')           
    self.send_header('duplicate', 'xxxxxcc56677')           
    self.send_header('content-length', '0')                     
    self.end_headers()

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Handler.do_GET = do_GET
httpd = SocketServer.TCPServer(("", PORT), Handler)
httpd.serve_forever()
