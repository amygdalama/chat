import socket


if __name__ == '__main__':
    host = 'localhost'
    port = 5000
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    s.send('hello world')
    data = s.recv(size)
    s.close()
    print data