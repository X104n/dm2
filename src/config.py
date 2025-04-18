"""Configuration file"""
from TUI import choose_from_list
import socket

IP_ADDRESSES = [
    "10.0.3.4",
    "10.0.3.5",
    "10.0.3.6",
    "10.0.3.7",
    "localhost"
]

GATEWAYS = [
    "discover", # Use this to discover data products in the data mesh domain 
    "control", # Use this to control the data product such as start, stop, restart
    "observe", # Use this to observe like the healt and status of the data product (may not need this)
    "consume", # Use this to consume the data product (read only)
    "ingest" # Use this to ingest data into the data product (write only)
]

def ip_setup():
    chosen_ip = choose_from_list("Choose an IP address:", IP_ADDRESSES)
    ip = IP_ADDRESSES[chosen_ip]
    return ip

def socket_setup():
    host = ip_setup()
    port = 9000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(10)
    print(f"Listening on {host}:{port}")
    return sock