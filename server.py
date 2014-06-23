import socket


if __name__ == '__main__':
    host = ''
    port = 5000
    backlog = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)
    while True:
        client, address = s.accept()
        while True:
            data = client.recv(size)
            if data == 'logout':
                client.send('logged out')
                client.close()
            elif data:
                client.send('logged in')