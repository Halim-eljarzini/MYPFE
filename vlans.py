import getpass
import sys
import telnetlib
HOST = "10.0.0.1"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
tn.write("conf t\n")
tn.write("int loop 1\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("int loop 2\n")
tn.write("ip address 2.2.2.2 255.255.255.255\n")
tn.write("int loop 3\n")
tn.write("ip address 3.3.3.3 255.255.255.255\n")
tn.write("int loop 4\n")
tn.write("ip address 4.4.4.4 255.255.255.255\n")
tn.write("int loop 5\n")
tn.write("ip address 5.5.5.5 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()

