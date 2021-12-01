from socket import socket, AF_INET, SOCK_DGRAM
import sys

def udp_with_game(
    HOST="127.0.0.1",
    PORT=8000
):

    s=socket(AF_INET, SOCK_DGRAM)
    s.bind((HOST, PORT))

    try:
        while True:
            msg, adress=s.recvfrom(32)
            print (msg)
    except KeyboardInterrupt:
        print ("close")
        s.close()
        sys.exit