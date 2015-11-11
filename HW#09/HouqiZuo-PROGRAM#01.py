__author__ = 'Nick'

import psutil
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPHandler(BaseHTTPRequestHandler):
     string = None
     def do_GET(self):
        self.send_response(200)
        self.end_headers()
        #self.wfile.write(b"Hi")
        self.wfile.write(bytes(MyHTTPHandler.string,'utf-8'))
        return

disk = psutil.disk_io_counters()
mem = psutil.virtual_memory()
string = str("Disk read_time = "+str(disk.read_time)+"\nDisk write_time = "+str(disk.write_time)
             +"\nmemory available = "+str(mem.available)+"\nmemory total = "+str(mem.total))
MyHTTPHandler.string = string

server = HTTPServer(("", 8000), MyHTTPHandler)
server.serve_forever()