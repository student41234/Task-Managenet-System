from tkinter import*
from tkinter import ttk,messagebox
import pymysql

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("SIGN  IN  Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        
        left_lbl=Label(self.root,bg="#031F3C")
        left_lbl.place(x=600,y=0,relwidth=1,relheight=1)


        right_lbl=Label(self.root,bg="#08A3D2")
        right_lbl.place(x=600,y=0,relwidth=1,relheight=1)




        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=300,y=100,width=700,height=500)

        title=Label(login_frame,text="SIGN  IN  HERE",font=("times",30,"bold"),bg="white",fg="#08A3D2").place(x=50,y=50)
       
       
        email=Label(login_frame,text="EMAIL  ADRESS",font=("times",18,"bold"),bg="white",fg="gray").place(x=50,y=130)
        self.txt_email=Entry(login_frame,font=("times",15,),bg="lightgray")
        self.txt_email.place(x=50,y=180,width=350,height=35)


        password=Label(login_frame,text="PASSWORD",font=("times",18,"bold"),bg="white",fg="gray").place(x=50,y=230)
        self.txt_password=Entry(login_frame,font=("times",15,),bg="lightgray")
        self.txt_password.place(x=50,y=280,width=350,height=35)


        btn_reg=Button(login_frame,text="Register New Account?",command=self.register_window,cursor="hand2",fg="#B00857",bg="white",font=("times",15,"bold"),bd=0)
        btn_reg.place(x=40,y=330,width=230)


        btn_log=Button(login_frame,text="login",command=self.login,fg="white",bg="#B00857",cursor="hand2",font=("times",20,"bold"),bd=0)
        btn_log.place(x=50,y=380,width=100,height=35)

    
    def register_window(self):
        self.root.destroy()
        import register
        

    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee2 where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username &Pasword",parent=self.root)
                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    import tms

                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root) 


        



root=Tk()
obj=Login(root)
root.mainloop()    