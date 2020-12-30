from tkinter import *
import os
import datetime

def date(file_corespend):
    day = datetime.datetime.now().day
    months = datetime.datetime.now().month
    year = datetime.datetime.now().year
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    file_corespend.write(f"connected at {day} {months} {year} at {Time}"+"\n")
    file_corespend.write(username1 + "\n")
    file_corespend.write(password1)
    file_corespend.close()

def screen7_delete():
    screen7.destroy()


def saved():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Information")
    screen7.geometry("300x150")
    Label(screen7, text = "your file is successfully saved", bg="green",width = 120, height = 80).pack()
    Button(screen7, text = ("OK"), command = screen7_delete).pack()


def screen6_delete():
    screen6.destroy()


def create_button():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename,"w")
    data.write(notes)
    data.close()
    saved()

def create_notes():
    global screen6
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    screen6 = Toplevel(screen)
    screen6.title("Creating a new note")
    screen6.geometry("1080x720")
    Label(screen6, text = "Creating a new note", width = 300, height = 3, bg = "grey", font=("calibri" , 15)).pack()
    Label(screen6, text = "").pack()
    Label(screen6 , text = "please enter the name of the file you want to create:").pack()
    Entry(screen6, textvariable = raw_filename).pack()
    Label(screen6 , text = "please enter you note:").pack()
    Entry(screen6, textvariable = raw_notes).pack()
    Button(screen6, text = "Create the note", command = create_button).pack()
    Button(screen6, text = 'Undo', command = screen6_delete).pack()

def screen9_delete():
    screen9.destroy()


def view_notes1():
    global screen9
    filename1 = raw_filename1.get()
    data1 = open(filename1 , "r")
    data2 = data1.read()
    screen9 = Toplevel(screen)
    screen9.title("notes")
    screen9.geometry("400x400")
    Label(screen9, text = data2).pack()
    Label(screen9,text = ("")).pack()
    Button(screen9, text = "Back", command = screen9_delete)
    data1.close()


def view_notes():
    global screen8
    screen8 = Toplevel()
    screen8.title("Your Notes")
    screen8.geometry("400x400")
    Label(screen8, text=f"You Notes {username1}", width=300, height=3, bg="grey", font=("calibri", 15)).pack()
    all_files = os.listdir()
    Label(screen8, text = all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen8 , textvariable = raw_filename1).pack()
    Button(screen8,text ="ok" , command = view_notes1).pack()

def screen11_deleet():
    screen11.destroy()

def yes_button():
    screen11_deleet()
    filename = filename_delete.get()
    screen12 = Toplevel(screen)
    screen12.title(f"deleting {filename}")
    screen12.geometry("400x400")
    os.remove(filename)
    Label(screen12, text = f"deleting {filename}... ").pack()
    Label(screen12, text = f"{filename} is deleted").pack()


def no_button():
    screen11.destroy()



def delete_file():
    global screen11
    filename = filename_delete.get()
    screen11 = Toplevel(screen)
    screen11.title("Delete Confimation")
    screen11.geometry("400x400")
    Label(screen11, text = f"Do you want to delete {filename}? ").pack()
    Button(screen11, text = "yes", command = yes_button).pack()
    Button(screen11, text = "No", command = no_button).pack()

def delete_notes():
    global screen10
    screen10 = Toplevel(screen)
    screen10.title("Delete page")
    screen10.geometry("400x400")
    Label(screen10, text=f"Delete You Notes {username1}", width=300, height=3, bg="grey", font=("calibri", 15)).pack()
    All_files = os.listdir()
    Label(screen10, text="wish file do you want to delete").pack()
    Label(screen10, text = "").pack()
    Label(screen10, text = All_files).pack()
    global filename_delete
    filename_delete = StringVar()
    Entry(screen10, textvariable = filename_delete).pack()
    Button(screen10, text = "ok", command = delete_file).pack()




def session():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Django")
    screen3.geometry("1920x1080")
    Label(screen3,text = f"Welcome to Django {username1} , the revolutionary app", width = 300, height = 3 , bg="grey", font=("calibri, 15")).pack()
    Label(screen3, text=("")).pack()
    Button(screen3,text = "create notes", command = create_notes).pack()
    Label(screen3, text=("")).pack()
    Button(screen3,text = "view my Notes", command = view_notes).pack()
    Label(screen3, text=("")).pack()
    Button(screen3, text = "Delete a Note", command = delete_notes).pack()
    Label(screen3, text=("")).pack()
    Button(screen3, text = "Disconnect", command = screen3_delete).pack()




def screen3_delete():
    screen3.destroy()

def screen4_delete():
    screen4.destroy()

def screen5_delete():
    screen5.destroy()


def password_error():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5,text = "password error", bg = "red", font=("calibri", 13)).pack()
    Label(screen5,text=("")).pack()
    Label(screen5, text="Wrong Password ").pack()
    Label(screen5, text="please Try again").pack()
    Label(screen5, text=("")).pack()
    Button(screen5,text="OK", command=screen5_delete).pack()


def user_not_found():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")
    Label(screen4,text="user not found", bg="red", font=("calibri", 13)).pack()
    Label(screen4, text=("")).pack()
    Label(screen4,text = "This user does not existe ").pack()
    Label(screen4,text = "please register").pack()
    Button(screen4,text = "OK", command = screen4_delete).pack()


def sucessfully_connected():
    session()


def login_verify():
    global username1
    global password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        file1.close()
        if password1 in verify:
            sucessfully_connected()
        else :
            password_error()
    else:
        user_not_found()




def register_button():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write("                                              user information\n")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(screen1, text= "sucessfully registered", fg="green",font=("ariel", 18)).pack()





def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login page")
    screen2.geometry("1080x720")
    Label(screen2, text = "Login Page", width = 300, height = 3, bg = "grey" , font=("ariel, 15")).pack()
    Label(text=("")).pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1

    Label(screen2, text="username *").pack()
    Label(screen2,text=("")).pack()
    username_entry1 = Entry(screen2,textvariable = username_verify)
    username_entry1.pack()
    Label(text=("")).pack()
    Label(screen2, text="password *").pack()
    password_entry1 = Entry(screen2,textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text=("")).pack()
    Button(screen2, text="Connect",  width = 10 , height = 2, command= login_verify).pack()
    Label(screen2, text=("")).pack()
    Button(screen2, text="reset you password",width = 15 , height = 2).pack()



def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("register test 0.1V")
    screen1.geometry("300x250")
    global username
    global password
    global username_entry
    global password_entry #to have this variable in all the script and not only in this function
    username = StringVar()
    password = StringVar()
    Label(screen1, text="Register Page", bg="grey", font=("calibri", 15)).pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text="username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1, text="password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_button).pack()


def admin_button():
    global screen15
    screen15 = Toplevel(screen)
    screen15.title("admin dashboard")
    screen15.geometry("720x560")
    

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("1920x1080")
    screen.title("Note App")
    Label(text = "Note App", bg = "grey",width = "1920", height = "3", font=("calibri", 13)).pack()
    Label(text = ("")).pack()
    Button(text = "Login",width = "100", height = "3", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register",width = "100", height = "3", command = register).pack()
    Button(screen , text = "admin button" , bg = "grey", command = admin_button)


    screen.mainloop()




main_screen()
