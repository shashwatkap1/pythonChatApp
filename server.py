from socket import *
from tkinter import *
from tkinter import messagebox
root = Tk()
txt = Text(root)
txt.grid( columnspan=3)
sent = StringVar()


root.title("Server")
root.resizable(width=FALSE, height=FALSE)

port = 9020
server_socket = socket()
server_socket.bind(('localhost', port))

server_socket.listen()
e = Entry(root, width=100, textvariable=sent)
e.grid(row=1, column=0)
print('Server running')
conn, address = server_socket.accept()


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
            conn.send(sent.encode())
            e.delete(0,'end')
            x=x+1
        
            y=0
            receive_msg()
            
        
def receive_msg():
    global flag
    if(flag==0):
        data = conn.recv(1024).decode()
        if(not data):
            stop_server()
        else:
            global x,y
            message = Label(root, text="Simran: " +data).grid(sticky=NW)
        
            x+=1
        
            y=6
        
send = Button(root, text="Send", command=send_msg).grid(row=1,column=2)   
def stop_server():
    global flag
    conn.close()
    messagebox.showerror("Error", "Simran left the chat")   
    print("Server closed")

    flag=1           
 

    
root.mainloop()



