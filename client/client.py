import zmq
from pathlib import Path
import zmq.auth

# Get the current working directory
current_dir = Path.cwd()

# Navigate to the cert directory
cert_dir = current_dir / "client" / "cert"

# Navigate to the client.key_secret file in the cert directory
key_file_path = cert_dir / "client.key_secret"

# Navigate to the server.key file in the cert directory
server_key_path = cert_dir / "server.key"

class ZmqClient:
    def __init__(self, host, port):
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.DEALER)

        # client_public_key, client_secret_key = zmq.auth.load_certificate(str(key_file_path))
        # self.socket.setsockopt(zmq.CURVE_PUBLICKEY, client_public_key)
        # self.socket.setsockopt(zmq.CURVE_SECRETKEY, client_secret_key)
        # server_key, _ = zmq.auth.load_certificate(server_key_path)
        # self.socket.setsockopt(zmq.CURVE_SERVERKEY, server_key)
        self.socket.connect("tcp://localhost:5555")

    def send_message(self, message):
        while True:
            self.socket.send(message)
            response = self.socket.recv()
            print(response)

    def close(self):
        self.socket.close()
        self.context.term()

if __name__ == '__main__':
    client = ZmqClient(host="localhost", port=5555)    
    client.send_message(b"Hello, server!")  