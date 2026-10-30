# Program Name: Assignment3.py
# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Komi Sowu
# Assignment Number: Lab 3
# Due Date: 10/10/2026
# Purpose: Ask the user to enter a string, send it to Program B, receive the uppercase response, and print it.

import socket

# Create a TCP socket using IPv4.
s = socket.socket(
  socket.AF_INET, 
  socket.SOCK_STREAM
)

# Connect to Program B on the same computer.
s.connect(("127.0.0.1", 45566))

# Ask the user for a string and send it to Program B.
message = input("Enter a string: ")
s.sendall(message.encode("utf-8"))

# Receive the uppercase response and display it.
response = s.recv(4096).decode("utf-8")
print("Response from Program B:", response)

# Close the connection.
s.close()
