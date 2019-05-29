#Abenezer Kindie
import socket

#The host/ip address is defined
host = "127.0.0.1"

#Prompt the server for port
port = input("please enter the port number: \n")

#Create the TCP socket    
mySocket = socket.socket()

#Bind the created socket with the IP and Port
mySocket.bind((host,int(port)))

#The server is ready
print("The server is listening... ... ... ...")

#The server is listening    
mySocket.listen(1)

#The server accepts client conenction
conn, addr = mySocket.accept()

#Prints the comfirmation of connection with the client
print ("Connection from: " + str(addr))

#Stays in the loop until quited by the client
while 1:

    #Recieve the encoded message entered by the client then encode
    data = conn.recv(4096).decode()

    #checks the message
    if not data:
        break

    #Prints what the client sends for the server
    print ("The client says: " + str(data))

    #Changes the message to uppercase and then encode         
    data = str(data).upper().encode()

    #Prints what the server is sending
    print ("Server sending: " + str(data))

    #sends the message
    conn.send(data)

#prints termination message if quited by the client
print ("Connection from: " + str(addr)+ " treminated...")

#closes the connection
conn.close()

