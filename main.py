#Import Statements======================================================================================================

import pickle
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

#Global Variables========================================================================================================

headers = ["Account No.","Name","Balance"]

#GUI Methods=============================================================================================================

def display_table(window,data):
    #Helps in displaying table with rows and columns obtained from data
    rows = []
    for i in range(len(data)):
        
        cols = []

        for j in range(len(data[0])):
            
            e = Entry(window,relief=GROOVE)
            e.grid(row=i, column=j, sticky="NSEW")
            e.insert(END, data[i][j])
            cols.append(e)

        rows.append(cols)

    window.mainloop()



def showAllRecordsWindow():
    #shows window with all records present when the user clicks on show all records button
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    data = list(data)
    data.insert(0,headers)
    
    newWindow = Toplevel(root)
    newWindow.title("Records with us")
    
    display_table(newWindow,data)
 


def searchRecord():
    #shows window with text box to enter acc no and then opens a new window with all the details of the record 
    searchWindow = Toplevel(root)
    searchWindow.title("Search for a record")
    acc_var = IntVar()


    acc_label = Label(searchWindow, text = 'Account No: ', font=('calibre',10, 'bold'))
    acc_entry = Entry(searchWindow,textvariable = acc_var, font=('calibre',10,'normal'))
    
    def submit():
        bfile= open("databases/Banking_records.dat","rb")
        data = pickle.load(bfile)
        data = list(data)
        acc_no = acc_var.get()
        rec = list(filter(lambda x : x[0] == acc_no,data))
        if rec == []:
            messagebox.showerror("Account","No account with the entered acc no. exists")
        else:
            rec.insert(0,headers)
            display_table(searchWindow,rec)
        
        
    sub_btn=Button(searchWindow,text = 'Submit', command = submit)
    
    acc_label.grid(row=0,column=0)
    acc_entry.grid(row=0,column=1)
    sub_btn.grid(row=1,columnspan = 2)

    #Inifinite loop for window to display
    searchWindow.mainloop()

def recordAdditionWindow():
    #allows the user to add record within the table by showing a window with two text boxes where we could enter name and balance
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    if data == []:
        acc_no = 101
    else:
        acc_no = data[-1][0] + 1
    
    
    addWindow = Toplevel(root)
    addWindow.title("Add A Record")
    name_var=StringVar()
    bal_var=IntVar()
 

    def submit():
    
        name=name_var.get()
        bal=bal_var.get()

        data.append([acc_no,name,bal])
        fin = open("databases/Banking_records.dat","wb")
        pickle.dump(data,fin)
        fin.close()
        messagebox.showinfo("Record", "Record has been added")
        name_var.set("")
        bal_var.set("")
     
    
    name_label = Label(addWindow, text = 'Name ', font=('calibre',10, 'bold'))
    name_entry = Entry(addWindow,textvariable = name_var, font=('calibre',10,'normal'))
    
    bal_label = Label(addWindow, text = 'Balance ', font = ('calibre',10,'bold'))
    bal_entry=Entry(addWindow, textvariable = bal_var, font = ('calibre',10,'normal'))
    
    sub_btn= Button(addWindow,text = 'Submit', command = submit)
    
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    bal_label.grid(row=1,column=0)
    bal_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)

    addWindow.mainloop()


def deletionWindow():
    #opens window where we can write the name and acc no of the record which we want to delete
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    
    
    deleteWindow = Toplevel(root)
    deleteWindow.title("Delete A Record")
    name_var=StringVar()
    acc_var=IntVar()
 
    def submit():
    
        name=name_var.get()
        acc=acc_var.get()
        f = 0
        for i in range(len(data)):
            if data[i][0] == acc and data[i][1] == name:
                del data[i]
                messagebox.showinfo("Deletion", "Account Deleted")
                f = 1
                break
        if f == 0:
            messagebox.showerror("Account Error","Account does not exist")
        fin = open("databases/Banking_records.dat","wb")
        pickle.dump(data,fin)
        fin.close()
        
        name_var.set("")
        acc_var.set("")
     
     
    name_label = Label(deleteWindow, text = 'Name ', font=('calibre',10, 'bold'))
    name_entry = Entry(deleteWindow,textvariable = name_var, font=('calibre',10,'normal'))
    
    acc_label = Label(deleteWindow, text = 'Account No. ', font = ('calibre',10,'bold'))
    acc_entry=Entry(deleteWindow, textvariable = acc_var, font = ('calibre',10,'normal'))
    
    sub_btn= Button(deleteWindow,text = 'Submit', command = submit)
    
    
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    acc_label.grid(row=1,column=0)
    acc_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)

    deleteWindow.mainloop()


