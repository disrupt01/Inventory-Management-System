import tkinter as tk
from tkinter import ttk # ttk is to improve looks
from tkinter import messagebox, Menu
import create_tool_tip as tt

cg_font=('century gothic', 18)#
cg_font2=('century gothic', 27, 'italic')#
cg_font3=('century gothic', 10)
cg_font4=('century gothic', 15)
cg_font5=('century gothic', 14)

class widgets():
    def _quit(self):
        win.quit()
        win.destroy()
        exit()
        
    def createWidgets2(self):

        win=tk.Tk()
        win.title('I.V.M.S')
        win.resizable(0,0)
        win.iconbitmap(r'favicon.ico')
#####################################################################################
        #MENU BAR
        menubar=Menu(win)
        win.config(menu=menubar)

        #save=Menu(menubar, tearoff=0)
        #save.add_command(label='New')
        #save.add_separator()
        #save.add_command(label='Quit', command=self._quit)#, need a command here
        #menubar.add_cascade(label='Quit', menu=save)

        '''_quit=Menu(menubar, tearoff=0)
        _quit.add_command(label='New')
        _quit.add_separator()
        _quit.add_command(label='Exit', command=_quit)
        menubar.add_cascade(label='Quit', menu=_quit)'''

        #2nd to right of first
        helpmenu=Menu(menubar, tearoff=0)
        helpmenu.add_command(label='About')
        menubar.add_cascade(label='Help', menu=helpmenu)
########################################################################################

        #TABS
        tabcontrol=ttk.Notebook(win)
        '''
        one tab to serch
        one tab to enter data
        one tab for spread sheet
        one for Quantity Check
        one for data updation
        '''
        data_entry=ttk.Frame(tabcontrol)
        tabcontrol.add(data_entry, text='Data Entry')

        search=ttk.Frame(tabcontrol) 
        tabcontrol.add(search, text='Search')

        '''quantity_check=ttk.Frame(tabcontrol)
        tabcontrol.add(quantity_check, text='Quantity Check')'''

        #data_updation=ttk.Frame(tabcontrol)
        #tabcontrol.add(data_updation, text='Data Updation')

        spread_sheet=ttk.Frame(tabcontrol) 
        tabcontrol.add(spread_sheet, text='Spread Sheet')

        tabcontrol.pack(expand=1, fill='both')
