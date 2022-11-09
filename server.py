import socket
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 1234))
server.listen(4)
print('Соединение с клиентом')
client_socket, address = server.accept()
data = client_socket.recv(1024).decode('utf-8')
print('Соединение установлено', address[0],':', address[1])
print(data)
answer = 'Hello!'
content = answer.encode('utf-8')
client_socket.send(content)
print('Соединение разорвано')