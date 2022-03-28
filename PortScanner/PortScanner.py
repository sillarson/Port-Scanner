import socket
import sys

def tcp_scanner(port):
    """
    A scanner that takes a parameter(port). 
    This parameter is the port being scanned.
    """


    #sock is the name of the socket object to connect to ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    #resolve IP from host name
    try:
        remote_server = input("Enter a remote host to scan: ")
        remote_server_IP = socket.gethostbyname(remote_server)
    except socket.gaierror:
        #if host name not resolved, print error message then exit
        print("Host name couldn't be resolved...")
        sys.exit()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()


    #basic port scanner
    try:
        res = sock.connect_ex((remote_server_IP, port))
        if res == 0:
            print("Port {}: OPEN".format(port))
        sock.close()

    except socket.error:
        #when encountering an error, print error message then exit
        print("Couldn\'t connect to server... ")
        sys.exit()


def main():
    """
    The main class
    """
   


if __name__ == '__main__':
    for port in range(100):
        tcp_scanner(port)