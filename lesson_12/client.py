#Клиент (устанавливает соединение с сервером):
import socket
HOST = '127.0.0.1' # IP-адрес сервера
PORT = 50007 # порт сервера
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# клиент устанавливает соединение с сервером:
s.connect((HOST, PORT))
data = 'Hello world'
# обмен по сети происходит в формате bytes, поэтому строку перед
# передачей ее серверу, преобразуем:
s.send(data.encode('utf-8'))
print('Send[1]: ', data)
# получение данных от сервера:
data = s.recv(1024)
s.close()
print('Received[4]: ', data)
