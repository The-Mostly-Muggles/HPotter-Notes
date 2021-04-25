# small test file for basic idea of HPotter dns-request process
from dns import query
import socket

#create a udp socket listening to global ip on p53
listen_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listen_sock.bind (('0.0.0.0', 53))

#receive incomming udp dns query as a tuple (dns.message.Message, time-stamp, source address tuple: (ip, port))
message = query.receive_udp(listen_sock)
print (message)

# ...
# spawn bindd container and create a connection to it
# ...

#172.17.0.2= example ip for bindd:latest container
#redirect the query to a onewaythread going from HPotter to the dns 
reply = query.udp(message[0], '172.17.0.2', port=53)
print(reply)
