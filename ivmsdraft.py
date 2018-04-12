import tkinter as tk
from tkinter import ttk # ttk is to improve looks
from tkinter import messagebox, Menu
import create_tool_tip as tt
import widget_file as wf
import time

cg_font=('century gothic', 18)#
cg_font2=('century gothic', 27, 'italic')#
cg_font3=('century gothic', 10)

class Password:
    def __init__(self, master):
        self.win=master
        self.win.title('I.V.M.S')
        self.win.geometry('240x240')
        self.win.resizable(0,0)
        #self.win.iconbitmap(r'favicon.ico')

        self.createWidgets()#object directly cereates widgets

    def show_frame(self, cont):
            frame= self.frames[cont]
            frame.tkraise()

    

    def createWidgets(self):

        monty=ttk.Frame(self.win)
        monty.pack_propagate(0)
        monty.pack(fill=tk.BOTH, expand=1)
        #monty.grid(column=0, row=0, padx=8, pady=4)

        label=ttk.Label(monty, text="User Login", font=cg_font2)#.grid(column=0, row=0, sticky='W', padx=8, pady=4)
        label.place(relx=0.5, rely=0.10, anchor='center')
        ttk.Label(monty, text='Enter User ID:',font=cg_font).place(relx=0.5, rely=0.30, anchor='center')#.grid(column=0, row=1, sticky='W', padx=8, pady=4)
        #label.pack()
        self.uname=tk.StringVar()
        entry1= ttk.Entry(monty,width=20,textvariable=self.uname)
        entry1.place(relx=0.5, rely=0.43, anchor='center')
        entry1.focus()# set cursor in entry widget
        #entry1.grid(column=0, row=2,sticky='W', padx=8, pady=4)
        tt.createToolTip(entry1, 'Enter User ID')

        ttk.Label(monty, text='Enter Password:',font=cg_font).place(relx=0.5, rely=0.58, anchor='center')

        self.pass_word=tk.StringVar()
        entry2= ttk.Entry(monty,width=20, textvariable=self.pass_word, show='*')
        entry2.place(relx=0.5, rely=0.71, anchor='center')
        entry2.focus()# set cursor in entry widget
        #entry2.grid(column=0, row=4,sticky='W', padx=8, pady=4)
        tt.createToolTip(entry2, 'Enter Password')

        def login(uname, pass_word):
            pass_dict={'shivam':'ascaban'}
            u=uname.get()
            p=pass_word.get()
            if(pass_dict[u]==p):
                #self.show_frame(Password)
                #messagebox.showinfo("Message", "Right Password")
                obj=wf.widgets()
                obj.createWidgets2()
                entry1.delete(0,'end')
                entry2.delete(0,'end')
                #self.win.quit()
                
                self.win.destroy()
                #time.sleep(10)
                #obj.createWidgets2()
                #exit()
                
            else:
                messagebox.showerror("Error", "Wrong Password")
        #btntot=ttk.Button(monty, fg='black', font=cg_font3, text='Login', bg='powder blue', ccommand=lambda:login(self.uname, self.pass_word)).grid(row=6,column=1)
        action=ttk.Button(monty, text="Log in", width=20, command=lambda:login(self.uname, self.pass_word))
        action.place(relx=0.5, rely=0.87, anchor='center')
        #action.grid(column=0, row=5,sticky='W', padx=8, pady=4)
        
root=tk.Tk()
x=Password(root)
#x.win.mainloop()
root.mainloop()

