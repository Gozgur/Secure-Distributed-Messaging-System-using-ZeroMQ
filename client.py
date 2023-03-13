import zmq

class ZmqClient:
    def __init__(self, host, port):
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.DEALER)
        self.socket.connect(f"tcp://{host}:{port}")