import zmq.auth
from zmq.auth.thread import ThreadAuthenticator

class SecureMessagingSystem:
    def __init__(self):
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.ROUTER)
        self.socket.bind("tcp://*:5555")
        
        self.authenticator = ThreadAuthenticator(self.context)
        self.authenticator.start()
        self.authenticator.allow("127.0.0.1")
        self.authenticator.configure_curve(domain="*", location='clients')
        self.authenticator.authenticator = self.my_zap_handler