from tkinter import Label, StringVar, messagebox, Menu, Tk, Entry, IntVar, Checkbutton, Radiobutton, Button, END
import sys

def tkinter_gui():
    # creating a tkinter GUI is a pain. In this case I used pixel count to design the window.
 

    #Creating object 'root' of Tk()

    root = Tk()

 

    #Providing Geometry to the form

    root.geometry("500x640")

 

    def exit_app():

        sys.exit()

 

    # Top of Screen Menu

    root_menu = Menu(root)

    root.config(menu=root_menu)

    root.title('Tool Name')

 

    file_menu = Menu(root_menu)

    root_menu.add_cascade(label='File', menu=file_menu)

    file_menu.add_cascade(label='Quit', command=exit_app)

 

    def about():

        messagebox.showinfo("This Application is made by Anthony Fenner")

 

    def version():

        messagebox.showinfo("Version History",

                            "Update: Version 1 - Created App.\n"

                            "Update: Version 2 - Bug Fix.\n"
 

    about_menu = Menu(root_menu)

    root_menu.add_cascade(label='About', menu=about_menu)

    about_menu.add_cascade(label='About', command=about)

    about_menu.add_cascade(label='Version', command=version)

 

    # Username and Password Login

    user_name = StringVar()

    pass_word = StringVar()

 

    username_label = Label(root, text="Username: ", width=20, font=("bold",10))

    username_label.place(x=80,y=20)

    user = Entry(root, text="Username", show=None, font=("bold",10), textvariable=user_name)

    user.place(x=240, y=20)

 
    # this is a great way to allow the user to toggle the veiw of their password.
    def show_hid_password():

        if(check_var.get()):

            passw.config(show="")

        else:

            passw.config(show="*")

 

    password_label = Label(root, text="Password: ", width=20, font=("bold",10))
    password_label.place(x=80,y=60)

    passw = Entry(root, text="password", show='*', font=("bold",10), textvariable=pass_word)
    passw.place(x=240, y=60)

 

    check_var = IntVar()
    Checkbutton(root,text="Show", variable=check_var, onvalue=1, offvalue=0, command=show_hid_password).place(x=400,y=60)

    provider = StringVar()

 

    #this creates 'Label' widget for Provider data

    label_1 =Label(root, text="Provider: ", width=20,font=("bold",10))
    label_1.place(x=80,y=100)

    entry_1 = Entry(root, text="provider", show=None, font=("bold",10), textvariable=provider)
    entry_1.place(x=240,y=100) 

    #the variable 'var' mentioned here holds Integer Value, by default 0
    var5=IntVar()

    #this creates 'Radio button' widget and uses place() method

    Radiobutton(root,text="radiob1",padx= 5, variable=var5, value=1).place(x=180,y=220)

    Radiobutton(root,text="radiob2",padx= 20, variable=var5, value=2).place(x=245,y=220)

 

    # State Function WA

    var8 = IntVar()

    var9 = IntVar()

    var10 = IntVar()

 

    # State Function NM

    var11 = IntVar()

    var12 = IntVar()

    var13 = IntVar()

    var14 = IntVar()

 

    def wa_state_func():

 

        catt1 = Checkbutton(root,text="LOB1", variable=var8)

        catt1.place(x=100,y=320)

        catt2 = Checkbutton(root,text="LOB2", variable=var9)

        catt2.place(x=190,y=320)

        catt3 = Checkbutton(root,text="LOB3", variable=var10)

        catt3.place(x=280,y=320)

 

    def new_mex_state_func():

 

        cat_1 = Checkbutton(root,text="LOB1", variable=var11)

        cat_1.place(x=95,y=320)

        cat_2 = Checkbutton(root,text="LOB2", variable=var12)

        cat_2.place(x=180,y=320)

        cat_3 = Checkbutton(root,text="LOB3", variable=var13)

        cat_3.place(x=240,y=320)

        cat_4 = Checkbutton(root,text="LOB4", variable=var14)

        cat_4.place(x=350,y=320)

 

    #the variable 'var' mentioned here holds Integer Value, by deault 0

    # var = IntVar()

 

    #this creates 'Radio button' widget and uses place() method

    wa_button = Button(root,text="Button One",padx= 5, command=wa_state_func)

    wa_button.place(x=140,y=270)

    new_mex_button = Button(root,text="Button Two",padx= 20, command=new_mex_state_func)

    new_mex_button.place(x=260,y=270)

    ######################################
    # Find Files

    prac_only_data = StringVar()

    prov_only_data = StringVar()

 

    label_6 = Label(root,text="File1: ", width=20,font=("bold",10))

    label_6.place(x=20,y=370)

 

    ent1=Entry(root, font=('Arial', 14), textvariable=prac_only_data)

    ent1.place(x=140,y=370)

 

    def prac_only_func():

        filename =askopenfilename(filetypes=(('CSV File', '*.csv'), ('All Files', '*.*')))

        ent1.insert(END, filename) # add this

 

    b1=Button(root,text="Open",width=10,font=('bold',10),command=prac_only_func)

    b1.place(x=370,y=370)

 

    # Prov Only Pull

 

    label_7 =Label(root,text="File2: ", width=20,font=("bold",10))

    label_7.place(x=20,y=420)

 

    ent2=Entry(root, font=('Arial', 14), textvariable=prov_only_data)

    ent2.place(x=140,y=420)

 

    def prov_only_func():

        filename2 =askopenfilename(filetypes=(('CSV File', '*.csv'), ('All Files', '*.*')))

        ent2.insert(END, filename2) # add this

 

    b2=Button(root,text="Open",width=10,font=('bold',10),command=prov_only_func)

    b2.place(x=370,y=420)

 

    #the variable 'var' mentioned here holds Integer Value, by deault 0

    var6=IntVar()

 

    #this creates 'Radio button' widget and uses place() method

    Radiobutton(root,text="radiob1",padx= 5, variable= var6, value=1).place(x=60,y=480)

    Radiobutton(root,text="radiob2",padx= 20, variable= var6, value=2).place(x=120,y=480)

    Radiobutton(root,text="radiob3",padx= 5, variable= var6, value=3).place(x=220,y=480)

    Radiobutton(root,text="radiob1",padx= 20, variable= var6, value=4).place(x=340,y=480)

 

    #the variable 'var' mentioned here holds Integer Value, by deault 0

    var7=IntVar()

 

    #this creates 'Radio button' widget and uses Office Hours analysis

    Radiobutton(root,text="radiob1",padx= 5, variable= var7, value=1).place(x=60,y=530)

    Radiobutton(root,text="radiob2",padx= 20, variable= var7, value=2).place(x=180,y=530)

    Radiobutton(root,text="radiob1",padx= 5, variable= var7, value=3).place(x=354,y=530)

 

 

    def delete_login_success():

        root.destroy()

 

    #this creates button for submitting the details provides by the user

    new_button = Button(root, text='Submit' , width=20,bg="black",fg='white', command=delete_login_success)

    new_button.place(x=180,y=580)

 

 

    #this will run the mainloop.

    root.mainloop()

 
    # You have to use .get() to pull the data stored in the variable.
    return user_name.get(), pass_word.get(), var5.get(), var8.get(), var9.get(), var10.get(), var11.get(), var12.get(), var13.get(), var14.get(), prac_only_data.get(), prov_only_data.get(), var6.get(), provider.get(), var7.get()

 
