#Використовуючи Python напиши програму яка покаже ім'я твого компютера (COMPUTERNAME, gethostname)
import socket
import os

print(os.environ['COMPUTERNAME'])
print(socket.gethostname())