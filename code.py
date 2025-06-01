import socket
import sys
from datetime import datetime
import argparse


with open("Port_Scanner.txt", "w") as file:
    parser = argparse.ArgumentParser(description="This is a basic Port Scanner")

    parser.add_argument("-s", "--Start", help="Enter the starting port", type=int, default=1)
    parser.add_argument("-e", "--End", help="Enter the ending port", type=int, default=1024)
    parser.add_argument("-t", "--Target", help="Enter the target IP/URL", required=True)
    args = parser.parse_args()

    try:
        host = socket.gethostbyname(args.Target)  # Get host's IP
    except socket.gaierror:
        print("Hostname could not be resolved.")
        file.write("Hostname could not be resolved.\n")
        sys.exit()

    initial_time = datetime.now()
    print(f"Start Time: {initial_time.strftime('%H:%M:%S')}")
    file.write(f"Start Time: {initial_time.strftime('%H:%M:%S')}\n")

    try:
        for port in range(args.Start, args.End + 1):
            #print(f"Scanning port {port}")
            sock = socket.socket()
            sock.settimeout(1)
            result = sock.connect_ex((host, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except:
                    service = "Unknown"

                print(f"Port {port} is OPEN | Protocol: {service}")
                file.write(f"Port {port} is OPEN | Protocol: {service}\n")

            sock.close()

    except socket.error:
        print("Could not connect to server. Exiting.")
        file.write("Could not connect to server. Exiting.\n")
        sys.exit()

    final_time = datetime.now()
    print(f"End Time: {final_time.strftime('%H:%M:%S')}")
    file.write(f"End Time: {final_time.strftime('%H:%M:%S')}\n")

    total_time = final_time - initial_time
    print(f"Total time taken: {total_time}")
    file.write(f"Total time taken: {total_time}\n")
