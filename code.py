import socket
import sys
from datetime import datetime
from time import strftime

target =input("Enter the host to SCAN: ")
host = socket.gethostbyname(target) #Gets host's IP

file = open("Port_Scanner.txt","w")

initial_time= datetime.now()
print("Start Time: {}".format(initial_time.strftime("%H:%M:%S")))
file.write("Start Time: {}\n".format(initial_time.strftime("%H:%M:%S")))
try:
    for port in range(1,1025):
        sock = socket.socket()
        sock.settimeout(0.1)
        result = sock.connect_ex((host,port))
        if result==0:
            try:
                print("Port no. {} Open Protocol {}".format(port,socket.getservbyport(port,"tcp")))
                file.write("Port no. {} Open Protocol {}\n".format(port,socket.getservbyport(port,"tcp")))
            except Exception as e:
                print("Port no. {} Open Protocol {}".format(port, "Unknown"))
                file.write("Port no. {} Open Protocol {}\n".format(port, "Unknown"))
        # else:
        #     print("Port no. {} closed".format(port))

except socket.gaierror:
    print("Hostname could not be resolved")
    file.write("Hostname could not be resolved")

except socket.error:
    print("Could not connet to Server...Exiting")
    file.write("Could not connet to Server...Exiting")

    sys.exit()


final_time = datetime.now()
print("End Time: {}".format(final_time.strftime("%H:%M:%S")))
file.write("End Time: {}\n".format(final_time.strftime("%H:%M:%S")))

total_time = final_time-initial_time
print("Total time is {}".format(total_time))
file.write("Total time is {}\n".format(total_time))
