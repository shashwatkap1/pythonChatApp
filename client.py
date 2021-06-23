from socket import *
from tkinter import *
from tkinter import messagebox
root = Tk()
txt = Text(root)
txt.grid( columnspan=3)
sent = StringVar()


root.title("CLIENT")
root.resizable(width=FALSE, height=FALSE)
port = 9020
client_socket = socket()
client_socket.connect(('localhost', port))

e = Entry(root, width=100, textvariable=sent)
e.grid(row=1, column=0)
print('Connected to server')

x=0
flag=0
y =0

def send_msg():
    global flag
    if(flag==0):
         sent=e.get()
         global x,y
         if(sent=="exit"):
           stop_server()
         else:   
            display= Label(root, text="You: "+sent).grid(sticky=NE)
            client_socket.send(sent.encode())
            e.delete(0,'end')
            x=x+1
        
            y=0
            receive_msg()

         
def receive_msg():
    
    global flag
    if(flag==0):
        data = client_socket.recv(1024).decode()
        if(data==''):
         return
        if(not data):
            stop_server()
        else:
            global x,y
            message = Label(root, text="Shashwat: " +data).grid( sticky=NW)
        
            x+=1
        
            y=6
send = Button(root, text="Send", command=send_msg).grid(row=1,column=2)   
def stop_server():
    global flag
    client_socket.close()
    messagebox.showerror("Error", "Shashwat left the chat")   
    flag=1 
    print("Disconnected from server")          
 
        
receive_msg()
root.mainloop()




        
        
       
