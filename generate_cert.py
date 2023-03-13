import os
import zmq.auth

def generate_keys(domain, location):
    base_dir = os.path.abspath(location)

    # Generate the server keypair
    server_public, server_secret = zmq.auth.create_certificates(location, domain)

    print(f"Generated certificates for {domain} in {base_dir}")
    print(f"Server public key: {server_public}")
    print(f"Server secret key: {server_secret}")

if __name__ == '__main__':
    generate_keys("server", ".")