def depWindow():
    #opens window that takes acc no and deposit to be made to that account
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    
    
    
    depositWindow = Toplevel(root)
    depositWindow.title("Deposit Window")
    acc_var=IntVar()
    dep_var=IntVar()
 

    def submit():
    
        acc_no=acc_var.get()
        dep=dep_var.get()
        f = 0
        for i in data:
            if i[0] == acc_no:
                data[data.index(i)][2] += dep
                f = 1
                messagebox.showinfo("Record", "Amount has been Deposited")
                break
        if f == 0:
            print("Account does not exist")
            messagebox.showerror("Record", "Accound does not exist")

        fin = open("databases/Banking_records.dat","wb")
        pickle.dump(data,fin)
        fin.close()
        
        acc_var.set(0)
        dep_var.set(0)
     
    
    acc_label = Label(depositWindow, text = 'Account No. ', font=('calibre',10, 'bold'))
    acc_entry = Entry(depositWindow,textvariable = acc_var, font=('calibre',10,'normal'))
    
    dep_label = Label(depositWindow, text = 'Amount to Deposit ', font = ('calibre',10,'bold'))
    dep_entry=Entry(depositWindow, textvariable = dep_var, font = ('calibre',10,'normal'))
    
    sub_btn= Button(depositWindow,text = 'Submit', command = submit)
    
    acc_label.grid(row=0,column=0)
    acc_entry.grid(row=0,column=1)
    dep_label.grid(row=1,column=0)
    dep_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)

    depositWindow.mainloop()

def withdrawMonWindow():
    #allows the user to withdraw money from acc using acc no and amount to be withdrawn
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    
    
    
    withdrawWindow = Toplevel(root)
    withdrawWindow.title("Withdraw Window")
    acc_var=IntVar()
    wd_var=IntVar()
 

    def submit():
    
        acc_no=acc_var.get()
        wd=wd_var.get()
        f = 0
        for i in data:
            if i[0] == acc_no:
                f = 1
                if wd > i[2]:
                    messagebox.showerror("Warning",("You cannot withdraw this amt. You have only Rs. "+ str(i[2]) +" in your account"))
                else:     
                    data[data.index(i)][2] -= wd
                    messagebox.showinfo("Record","Amount Rs. "+ str(wd) + " has been withdrawn")
                    break
        if f == 0:
            messagebox.showerror("Account Error", "Account no. does not exist")
        fin = open("databases/Banking_records.dat","wb")
        pickle.dump(data,fin)
        fin.close()
        
        acc_var.set(0)
        wd_var.set(0)
     
    
    acc_label = Label(withdrawWindow, text = 'Account No. ', font=('calibre',10, 'bold'))
    acc_entry = Entry(withdrawWindow,textvariable = acc_var, font=('calibre',10,'normal'))
    
    wd_label = Label(withdrawWindow, text = 'Amount to Withdraw ', font = ('calibre',10,'bold'))
    wd_entry=Entry(withdrawWindow, textvariable = wd_var, font = ('calibre',10,'normal'))
    
    sub_btn= Button(withdrawWindow,text = 'Submit', command = submit)
    
    acc_label.grid(row=0,column=0)
    acc_entry.grid(row=0,column=1)
    wd_label.grid(row=1,column=0)
    wd_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)

    withdrawWindow.mainloop()

def richestWindow():
    #allows us to see the record of the person with the highest balance
    richWindow = Toplevel(root)
    richWindow.title("Richest person on the record")
    bfile = open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    max_bal = 0
    rich = []
    for i in data:
        if i[2]> max_bal:
            rich = i
            max_bal = i[2]
    fdata = [headers,rich]
    display_table(richWindow,fdata)

#Command Line Methods===============================================================================================
#the work done by each function can be easily understood by reading its name as I have tried to make the function names as self-explanatory as possible
def show_data():
    
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    print("%10s"%"Account_no.","%20s"%"Account Holder Name","%20s"%"Balance")
    print("=====================================================================")
    for i in data:
        print("%10s"%str(i[0]),"%20s"%str(i[1]),"%20s"%str(i[2]))
    bfile.close()

def search_rec():
    acc_no = int(input("Enter acc no which you want details about"))
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    f = 0
    for i in data:
        if str(i[0]) == str(acc_no):
            print("%10s"%"Account_no.","%20s"%"Account Holder Name","%20s"%"Balance")
            print("=====================================================================")
            print("%10s"%str(i[0]),"%20s"%str(i[1]),"%20s"%str(i[2]))
            f = 1
    if f == 0:
        print("Record does not exist")

def add_record():
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    if data == []:
        acc_no = 101
    else:
        acc_no = data[-1][0] + 1
    name = input("Enter Account Name Holder: ")
    bal = int(input("Enter Account Balance: "))
    data.append([acc_no,name,bal])
    fin = open("databases/Banking_records.dat","wb")
    pickle.dump(data,fin)

def del_record():
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Name Holder: ")
    for i in range(len(data)):
        if data[i][0] == acc_no and data[i][1] == name:
            del data[i]
            break
    fin = open("databases/Banking_records.dat","wb")
    pickle.dump(data,fin)
    fin.close()
    print("Account Deleted")

