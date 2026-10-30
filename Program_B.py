# Program Name: Program_B.py
# Course: IT3883/Section W01
# Student Name: Komi Sowu
# Assignment Number: Lab 4
# Due Date: 11/06/2026
# Purpose: Listen for Program A, receive its message, convert it to uppercase, and send it back.


import socket

# Create a TCP socket using IPv4.
s = socket.socket(
  socket.AF_INET, 
  socket.SOCK_STREAM
)

# Bind to the local IP address and port, then listen for Program A.
s.bind(("127.0.0.1", 45566))
s.listen()
print("Program B is waiting to connect...")

# Accept the connection from Program A.
conn, addr = s.accept()

# Receive the string and convert it to uppercase.
message = conn.recv(4096).decode("utf-8")
display_message = message.upper()

# Send the uppercase string back to Program A.
conn.sendall(display_message.encode("utf-8"))

# Close the client connection and the listening socket.
conn.close()
s.close()
