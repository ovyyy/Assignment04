import socket

domain = socket.gethostname()
IP_address = socket.gethostbyname(domain)

print(f"The IP address of {domain} is {IP_address}.")