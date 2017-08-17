from tkinter import *
import ftplib, os
__version__ = '1'
__name__ = 'SA-MP Server CP'
__author__ = 'saidanemongi@gmail.com'
__credits__ = 'Mongi'
__date__ = '15-08-2017'
__license__ = '''
Copyright 2017 Mongi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
server = None
def credit():
    credit_root = Tk()
    credit_root.title('Credits')
    credit_root.minsize(300, 200)
    credit_root.maxsize(300, 200)
    credit_root.configure(background='white')
    f = Frame(credit_root, bg='white')
    f.grid()
    txt = Label(f, text='\n\n\n\tThis application developed by Mongi\n\tRelease Date: 15-08-2017\n\tAll rights reserved.', bg='white')
    txt.grid()
    credit_root.mainloop()
    return 1
def help_():
    help_root = Tk()
    help_root.title('Credits')
    help_root.minsize(450, 200)
    help_root.maxsize(450, 200)
    help_root.configure(background='white')
    f = Frame(help_root, bg='white')
    f.grid()
    txt = Label(f, text="\n\n\n\tThe application will require the FTP Details (User, Password, IP)\n\tyou have to install the .pwn file in your server to work.", bg="white")
    txt.grid()
    help_root.mainloop()
    return 1
def warning(text):
    warn_root = Tk()
    warn_root.title('Warning!')
    warn_root.minsize(300, 200)
    warn_root.maxsize(300, 200)
    warn_root.configure(background='white')
    f = Frame(warn_root, bg='white')
    f.grid()
    txt = Label(f, text='\n\n\n\tError: '+str(text)+'.', bg='white')
    txt.grid()
    warn_root.mainloop()
    return 1
def ban(event, playername):
    f = open("ControlPanel.cfg", "w")
    f.write("BanPlayer="+str(playername))
    f.close()
    server.cwd('/scriptfiles/CPFolder')
    server.storbinary('STOR ControlPanel.cfg', open('ControlPanel.cfg', 'rb'))
    server.cwd('..')
    os.system('del '+str(os.getcwd())+'\ControlPanel.cfg')
    return 1;
def kick(event, playername):
    f = open("ControlPanel.cfg", "w")
    f.write("KickPlayer="+str(playername))
    f.close()
    server.cwd('/scriptfiles/CPFolder')
    server.storbinary('STOR ControlPanel.cfg', open('ControlPanel.cfg', 'rb'))
    server.cwd('..')
    os.system('del '+str(os.getcwd())+'\ControlPanel.cfg')
    return 1
def CP_dialog():
    ban_root = Tk()
    ban_root.title('Ban')
    ban_root.minsize(400, 200)
    ban_root.maxsize(400, 200)
    ban_root.configure(background='white')
    f = Frame(ban_root, bg='white')
    f.grid()
    Label(f, text='\n\n', bg='white').grid(column=0, row=1)
    ban_text_playername = Label(f, text='    User   Name: ', font='Calibri 12 bold', bg='white')
    ban_text_playername.grid(column=0, row=4)
    Label(f, text='   ', bg='white').grid(column=1, row=4)
    ban_entry_playername = Entry(f, bg='white', width=25)
    ban_entry_playername.grid(column=2, row=4)
    Label(f, text='   ', bg='white').grid(column=3, row=4)
    ban_button = Button(f, text='Ban Player', bg='white')
    ban_button.bind('<Button-1>', lambda event: ban(event, ban_entry_playername.get()))
    ban_button.grid(column=4, row=4)
    Label(f, text='\n', bg='white').grid(column=0, row=4)
    kick_text_playername = Label(f, text='    User   Name: ', font='Calibri 12 bold', bg='white')
    kick_text_playername.grid(column=0, row=5)
    Label(f, text='   ', bg='white').grid(column=1, row=5)
    kick_entry_playername = Entry(f, bg='white', width=25)
    kick_entry_playername.grid(column=2, row=5)
    Label(f, text='   ', bg='white').grid(column=3, row=5)
    kick_button = Button(f, text='Kick Player', bg='white')
    kick_button.bind('<Button-1>', lambda event: kick(event, kick_entry_playername.get()))
    kick_button.grid(column=4, row=5)
    ban_root.mainloop()
def connect(event):
    global server
    ip = input_entry_ip.get().replace('\n', '')
    user = input_entry_user.get().replace('\n', '')
    password = input_entry_pass.get().replace('\n', '')
    server = ftplib.FTP()
    server.connect(ip, 21)
    try:
        server.login(user,password)
    except ftplib.error_perm:
        warning("Wrong FTP User or Password")
        root.destroy()
        return 0
    except Exception as e:
        warning("Unexpected Error: "+str(e))
        root.destroy()
        return 0
    root.destroy()
    CP_dialog()
    return 1
root = Tk()
root.title('Server CP')
root.maxsize(380, 500)
root.minsize(380, 500)
root.configure(background='white')
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Help', command=help_)
filemenu.add_separator()
filemenu.add_command(label='Credits', command=credit) 
menubar.add_cascade(label='?', menu=filemenu)
root.config(menu=menubar)
f = Frame(root, bg='white')
f.pack()
Label(f, text='\n\n', bg='white').grid(column=0, row=1)
Label(f, text='\n\n', bg='white').grid(row=2)
input_text_ip = Label(f, text='FTP Host: ', font='Calibri 12 bold', bg='white')
input_text_ip.grid(column=0, row=4)
input_entry_ip = Entry(f, bg='white', width=25)
input_entry_ip.grid(column=1, row=4)
Label(f, text='', bg='white').grid(column=0, row=5)
input_text_user = Label(f, text='User Name: ', font='Calibri 12 bold', bg='white')
input_text_user.grid(column=0, row=6)
input_entry_user = Entry(f, bg='white', width=25)
input_entry_user.grid(column=1, row=6)
Label(f, text='', bg='white').grid(column=0, row=7)
input_text_pass = Label(f, text='Password: ', font='Calibri 12 bold', bg='white')
input_text_pass.grid(column=0, row=8)
input_entry_pass = Entry(f, bg='white', width=25)
input_entry_pass.grid(column=1, row=8)
new_frame = Frame(root, bg='white')
new_frame.pack()
Label(new_frame, text='\n\n', bg='white').grid()
connect_b = Button(new_frame, text='Connect', bg='white')
connect_b.bind('<Button-1>', connect)
connect_b.grid()
root.mainloop()
