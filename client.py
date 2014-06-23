import argparse
import socket
import sys


class Session(object):

    def __init__(self, host, port, size):
        self.host = host
        self.port = port
        self.size = size
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, port))
        self.username = None

    def login(self):
        self.username = raw_input("username: ")
        self.connection.send(self.username)
        response = self.connection.recv(args.size)
        if response == 'logged in':
            print "Logged in as %s" % self.username
        else:
            "error logging in. server response: %s" % response

    def logout(self):
        self.connection.send('logout')
        response = self.connection.recv(args.size)
        if response == 'logged out':
            self.connection.close()
            print "Logged out"
        else:
            print "error logging out. server response: %s" % response


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', type=int, default=5000)
    parser.add_argument('size', nargs='?', type=int, default=1024)
    args = parser.parse_args()
    session = Session(args.host, args.port, args.size)
    session.login()
    session.logout()