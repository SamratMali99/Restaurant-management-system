from tkinter import *
from datetime import datetime
import random
from tkinter import messagebox
import sys
import mysql.connector

def main():
    top = Tk()
    lp = LoginPage(top)
    top.mainloop()

class LoginPage:
    def __init__ (self,top):
        self.top = top
        self.top.geometry("1700x800+0+0")
        self.top.configure(bg="#333333")
        self.top.title("Login Page")
        self.title_label = Label(self.top, text="Restaurant management system", font=('arial', 35, 'bold'), bg="purple")
        self.title_label.pack(side=TOP, fill=X)

        self.main_frame = Frame(self.top, bg="lightgray")
        self.main_frame.place(x=450, y=150,width=600,height=350)


        self.login_lb = Label(self.main_frame,text="Login",font=('arial',25,'bold'),bg="lightgray",fg="red")
        self.login_lb.place(x=270,y=10)

        username = StringVar()
        password = StringVar()

        self.user_lb = Label(self.main_frame,text="Username: ",font=("Times new roman",15),bg="lightgray",fg="red")
        self.user_lb.place(x=100, y=100)

        self.user_entry = Entry(self.main_frame, font=("arial",15),relief=GROOVE, textvariable=username)
        self.user_entry.place(x=200 ,y=100 )

        self.pwd_lb = Label(self.main_frame, text="Password: ", font=("Times new roman", 15), bg="lightgray",fg="red")
        self.pwd_lb.place(x=100, y=150)

        self.pwd_entry = Entry(self.main_frame, font=("arial",15),relief=GROOVE, textvariable=password,show="* ")
        self.pwd_entry.place(x=200, y=150)


        def check_login():
            if username.get() == "" and password.get() == "":
                messagebox.showinfo("Error", "Enter Username and password", parent=self.top)
            else:
                try:
                    connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                         database="res")
                    cur = connection.cursor()
                    cur.execute("select * from rest where username=%s and password=%s",
                                [(username.get()), (password.get())])
                    row = cur.fetchall()

                    if row:
                        billing_sect()

                    else:
                        messagebox.showerror("Error!", "Invalid USERNAME & PASSWORD", parent=self.top)

                        connection.close()

                except Exception as e:
                    messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.top)

        def sign_up():
            if username.get() == "" and password.get() == "":
                messagebox.showinfo("Error", "Enter Username and password", parent=self.top)
            else:
                try:
                    connection = mysql.connector.connect(host="localhost", user="root", password="",
                                                         database="res")
                    cur = connection.cursor()
                    cur.execute("insert into rest values(%s, %s);",
                                [(username.get()), (password.get())])

                    connection.commit()

                    connection.close()

                except Exception as e:
                    messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.top)

        def reset():
            username.set("")
            password.set("")

        def billing_sect():
            self.top2 = Toplevel(self.top)
            self.bp = BillingPage(self.top2)

        self.login_btn = Button(self.main_frame,text="Login",font=("Arial",12),command=check_login)
        self.login_btn.place(x=230,y=200)

        self.sign_up_btn = Button(self.main_frame,text="signup",font=("Arial",12),command=sign_up)
        self.sign_up_btn.place(x=300,y=200)

        self.reset_btn = Button(self.main_frame,text="Reset",font=("Arial",12),command=reset)
        self.reset_btn.place(x=370,y=200)


