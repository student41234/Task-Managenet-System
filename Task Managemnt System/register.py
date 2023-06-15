from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
class reg:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        #==========Bg Image============

        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #================Left Image==================
        self.left=ImageTk.PhotoImage(file="images/sd.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #=============Register Frame=================
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #====================Row1=====
        
        f_name=Label(frame1,text="First Name",font=("times",15,"bold"),bg="white",fg="grey").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        l_name=Label(frame1,text="Last Name",font=("times",15,"bold"),bg="white",fg="grey").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        #=====================Row2======
        contact=Label(frame1,text="Contact Number",font=("times",15,"bold"),bg="white",fg="grey").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times",15,"bold"),bg="white",fg="grey").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        #===================Row3========
        quest=Label(frame1,text="Security Question",font=("times",15,"bold"),bg="white",fg="grey").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times",13),state="readonly",justify=CENTER)
        self.cmb_quest["values"]=("Select","Your First Pet Name","Your Birth Place","Your Best Friend")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        ans=Label(frame1,text="Answer",font=("times",15,"bold"),bg="white",fg="grey").place(x=370,y=240)
        self.txt_ans=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_ans.place(x=370,y=270,width=250)

        #===================Row4====
        password=Label(frame1,text="Password",font=("times",15,"bold"),bg="white",fg="grey").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times",15,"bold"),bg="white",fg="grey").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)


        #==========Terms========
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agre All The terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times",12)).place(x=50,y=380)
        
        
        
        self.btn_img=ImageTk.PhotoImage(file="images/rg.jpg")
        btn=Button(frame1,image=self.btn_img,bd=0,command=self.register_data,cursor="hand2").place(x=50,y=410,width=270,height=30)
        
        #=========  Sign In =========
        sig_btn=Button(left,text="SIGN  IN",bd=0,command=self.login_window,cursor="hand2",bg="white",fg="red",font="times 12 bold").place(x=215,y=470,width=100)
        
    
    def login_window(self):
        self.root.destroy()
        import login


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_ans.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.var_chk=(0)
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_ans.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fiels Are Requird",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our terms & Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee2")
                cur=con.cursor()
                cur.execute("select * from employee2 where email=%s",self.txt_email.get())
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","Use Already Exists,Please try with Another Email",parent=self.root)
                else:
                    cur.execute("insert into employee2 (f_name,l_name,contact,email,quest,ans,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                    self.txt_lname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_ans.get(),
                                    self.txt_password.get()
                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registered Succesfully",parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

        




root=Tk()
obj=reg(root)
root.mainloop()       