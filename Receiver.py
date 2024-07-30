import socket
from datetime import datetime

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP address and port
ip_address = "127.0.0.1"
port_no = 2525
complete_address = (ip_address, port_no)

# Bind the socket to the address
s.bind(complete_address)

while True:
    # Receive data from the socket
    data, sender_address = s.recvfrom(100)
    message = data.decode('ascii')
    sender_ip_address = sender_address[0]

    # Open a file to write the message
    with open(f"{sender_ip_address}.txt", "a") as f:
        sender_port_number = sender_address[1]
        current_date_and_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_with_date_and_time = f"Your current date and time is: {current_date_and_time} : Your message is: {message}\n"

        f.write(message_with_date_and_time)

    # Print the message
    print(message)

    # # Send a response back to the sender
    s.sendto(b"Thank you for your message !!", sender_address)
