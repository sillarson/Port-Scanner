import socket
import sys

def tcp_scanner(port):
    """
    A scanner that takes a parameter(port). 
    This parameter is the port being scanned.
    """
    #sock is the name of the socket object to connect to ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    pass

if __name__ == '__main__':
    main()