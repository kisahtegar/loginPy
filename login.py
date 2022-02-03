import tkinter as tk

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        #self.master = master
        self.label()
        self.entry()
        self.button()

    def label(self):
        # Title Label
        self.T_Label = tk.Label(self.master)
        self.T_Label.config(text="Login Page", font=("italic", 20))
        self.T_Label.place(x=120 ,y=15)
        # Username Label
        self.U_Label = tk.Label(self.master)
        self.U_Label.config(text="Username", font=("times new roman", 15))
        self.U_Label.place(x=45, y=60)
        # Password Label
        self.P_Label = tk.Label(self.master)
        self.P_Label.config(text="Password", font=("times new roman", 15))
        self.P_Label.place(x=45, y=95)
    
    def entry(self):
        # Username Entry
        self.U_Entry = tk.Entry(self.master)
        self.U_Entry.config(width=30)
        self.U_Entry.place(x=145, y=65)
        # Password Entry
        self.P_Entry = tk.Entry(self.master)
        self.P_Entry.config(show="*", width=30)
        self.P_Entry.place(x=145, y=100)

    def button(self):   
        # Login Button
        self.L_Button = tk.Button(self.master)
        self.L_Button.config(text="Login", height=2, width=10)
        self.L_Button.place(x=100, y=130)
        # Exit Button
        self.E_Button = tk.Button(self.master)
        self.E_Button.config(text="Exit", height=2, width=10, command=root.quit)
        self.E_Button.place(x=200, y=130)

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master = master
        self.config(bg="white")
        self.master.geometry("400x200")
        
        self.login = LoginPage(self)
        self.login.pack()

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(width="False", height="False")
    MainApplication(root).pack()
    root.mainloop()