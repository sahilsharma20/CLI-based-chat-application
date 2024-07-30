import socket

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Target IP and port
target_ip = "127.0.0.1"
target_port = 2525
target_address = (target_ip, target_port)
condition = True

while condition:
    message = input("Please enter your message: ")
    message_encrypted = message.encode('ascii')

    # Send the message to the target address
    s.sendto(message_encrypted, target_address)
    print("Your message is successfully sent to the receiver")

    # Receive acknowledgment from receiver
    data, address = s.recvfrom(1024)
    acknowledgement = data.decode('ascii')
    print(f"Your message is received: {acknowledgement}")

    # Check if the user wants to quit the program
    permission = input("Do you want to quit this program? Press Y/N: ")

    if permission.lower() == "y":
        condition = False
