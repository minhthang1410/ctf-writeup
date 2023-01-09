from flask import Flask, redirect, request, make_response
import socket

app = Flask(__name__)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]

@app.route('/')
def hello_world():
    return 'Hello World from Thắng'

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):    
#     if request.method == 'HEAD':
#         resp = make_response("Foo bar baz")
#         resp.headers['Content-type'] = 'image'
#         return resp
#     else:
#         return redirect("file:///usr/src/app/fl4gg_tetCTF")
    
if __name__ == '__main__':
    app.run(debug=True, port=8000, host=local_ip)