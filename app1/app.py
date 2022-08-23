from cProfile import run
import socket
from flask import Flask

app = Flask(__name__)



@app.route("/")
def hello_world():
    return IPAddr
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
     
# flask run --port=80

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)     
print("Your Computer IP Address is:" + IPAddr) 

