#!/usr/bin/python
import socket
import subprocess
import re

# Configuration
host = "62.173.140.174"
port = 10300
timeout = 10


# Function to run shell commands
def run_command(command):
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, check=True)
        print(f"{result.stdout.strip()}")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return None

# Establish a socket connection
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.settimeout(timeout)
        print("Connection established. Sending start command...")

        # Send start command
        sock.sendall(b"start\r\n")

        # Initialize buffer
        buffer = ""
        hash_count = 0

        # Read and process data
        while True:
            more = sock.recv(4096).decode('utf-8')
            if not more:
                raise Exception("Socket closed by the server")
            buffer += more

            if '>>>' in buffer:
                # Process hashes
                matches = re.findall(r'\(\d+/100\) ([a-f0-9]{32})', buffer)
                for hash_value in matches:
                    print(f"{hash_count}: {hash_value}")
                    command = f"hashcat -m 0 -a 0 -w 4 -O {hash_value} --potfile-disable /usr/share/wordlists/rockyou.txt | grep '{hash_value}:' | cut -d ':' -f 2"
                    result = run_command(command)
                    if result:
                        sock.sendall(f"{result}\r\n".encode('utf-8'))
                    else:
                        print("No result to send for hash.")
                    hash_count += 1

                # Clear buffer after sending responses
                buffer = ""

            # After processing 100 hashes, just wait for any additional data
            if hash_count >= 100:
                print("All hashes processed. Waiting for any additional data...")
                while True:
                    final_data = sock.recv(4096).decode('utf-8')
                    if final_data:
                        print("Additional data received from server:", final_data)
                        break
                    else:
                        print("No additional data received. Ending session.")
                        break

except Exception as e:
    print(f"An error occurred: {e}")