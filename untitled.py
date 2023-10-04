import socket

def get_hostname_IP():
    hostname = input("Enter URL: ")
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')

get_hostname_IP()