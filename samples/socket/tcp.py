
#!/usr/bin/env python
#-*_ coding:utf-8 -*-

import socket
#Install a socket AF_INET IPv4, AF_INET6 IPv6
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Establish connection
s.connect(('www.sina.com',80))

#send data
s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

#Receive data
buffer=[]
while True:
   # receive 1024k every time
   d=s.recv(1024)
   if d:
       buffer.append(d)
   else:
       break
data=b''.join(buffer)

#Close connection
s.close()

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))


#Write in file
with open('sina.html','wb')as f:
   f.write(html)