def deposit():
    acc_no = int(input("Enter acc no in which you want to deposit money: "))
    dep = int(input("Amount to deposit"))
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    f = 0
    bfile.close()
    for i in data:
        if i[0] == acc_no:
            data[data.index(i)][2] += dep
            f = 1
            break
    if f == 0:
        print("Account does not exist")
    fin = open("databases/Banking_records.dat","wb")
    pickle.dump(data,fin)

def withdraw():
    acc_no = int(input("Enter acc no in which you want to deposit money: "))
    wd = int(input("Amount to be withdrawn: "))
    bfile= open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    bfile.close()
    for i in data:
        if i[0] == acc_no:
            while True:
                if wd > i[2]:
                    print(f"You cannot withdraw this amt. You have only { i[2] } in your account")
                    choice = input("Do you want to exit?(y/n):")
                    if choice.upper() == "Y":
                        break
                    else:
                        wd = int(input("Enter new amt to withdraw: "))
                else:     
                    data[data.index(i)][2] -= wd
                    break
                                 
    
    fin = open("databases/Banking_records.dat","wb")
    pickle.dump(data,fin)
    fin.close()

def richest():
    bfile = open("databases/Banking_records.dat","rb")
    data = pickle.load(bfile)
    max_bal = 0
    rich = []
    for i in data:
        if i[2]> max_bal:
            rich = i
            max_bal = i[2]
    print(f"{rich[1]} has a balance of {rich[2]}")



#Driver Code=================================================================================================================


while True:
    #ifinite loop
    mode = input("Enter mode: ")
    if mode == 'gui':
        #gui mode
        root=Tk()
        root.title("Bank UI")
        root.geometry("800x800")
        root.configure(bg='blue')
        n_rows =4
        n_columns =3
        for i in range(n_rows):
            root.grid_rowconfigure(i,  weight =1)
        for i in range(n_columns):
            root.grid_columnconfigure(i,  weight =1)

        fontStyle = tkFont.Font(family="Lucida Grande", size=24)
        buttonfontStyle = tkFont.Font(family="Lucida Grande", size=14)
        label_bank = Label(root,text = "DP Bank\nProject By Daksh Pari",background="blue", font=fontStyle)
        label_bank.grid(columnspan = 3)



        disp_btn = Button(root, text="Display all the records",font=buttonfontStyle,command = showAllRecordsWindow)
        disp_btn.grid(row =1 ,column=0,sticky="NSEW")

        search_btn = Button(root, text="Search for record",font=buttonfontStyle,command=searchRecord)
        search_btn.grid(row =1 ,column=1,sticky="NSEW")

        add_btn = Button(root, text="Add a record",font=buttonfontStyle,command = recordAdditionWindow)
        add_btn.grid(row =1 ,column=2,sticky="NSEW")



        del_btn = Button(root, text="Delete a record",font=buttonfontStyle,command = deletionWindow)
        del_btn.grid(row =2 ,column=0,sticky="NSEW")

        deposit_btn = Button(root, text="Deposit money in an account",font=buttonfontStyle,command = depWindow)
        deposit_btn.grid(row =2 ,column=1,sticky="NSEW")

        withdraw_btn = Button(root, text="Withdraw Money",font=buttonfontStyle,command = withdrawMonWindow)
        withdraw_btn.grid(row =2 ,column=2,sticky="NSEW")

        richest_btn = Button(root, text="Show the richest man",font=buttonfontStyle,command= richestWindow)
        richest_btn.grid(columnspan=3,sticky="NSEW")

        root.mainloop()

    elif mode == 'cli':
        #Command line
        while True:
            
            print("%10s"%"Choice","%20s"%"|","%20s"%"Task")
            print("%10s"%"1","%20s"%"|","%20s"%"Display all the records")
            print("%10s"%"2","%20s"%"|","%20s"%"Search a record")
            print("%10s"%"3","%20s"%"|","%20s"%"Add a client")
            print("%10s"%"4","%20s"%"|","%20s"%"Deposit Money")
            print("%10s"%"5","%20s"%"|","%20s"%"Who's the richest?")
            print("%10s"%"6","%20s"%"|","%20s"%"Delete a record")
            print("%10s"%"7","%20s"%"|","%20s"%"Withdraw money")
            print("%10s"%"8","%20s"%"|","%20s"%"Exit")

            ch = int(input("Enter choice"))
            if ch == 1:
                show_data()
            elif ch == 2:
                search_rec()
            elif ch == 3:
                add_record()
            elif ch == 4:
                deposit()
            elif ch == 5:
                richest()
            elif ch == 6:
                del_record()
            elif ch==7:
                withdraw()
            elif ch==8:
                break                         
            else:
                print("Enter correct choice!")
            print("\n"*15)
    elif mode == "exit":
        print("Out of the Program! Thanks for trying it")

    else:
        print("This mode does not exist!Try Again\n")