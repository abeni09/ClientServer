#Abenezer Kindie
import socket

#Prompt the client for IP
host = input("Enter the IP : ")

#Prompt the client for port
port = input("Enter the port: ")

#Attach to the TCP socket       
mySocket = socket.socket()

#Connects to the socket using the ip and port
mySocket.connect((host,int(port)))

#Prompt the client for message
message = input("Please enter the statement: ")

#Stays in the loop until quited by the client using the 'q' key         
while message != 'q' :

        #Encode the message then sends the message
        mySocket.send(message.encode())

        #Recieve the uppercased message from the server
        data = mySocket.recv(4096)

        #Decode the message recieved and then prints      
        print ('Returned text from the server: ' + data.decode() + "\n")
        print("Type q to quit the program.  ")
                 
        message = input("Please enter the statement: ")

print("Ooops....You quited")

#If out of the ;oop, the socket is closed                 
mySocket.close()
 