class BillingPage:
    def __init__(self,top):
        self.top =top
        self.top.geometry("1700x800+0+0")
        self.top.configure(bg="#333333")
        self.top.title("Billing Page")

        bill_no = random.randint(1000,9999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)


        cal_var = StringVar()

        cust_nm = StringVar()
        cust_conct = StringVar()
        date_pr = StringVar()
        item_pur =StringVar()
        item_qty =StringVar()
        cost_of_one =StringVar()

        date_pr.set(datetime.now())

        total_list = []
        self.grd_total = 0

        self.title_label = Label(self.top, text="Restaurant management system", font=('arial', 35, 'bold'), bg="purple")
        self.title_label.pack(side=TOP, fill=X)

        self.entry_frame = LabelFrame(self.top,text="Details",background="Lightgray",font=('Arial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20, y=95, width=550, height=650)

        self.bill_no_lb = Label(self.entry_frame,text="Bill Number: ",font=('Arial',15))
        self.bill_no_lb.grid(row=0, column=0,padx=2,pady=2)

        self.bill_no_entry = Entry(self.entry_frame,bd=5,textvariable=bill_no_tk, font=('Arial',15))
        self.bill_no_entry.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_entry.config(state=DISABLED)

        self.Custumer_name_lb = Label(self.entry_frame, text="Customer Name: ", font=('Arial', 15))
        self.Custumer_name_lb.grid(row=1, column=0, padx=2, pady=2)

        self.Custumer_name_entry = Entry(self.entry_frame, bd=5, textvariable=cust_nm, font=('Arial', 15))
        self.Custumer_name_entry.grid(row=1, column=1, padx=2, pady=2)

        self.Custumer_conct_lb = Label(self.entry_frame, text="Customer Contact: ", font=('Arial', 15))
        self.Custumer_conct_lb.grid(row=2, column=0, padx=2, pady=2)

        self.Custumer_conct_entry = Entry(self.entry_frame, bd=5, textvariable=cust_conct, font=('Arial', 15))
        self.Custumer_conct_entry.grid(row=2, column=1, padx=2, pady=2)

        self.Date_lb = Label(self.entry_frame, text="Date: ", font=('Arial', 15))
        self.Date_lb.grid(row=3, column=0, padx=2, pady=2)

        self.Date_entry = Entry(self.entry_frame, bd=5, textvariable=date_pr, font=('Arial', 15))
        self.Date_entry.grid(row=3, column=1, padx=2, pady=2)

        self.item_pur_lb = Label(self.entry_frame, text="Item name: ", font=('Arial', 15))
        self.item_pur_lb.grid(row=4, column=0, padx=2, pady=2)

        self.item_pur_entry = Entry(self.entry_frame, bd=5, textvariable=item_pur, font=('Arial', 15))
        self.item_pur_entry.grid(row=4, column=1, padx=2, pady=2)

        self.item_qunt_lb = Label(self.entry_frame, text="Item Quantity: ", font=('Arial', 15))
        self.item_qunt_lb.grid(row=5, column=0, padx=2, pady=2)

        self.item_qunt_entry = Entry(self.entry_frame, bd=5, textvariable=item_qty, font=('Arial', 15))
        self.item_qunt_entry.grid(row=5, column=1, padx=2, pady=2)

        self.cost_lb = Label(self.entry_frame, text="Cost of One: ", font=('Arial', 15))
        self.cost_lb.grid(row=6, column=0, padx=2, pady=2)

        self.cost_entry = Entry(self.entry_frame, bd=5, textvariable=cost_of_one, font=('Arial', 15))
        self.cost_entry.grid(row=6, column=1, padx=2, pady=2)

        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\tAswaad Restaurant")
            self.bill_txt.insert(END,"\n\t\t\t 7 street, Near railway sattion")
            self.bill_txt.insert(END,"\n\t\t\t\tContact = 9623XXXXXX")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,f"\nBill Number: {bill_no_tk.get()}")

        def genbill():
            if cust_nm.get() == "" or (cust_conct.get() == "" or len(cust_conct.get()) != 10):
                messagebox.showerror("Error","Please enter the detail correctly",parent=self.top)
            else:
                self.bill_txt.insert(END,f"\nCustumer Name: {cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustumer Contact: {cust_conct.get()}")
                self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
                self.bill_txt.insert(END,"\n=================================================================================")
                self.bill_txt.insert(END,"\n\tProduct Name \t\t    Quantity\t\t   Per cost\t\t   Total")
                self.bill_txt.insert(END,"\n=================================================================================")

                self.add_btn.config(state=NORMAL)
                self.total_btn.config(state=NORMAL)


        def clear_func():
            cust_nm.set("")
            cust_conct.set("")
            item_pur.set("")
            item_qty.set("")
            cost_of_one.set("")

        def reset_func():
            total_list.clear()
            self.grd_total = 0
            self.add_btn.config(state=DISABLED)
            self.total_btn.config(state=DISABLED)
            self.save_btn.config(state=DISABLED)
            self.bill_txt.delete("1.0",END)
            default_bill()

        def add_func():
            if item_pur.get() == "" or item_qty.get() == "":
                 messagebox.showerror("Error","Please enter all details correctly.",parent=self.top)
            else:
                qty = int(item_qty.get())
                cost_of_ones = int(cost_of_one.get())
                total = qty * cost_of_ones
                total_list.append(total)
                self.bill_txt.insert(END,f"\n\t{item_pur.get()} \t\t    {item_qty.get()}\t\t   {cost_of_one.get()}\t\t   Rs.{total}")


        def total_func():
            for item in total_list:
                self.grd_total =self.grd_total + item
            self.bill_txt.insert(END,"\n=================================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t              Total : {self.grd_total}")
            self.bill_txt.insert(END,"\n=================================================================================")
            self.save_btn.config(state=NORMAL)

        def save_fucn():
            user_choice = messagebox.askyesno("Comfirm?",f"Do you want to save bill {bill_no_tk.get()}",parent=self.top)
            if user_choice > 0 :
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                    con = open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error",f"Error due to {e}",parent=self.top)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success",f"Bill {bill_no_tk.get()} has been saved Sucessfully!",parent=self.top)

            else:
                return

        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Option",bg="lightgray",font=('Arial',15))
        self.button_frame.place(x=20, y=280, width= 390, height=300)

        self.add_btn = Button(self.button_frame, bd=2,text="Add",font=('Arial',12),width=12, height=3,command=add_func)
        self.add_btn.grid(row=0, column=0, padx=4,pady=2)

        self.generate_btn = Button(self.button_frame, bd=2,text="Generate",font=('Arial',12),width=12, height=3,command=genbill)
        self.generate_btn.grid(row=0, column=1, padx=4,pady=2)

        self.clear_btn = Button(self.button_frame, bd=2,text="Clear",font=('Arial',12),width=12, height=3,command=clear_func)
        self.clear_btn.grid(row=0, column=2, padx=4,pady=2)

        self.total_btn = Button(self.button_frame, bd=2, text="Total", font=('Arial', 12), width=12, height=3,command=total_func)
        self.total_btn.grid(row=1, column=0, padx=4, pady=2)

        self.reset_btn = Button(self.button_frame, bd=2, text="Reset", font=('Arial', 12), width=12, height=3,command=reset_func)
        self.reset_btn.grid(row=1, column=1, padx=4, pady=2)
        
        self.save_btn = Button(self.button_frame, bd=2, text="Save", font=('Arial', 12), width=12, height=3,command=save_fucn)
        self.save_btn.grid(row=1, column=2, padx=4, pady=2)

        self.add_btn.config(state=DISABLED)
        self.total_btn.config(state=DISABLED)
        self.save_btn.config(state=DISABLED)

        self.cal_frame = Frame(self.top,bd=8,background="lightgray",relief=GROOVE)
        self.cal_frame.place(x=650,y=90,width=720,height=315)

        self.num_entry = Entry(self.cal_frame,bd=15,background="lightgray",textvariable=cal_var,font=('Arial',15),width=60,justify='right')
        self.num_entry.grid(row=0,column=0,columnspan=4)

        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                if cal_var.get().isdigit():
                    value = int(cal_var.get())
                else:
                    try:
                        value = eval(self.num_entry.get())
                    except:
                        print("Error")
                    cal_var.set(value)
                    self.num_entry.update()
            else:
                cal_var.set(cal_var.get() + text)
                self.num_entry.update()

        self.cal_btn1 = Button(self.cal_frame,bg="lightgray",text="1",bd=8,width=15,height=2)
        self.cal_btn1.grid(row=1,column=0, padx=2, pady=2)
        self.cal_btn1.bind("<Button-1>",press_btn)

        self.cal_btn2 = Button(self.cal_frame, bg="lightgray", text="2", bd=8, width=15, height=2)
        self.cal_btn2.grid(row=1, column=1, padx=2, pady=2)
        self.cal_btn2.bind("<Button-1>", press_btn)

        self.cal_btn3 = Button(self.cal_frame, bg="lightgray", text="3", bd=8, width=15, height=2)
        self.cal_btn3.grid(row=1, column=2, padx=2, pady=2)
        self.cal_btn3.bind("<Button-1>", press_btn)

        self.cal_btn_add = Button(self.cal_frame, bg="lightgray", text="+", bd=8, width=15, height=2)
        self.cal_btn_add.grid(row=1, column=3, padx=2, pady=2)
        self.cal_btn_add.bind("<Button-1>", press_btn)

        self.cal_btn4 = Button(self.cal_frame, bg="lightgray", text="4", bd=8, width=15, height=2)
        self.cal_btn4.grid(row=2, column=0, padx=2, pady=2)
        self.cal_btn4.bind("<Button-1>", press_btn)

        self.cal_btn5 = Button(self.cal_frame, bg="lightgray", text="5", bd=8, width=15, height=2)
        self.cal_btn5.grid(row=2, column=1, padx=2, pady=2)
        self.cal_btn5.bind("<Button-1>", press_btn)

        self.cal_btn6 = Button(self.cal_frame, bg="lightgray", text="6", bd=8, width=15, height=2)
        self.cal_btn6.grid(row=2, column=2, padx=2, pady=2)
        self.cal_btn6.bind("<Button-1>", press_btn)

        self.cal_btn_sub = Button(self.cal_frame, bg="lightgray", text="-", bd=8, width=15, height=2)
        self.cal_btn_sub.grid(row=2, column=3, padx=2, pady=2)
        self.cal_btn_sub.bind("<Button-1>", press_btn)

        self.cal_btn7 = Button(self.cal_frame, bg="lightgray", text="7", bd=8, width=15, height=2)
        self.cal_btn7.grid(row=3, column=0, padx=2, pady=2)
        self.cal_btn7.bind("<Button-1>", press_btn)

        self.cal_btn8 = Button(self.cal_frame, bg="lightgray", text="8", bd=8, width=15, height=2)
        self.cal_btn8.grid(row=3, column=1, padx=2, pady=2)
        self.cal_btn8.bind("<Button-1>", press_btn)

        self.cal_btn9 = Button(self.cal_frame, bg="lightgray", text="9", bd=8, width=15, height=2)
        self.cal_btn9.grid(row=3, column=2, padx=2, pady=2)
        self.cal_btn9.bind("<Button-1>", press_btn)

        self.cal_btn_mul = Button(self.cal_frame, bg="lightgray", text="*", bd=8, width=15, height=2)
        self.cal_btn_mul.grid(row=3, column=3, padx=2, pady=2)
        self.cal_btn_mul.bind("<Button-1>", press_btn)

        self.cal_btn0 = Button(self.cal_frame, bg="lightgray", text="0", bd=8, width=15, height=2)
        self.cal_btn0.grid(row=4, column=0, padx=2, pady=2)
        self.cal_btn0.bind("<Button-1>", press_btn)

        self.cal_btn_dot = Button(self.cal_frame, bg="lightgray", text=".", bd=8, width=15, height=2)
        self.cal_btn_dot.grid(row=4, column=1, padx=2, pady=2)
        self.cal_btn_dot.bind("<Button-1>", press_btn)

        self.cal_btn_eql = Button(self.cal_frame, bg="lightgray", text="=", bd=8, width=15, height=2)
        self.cal_btn_eql.grid(row=4, column=2, padx=2, pady=2)
        self.cal_btn_eql.bind("<Button-1>", press_btn)

        self.cal_btn_div = Button(self.cal_frame, bg="lightgray", text="/", bd=8, width=15, height=2)
        self.cal_btn_div.grid(row=4, column=3, padx=2, pady=2)
        self.cal_btn_div.bind("<Button-1>", press_btn)

        self.bill_frame = LabelFrame(self.top,text="Bill Area",font=('Arial',20),background="lightgray",bd=8,relief=GROOVE)
        self.bill_frame.place(x=685, y=430, width=690,height=330 )

        self.y_scroll = Scrollbar(self.bill_frame,orient="vertical")
        self.bill_txt = Text(self.bill_frame,bg="White",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.bill_txt.pack(fill=BOTH, expand=TRUE)

        default_bill()


main()