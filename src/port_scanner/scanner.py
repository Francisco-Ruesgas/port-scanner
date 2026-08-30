import socket

def is_port_open(ip="127.0.0.1", port=None):
    """
    Check if a specific port is open on a given IP address.

    Args:
        ip (str): The IP address to check.
        port (int): The port number to check.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = sock.connect_ex((ip, port))
    sock.close()
    if connected == 0:
        return True
    else:
        return False