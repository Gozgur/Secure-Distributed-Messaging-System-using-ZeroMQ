import zmq

class ZmqClient:
    def __init__(self, host, port):
        self.context = zmq.Context.instance()
        self.socket = self.context.socket(zmq.DEALER)
        self.socket.connect(f"tcp://{host}:{port}")

    def send_message(self, message):
        self.socket.send(message)
        response = self.socket.recv()
        print("Received response: %s" % response)

    def close(self):
        self.socket.close()
        self.context.term()

if __name__ == '__main__':
    client = ZmqClient("localhost", 5555)
    client.send_message(b"Hello, server!")  