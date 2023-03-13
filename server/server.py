import zmq.auth
from zmq.auth.thread import ThreadAuthenticator
from pathlib import Path
from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()

# Navigate to the clients directory
clients_dir = current_dir / "server" / "clients"

# Navigate to the cert directory
cert_dir = current_dir / "server" / "cert"

# Navigate to the server.key_secret file in the cert directory
key_file_path = cert_dir / "server.key_secret"

class SecureMessagingSystem:
    def __init__(self):
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.ROUTER)
        self.socket.bind("tcp://*:5555")
        
        self.authenticator = ThreadAuthenticator(self.context)
        self.authenticator.start()
        self.authenticator.allow("127.0.0.1")
        self.authenticator.configure_curve(domain="*", location=str(clients_dir))
        self.curve_secretkey, self.curve_publickey = zmq.auth.load_certificate(str(key_file_path))
        self.authenticator.curve_server = True

    def start(self):
        while True:
            message = self.socket.recv_multipart()
            identity, payload = message[0], message[1:]
            print(f"Received request from {identity}: {payload}")
            response = [identity, b"Hello, client!"]
            self.socket.send_multipart(response)

