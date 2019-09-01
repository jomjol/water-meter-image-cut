from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse
import urllib.request
import socketserver

import lib.CutImageClass
import cv2


CutImage = lib.CutImageClass.CutImage()

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global CutImage
        if "/image_tmp/" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'image/jpeg')
            with open('.'+self.path, 'rb') as file: 
                self.wfile.write(file.read()) # Read the file and send the contents 
        if "url=" in self.path:
            url = parse.parse_qs(parse.urlparse(self.path).query)['url'][0]
            urllib.request.urlretrieve(url, './image_tmp/original.jpg')

            result = CutImage.Cut('./image_tmp/original.jpg')

            txt = 'Original: <p><img src=/image_tmp/original.jpg></img><p>'
            txt = txt + 'Rotate: <p><img src=/image_tmp/rot.jpg></img><p>'
            txt = txt + '<p>Aligned Image: <p><img src=/image_tmp/alg.jpg></img><p>'
            txt = txt + 'Digital Counter: <p>'
            for i in range(len(result[1])):
                txt = txt + '<img src=/image_tmp/'+  str(result[1][i][0]) + '.jpg></img>'
            txt = txt + '<p>'
            txt = txt + 'Analog Meter: <p>'
            for i in range(len(result[0])):
                txt += '<img src=/image_tmp/'+  str(result[0][i][0]) + '.jpg></img>'
            txt = txt + '<p>'

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(txt, 'UTF-8'))

PORT = 3000

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()