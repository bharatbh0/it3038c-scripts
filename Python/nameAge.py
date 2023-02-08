import socket

hosts = ['www.uc.edu', 'www.google.com', 'www.bing.com']

for h in hosts:
	print(socket.gethostbyname(h))

print('Working from hosts: " + socket.getfqdn())

for h in hosts:
	print(h + ': ' + socket.gethostbyname(h))