###################################################################################
################################################################################
        #DATA ENTRY
        #LABEL FRAMES
        monty=ttk.LabelFrame(data_entry, text='DATA ENTRY')
        monty.grid(column=0, row=0, padx=8, pady=4)
        
        #ENTRY 
        #calibri_font
        #0 Product ID
        ttk.Label(monty, text='Enter Product ID:', font=cg_font3).grid(column=0, row=0, sticky='W', padx=8, pady=4)
        name0=tk.StringVar()
        nameEntered0=ttk.Entry(monty, width=24, textvariable=name0)
        nameEntered0.focus()# set cursor in entry widget
        nameEntered0.grid(column=0, row=1,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered0, 'Enter Product ID')

        #1 Enter Product
        ttk.Label(monty, text='Enter Product:', font=cg_font3).grid(column=0, row=2, sticky='W', padx=8, pady=4)
        name1=tk.StringVar()
        nameEntered1=ttk.Entry(monty, width=24, textvariable=name1)
        nameEntered1.focus()# set cursor in entry widget
        nameEntered1.grid(column=0, row=3,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered1, 'Enter Product')

        #2 ENTER BRAND
        ttk.Label(monty, text='Enter Brand:', font=cg_font3).grid(column=1, row=2, sticky='W', padx=8, pady=4) #font=calibri_font)
        name2=tk.StringVar()
        nameEntered2=ttk.Entry(monty, width=24, textvariable=name2)
        nameEntered2.focus()# set cursor in entry widget
        nameEntered2.grid(column=1, row=3,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered2, 'Enter Brand')


        #3 ENTER QUANTITY COMBOBOX
        ttk.Label(monty, text='Enter Quantity:', font=cg_font3).grid(column=2, row=2, sticky='W', padx=8, pady=4)# font=calibri_font)
        number1=tk.StringVar()
        numberChosen1=ttk.Combobox(monty, width=18, textvariable=number1)
        numberChosen1['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
        numberChosen1.grid(column=2, row=3,sticky='W', padx=8, pady=4)
        numberChosen1.current(0)
        tt.createToolTip(numberChosen1, 'Enter Quantity')

        #4 ENTER DATE OF PURCHASE
        ttk.Label(monty, text='Enter Date of Purchase:', font=cg_font3).grid(column=0, row=4, sticky='W', padx=8, pady=4) #font=calibri_font)
        name3=tk.StringVar()
        nameEntered3=ttk.Entry(monty, width=24, textvariable=name3)
        nameEntered3.focus()# set cursor in entry widget
        nameEntered3.grid(column=0, row=5,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered3, 'Enter Date of Purchase')

        #5 COMBOBOX SHELF NUMBER
        ttk.Label(monty, text='Enter Shelf Number:', font=cg_font3).grid(column=0, row=6, sticky='W', padx=8, pady=4)# font=calibri_font)
        number2=tk.StringVar()
        numberChosen2=ttk.Combobox(monty, width=20, textvariable=number2)
        numberChosen2['values']=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
        numberChosen2.grid(column=0, row=7,sticky='W', padx=8, pady=4)
        numberChosen2.current(0)
        tt.createToolTip(numberChosen2, 'Enter Shelf Number')

        #8 ENTER DATE OF ENTRY
        ttk.Label(monty, text='Enter Date of Entry:', font=cg_font3).grid(column=1, row=0, sticky='W', padx=8, pady=4) #font=calibri_font)
        name4=tk.StringVar()
        nameEntered4=ttk.Entry(monty, width=24, textvariable=name4)
        nameEntered4.focus()# set cursor in entry widget
        nameEntered4.grid(column=1, row=1,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered3, 'Enter Date of Entry')




        #6 RADIOBUTTON
        ttk.Label(monty, text='Is Product a Food Item\n or Medicine?', font=cg_font3).grid(column=0, row=8, sticky='W', padx=8, pady=4)# font=calibri_font)
        choice=['Yes', 'No']
        radVar1=tk.IntVar()
        radVar1.set(99)

        '''def radCall():
            radsel=radVar.get()
            if radsel==0: nameEntered4.configure(state='disabled')
            elif radsel==1: nameEntered4.configure(state='enabled')'''

        for col in range(2):
            curRad='rad' + str(col)
            curRad=tk.Radiobutton(monty, text=choice[col], variable=radVar1,
                                  value=col)#, command=radCall)
            curRad.grid(column=col, row=9, sticky=tk.W)
            tt.createToolTip(curRad, "Click for " + choice[col])

        #7
        ttk.Label(monty, text='If Yes,\n Enter Best Before Date:', font=cg_font3).grid(column=2, row=8, sticky='W', padx=8, pady=4) #font=calibri_font)
        name5=tk.StringVar()
        nameEntered5=ttk.Entry(monty, width=24, textvariable=name5)
        nameEntered5.focus()# set cursor in entry widget
        nameEntered5.grid(column=2, row=9,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered4, 'Enter Best Before Date')

        #6 RADIOBUTTON
        ttk.Label(monty, text='Is Product a Glass Item?', font=cg_font3).grid(column=0, row=10, sticky='W', padx=8, pady=4)# font=calibri_font)
        choice=['Yes', 'No']
        radVar2=tk.IntVar()
        radVar2.set(99)

        for col in range(2):
            curRad='rad' + str(col)
            curRad=tk.Radiobutton(monty, text=choice[col], variable=radVar2,
                                  value=col)#, command=radCall)
            curRad.grid(column=col, row=11, sticky=tk.W)
            tt.createToolTip(curRad, "Click for " + choice[col])

        #6 BUTTON
        def clickMe():
            #enter command here
           '''print('{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(name0.get(), name4.get(), name1.get()
                                                  , name2.get(), number1.get(), name3.get(), number2.get(), radVar1.get()
                                                  , radVar2.get()))'''
           with open('ivms.txt', 'a') as f:
               f.write('{0} {1} {2} {3} {4} {5} {6} {7} {8}\n'.format(name0.get(), name4.get(), name1.get(), name2.get(), number1.get(), name3.get(), number2.get(), radVar1.get() , radVar2.get()))  
           nameEntered0.delete(0,'end')#clear all data in enteries on click
           nameEntered1.delete(0,'end')
           nameEntered2.delete(0,'end')
           nameEntered3.delete(0,'end')
           nameEntered4.delete(0,'end')
           #nameEntered5.delete(0,'end')
           numberChosen1.delete(0,'end')
           numberChosen2.delete(0,'end')
           #curRad.delete(0,'end')
           #curRad1.delete(0,'end')
           #f.close()
                    
        action=ttk.Button(monty, text="Save", command= clickMe)
        #action.configure(state='disabled')#widget gets disabled
        action.grid(column=1, row=12)
        tt.createToolTip(action, 'Click to Save')
#################################################################################
#################################################################################
        self.strx=['xx','xx','xx','xx','xx','xx','xx', 'xx']
        monty1=ttk.LabelFrame(search, text='SEARCH')
        monty1.pack_propagate(0)
        monty1.pack(fill=tk.BOTH, expand=1)
        
        '''
        monty2=ttk.Frame(monty1)
        monty2.pack_propagate(0)
        monty2.pack(fill=tk.BOTH, expand=1)'''

        #PRODUCT ID ENTRY
        ttk.Label(monty1, text='Enter Product ID:', font=cg_font4).grid(column=0, row=0, sticky='EW', padx=8, pady=4)
        self.name5=tk.StringVar()
        nameEntered5=ttk.Entry(monty1, width=30, textvariable=self.name5)
        nameEntered5.grid(column=0, row=1,sticky='W', padx=8, pady=4)
        tt.createToolTip(nameEntered5, 'Enter Product ID')

        #PRODUCT NAME
        ttk.Label(monty1, text='Product:', font=cg_font5).grid(column=0, row=2, sticky='W', padx=8, pady=4)
        self.pro=tk.StringVar()
        self.pro.set(self.strx[0])
        proent=ttk.Entry(monty1, width=20, textvariable=self.pro)
        proent.grid(column=1, row=2,sticky='W', padx=8, pady=4)
        #tt.createToolTip(nameEntered5, 'Enter Product ID')


        #BRAND NAME
        ttk.Label(monty1, text='Brand:', font=cg_font5).grid(column=0, row=3, sticky='W', padx=8, pady=4)
        self.brand=tk.StringVar()
        self.brand.set(self.strx[1])
        brandent=ttk.Entry(monty1, width=20, textvariable=self.brand)
        brandent.grid(column=1, row=3,sticky='W', padx=8, pady=4)

        #QUANTITY
        ttk.Label(monty1, text='Quantity:', font=cg_font5).grid(column=0, row=4, sticky='W', padx=8, pady=4)
        self.quan=tk.StringVar()
        self.quan.set(self.strx[2])
        quanent=ttk.Entry(monty1, width=20, textvariable=self.quan)
        quanent.grid(column=1, row=4,sticky='W', padx=8, pady=4)

        #DATE OF ENTRY 
        ttk.Label(monty1, text='Date of Entry:', font=cg_font5).grid(column=0, row=5, sticky='W', padx=8, pady=4)
        self.date=tk.StringVar()
        self.date.set(self.strx[3])
        dateent=ttk.Entry(monty1, width=20, textvariable=self.date)
        dateent.grid(column=1, row=5,sticky='W', padx=8, pady=4)

        #DATE OF PURCHASE
        ttk.Label(monty1, text='Date of Purchase:', font=cg_font5).grid(column=0, row=6, sticky='W', padx=8, pady=4)
        self.date2=tk.StringVar()
        self.date2.set(self.strx[4])
        date2ent=ttk.Entry(monty1, width=20, textvariable=self.date2)
        date2ent.grid(column=1, row=6,sticky='W', padx=8, pady=4)

        #SHELF NUMBER
        ttk.Label(monty1, text='Shelf Number:', font=cg_font5).grid(column=0, row=7, sticky='W', padx=8, pady=4)
        self.shelf=tk.StringVar()
        self.shelf.set(self.strx[5])
        shelfent=ttk.Entry(monty1, width=20, textvariable=self.shelf)
        shelfent.grid(column=1, row=7,sticky='W', padx=8, pady=4)

        #food or medicine
        ttk.Label(monty1, text='Food or Medicine?:', font=cg_font5).grid(column=0, row=8, sticky='W', padx=8, pady=4)
        self.form=tk.StringVar()
        self.form.set(self.strx[6])
        forment=ttk.Entry(monty1, width=20, textvariable=self.form)
        forment.grid(column=1, row=8, sticky='W', padx=8, pady=4)

        #GLASS ITEM
        ttk.Label(monty1, text='Glass Item?', font=cg_font5).grid(column=0, row=9, sticky='W', padx=8, pady=4)
        self.glass=tk.StringVar()
        self.glass.set(self.strx[7])
        glsent=ttk.Entry(monty1, width=20, textvariable=self.glass)
        glsent.grid(column=1, row=9,sticky='W', padx=8, pady=4)


        def clickMe2():
            self.stry=['parle g', 'parle', '100', '3/12/2015, 3/12/2015', '15', 'yes', 'yes'] 
            self.pro.set(self.stry[0])
            self.brand.set(self.stry[1])
            self.quan.set(self.stry[2])
            self.date.set(self.stry[3])
            self.date2.set(self.stry[4])
            self.shelf.set(self.stry[5])
            self.form.set(self.stry[6])
            #self.glass.set(self.strx[7])

        def clickMe3():
            self.pro.set('xx')
            self.brand.set('xx')
            self.quan.set('xx')
            self.date.set('xx')
            self.date2.set('xx')
            self.shelf.set('xx')
            self.form.set('xx')
            self.glass.set('xx')

        action1=ttk.Button(monty1, text="Search", width=21, command= clickMe2)
        #action.configure(state='disabled')#widget gets disabled
        action1.grid(column=1, row=11, columnspan=2, sticky='w'+'e', padx=4, pady=2)
        tt.createToolTip(action1, 'Click to Search')

        action2=ttk.Button(monty1, text="Reset", width=21, command= clickMe3)
        #action.configure(state='disabled')#widget gets disabled
        action2.grid(column=1, row=10, columnspan=2, sticky='w'+'e', padx=4, pady=2)
        tt.createToolTip(action1, 'Click to Reset')

        #win.mainloop()
