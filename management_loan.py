from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title('Loan Management System')
        self.root.geometry('1350x720+0+0')
        
        # Title Label
        title = Label(self.root, text='Loan Management System',
                     font=('times new roman', 40, 'bold'),
                     bg='blue', fg='gold', bd=10, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # =====================================Variables=============================================
        self.Loan_id = StringVar()
        self.Name = StringVar()
        self.Year = StringVar()
        self.rate = StringVar()
        self.monthly_payment = StringVar()
        self.Total_payment = StringVar()
        self.AadharNumber = StringVar()
        self.Address = StringVar()
        self.Pincode = StringVar()
        self.Amount = StringVar()

        # ==========================Details Frame===========================
        Detail_F = Frame(self.root, bd=4, relief=RIDGE, bg='powderblue')
        Detail_F.place(x=10, y=90, width=520, height=620)

        lbl_id = Label(Detail_F, text='Loan Id', font=('times new roman', 15, 'bold'))
        lbl_id.grid(row=0, column=0, padx=20, pady=10, sticky='w')
        txt_id = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Loan_id)
        txt_id.grid(row=0, column=1)

        lbl_name = Label(Detail_F, text='Full Name', font=('times new roman', 15, 'bold'))
        lbl_name.grid(row=1, column=0, padx=20, pady=10, sticky='w')
        txt_name = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Name)
        txt_name.grid(row=1, column=1)

        lbl_year = Label(Detail_F, text="Loan Years", font=('times new roman', 15, 'bold'))
        lbl_year.grid(row=2, column=0, pady=10, padx=20, sticky='w')
        txt_year = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Year)
        txt_year.grid(row=2, column=1)

        lbl_rate = Label(Detail_F, text="Interest Rate", font=('times new roman', 15, 'bold'))
        lbl_rate.grid(row=3, column=0, pady=10, padx=20, sticky='w')
        txt_rate = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.rate)
        txt_rate.grid(row=3, column=1)

        lbl_mpay = Label(Detail_F, text="Monthly Payment", font=('times new roman', 15, 'bold'))
        lbl_mpay.grid(row=4, column=0, pady=10, padx=20, sticky='w')
        txt_mpay = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.monthly_payment)
        txt_mpay.grid(row=4, column=1)

        lbl_tpay = Label(Detail_F, text="Total Payment", font=('times new roman', 15, 'bold'))
        lbl_tpay.grid(row=5, column=0, pady=10, padx=20, sticky='w')
        txt_tpay = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Total_payment)
        txt_tpay.grid(row=5, column=1)

        lbl_aadhar = Label(Detail_F, text="Aadhar Number", font=('times new roman', 15, 'bold'))
        lbl_aadhar.grid(row=6, column=0, pady=10, padx=20, sticky='w')
        txt_aadhar = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.AadharNumber)
        txt_aadhar.grid(row=6, column=1)

        lbl_add = Label(Detail_F, text="Address", font=('times new roman', 15, 'bold'))
        lbl_add.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        txt_add = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Address)
        txt_add.grid(row=7, column=1)

        lbl_pin = Label(Detail_F, text="Pincode", font=('times new roman', 15, 'bold'))
        lbl_pin.grid(row=8, column=0, pady=10, padx=20, sticky='w')
        txt_pin = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Pincode)
        txt_pin.grid(row=8, column=1)

        lbl_amt = Label(Detail_F, text="Loan Amount", font=('times new roman', 15, 'bold'))
        lbl_amt.grid(row=9, column=0, pady=10, padx=20, sticky='w')
        txt_amt = Entry(Detail_F, font=('times new roman', 15, 'bold'), bd=3, relief=GROOVE, textvariable=self.Amount)
        txt_amt.grid(row=9, column=1)

        # =========================Right Frame===============================
        RFrame = Frame(self.root, bd=4, relief=RIDGE, bg='powderblue')
        RFrame.place(x=540, y=90, width=800, height=620)

        yscroll = Scrollbar(RFrame, orient=VERTICAL)
        self.customer_table = ttk.Treeview(RFrame, columns=(
            "Loan_id", "Name", "Year", "rate", "monthly_payment", 
            "Total_payment", "AadharNumber", "Address", "Pincode", "Amount"
        ), yscrollcommand=yscroll.set)
        
        yscroll.pack(side=RIGHT, fill=Y)
        yscroll.config(command=self.customer_table.yview)
        
        self.customer_table.heading("Loan_id", text="Loan ID")
        self.customer_table.heading("Name", text="Name")
        self.customer_table.heading("Year", text="Years")
        self.customer_table.heading("rate", text="Rate")
        self.customer_table.heading("monthly_payment", text="Monthly Pay")
        self.customer_table.heading("Total_payment", text="Total Pay")
        self.customer_table.heading("AadharNumber", text="Aadhar No")
        self.customer_table.heading("Address", text="Address")
        self.customer_table.heading("Pincode", text="Pincode")
        self.customer_table.heading("Amount", text="Amount")
        
        self.customer_table['show'] = 'headings'
        
        self.customer_table.column("Loan_id", width=80)
        self.customer_table.column("Name", width=120)
        self.customer_table.column("Year", width=60)
        self.customer_table.column("rate", width=60)
        self.customer_table.column("monthly_payment", width=100)
        self.customer_table.column("Total_payment", width=100)
        self.customer_table.column("AadharNumber", width=120)
        self.customer_table.column("Address", width=150)
        self.customer_table.column("Pincode", width=80)
        self.customer_table.column("Amount", width=100)
        
        self.customer_table.pack(fill=BOTH, expand=1)
        self.fetch()
        self.customer_table.bind("<ButtonRelease-1>", self.get_cursor)

        # =========================Buttom Frame===========================
        btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='powderblue')
        btn_Frame.place(x=535, y=610, width=800, height=100)

        btn1 = Button(btn_Frame, text='Add record', font='arial 18 bold', width=9, bg='lime', fg='crimson', command=self.addrecord)
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = Button(btn_Frame, text='Update', font='arial 18 bold', width=9, bg='lime', fg='crimson', command=self.update)
        btn2.grid(row=0, column=1, padx=10, pady=10)

        btn3 = Button(btn_Frame, text='Delete', font='arial 18 bold', bg='lime', fg='crimson', width=9, command=self.delete)
        btn3.grid(row=0, column=2, padx=8, pady=10)

        btn4 = Button(btn_Frame, text='Reset', font='arial 18 bold', bg='lime', fg='crimson', width=9, command=self.reset)
        btn4.grid(row=0, column=3, padx=8, pady=10)

        btn5 = Button(btn_Frame, text='Exit', font='arial 18 bold', bg='lime', fg='crimson', width=9, command=self.exit)
        btn5.grid(row=0, column=4, padx=8, pady=10)

    # ================================Functions===================================
    def total(self):
        try:
            amount = float(self.Amount.get())
            rate = float(self.rate.get())
            years = float(self.Year.get())
            
            # Simple interest calculation
            total_interest = (amount * rate * years) / 100
            total_payment = amount + total_interest
            monthly_payment = total_payment / (years * 12)
            
            self.monthly_payment.set(f"{monthly_payment:.2f}")
            self.Total_payment.set(f"{total_payment:.2f}")
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers for amount, rate, and years')

    def addrecord(self):
        if self.Loan_id.get() == '' or self.Name.get() == '':
            messagebox.showerror('Error', 'Loan ID and Name are required')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', 
                                     password='', database='emp')
                cursor = con.cursor()
                
                # Check if Loan ID already exists
                cursor.execute("SELECT * FROM customer WHERE Loan_id=%s", (self.Loan_id.get(),))
                if cursor.fetchone() is not None:
                    messagebox.showerror('Error', 'Loan ID already exists')
                    return
                
                # Calculate payments
                self.total()
                
                # Insert new record
                cursor.execute("""
                    INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (
                    self.Loan_id.get(),
                    self.Name.get(),
                    self.Year.get(),
                    self.rate.get(),
                    self.monthly_payment.get(),
                    self.Total_payment.get(),
                    self.AadharNumber.get(),
                    self.Address.get(),
                    self.Pincode.get(),
                    self.Amount.get()
                ))
                
                con.commit()
                self.fetch()
                messagebox.showinfo('Success', 'Record added successfully')
            except pymysql.Error as e:
                messagebox.showerror('Database Error', f'Error: {str(e)}')
            finally:
                if 'con' in locals() and con.open:
                    con.close()

    def fetch(self):
        try:
            con = pymysql.connect(host='localhost', user='root', 
                                 password='', database='emp')
            cursor = con.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            
            self.customer_table.delete(*self.customer_table.get_children())
            for row in rows:
                self.customer_table.insert('', END, values=row)
        except pymysql.Error as e:
            messagebox.showerror('Database Error', f'Error: {str(e)}')
        finally:
            if 'con' in locals() and con.open:
                con.close()

    def get_cursor(self, ev):
        cursor_row = self.customer_table.focus()
        content = self.customer_table.item(cursor_row)
        row = content['values']
        
        if row:
            self.Loan_id.set(row[0])
            self.Name.set(row[1])
            self.Year.set(row[2])
            self.rate.set(row[3])
            self.monthly_payment.set(row[4])
            self.Total_payment.set(row[5])
            self.AadharNumber.set(row[6])
            self.Address.set(row[7])
            self.Pincode.set(row[8])
            self.Amount.set(row[9])

    def update(self):
        if self.Loan_id.get() == '':
            messagebox.showerror('Error', 'Select a record to update')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', 
                                     password='', database='emp')
                cursor = con.cursor()
                
                # Recalculate payments before updating
                self.total()
                
                cursor.execute("""
                    UPDATE customer SET 
                    Name=%s, Year=%s, rate=%s, monthly_payment=%s, 
                    Total_payment=%s, AadharNumber=%s, Address=%s, 
                    Pincode=%s, Amount=%s
                    WHERE Loan_id=%s
                    """, (
                    self.Name.get(),
                    self.Year.get(),
                    self.rate.get(),
                    self.monthly_payment.get(),
                    self.Total_payment.get(),
                    self.AadharNumber.get(),
                    self.Address.get(),
                    self.Pincode.get(),
                    self.Amount.get(),
                    self.Loan_id.get()
                ))
                
                con.commit()
                self.fetch()
                messagebox.showinfo('Success', 'Record updated successfully')
            except pymysql.Error as e:
                messagebox.showerror('Database Error', f'Error: {str(e)}')
            finally:
                if 'con' in locals() and con.open:
                    con.close()

    def delete(self):
        if self.Loan_id.get() == '':
            messagebox.showerror('Error', 'Select a record to delete')
        else:
            if messagebox.askyesno('Confirm', 'Are you sure you want to delete this record?'):
                try:
                    con = pymysql.connect(host='localhost', user='root', 
                                         password='', database='emp')
                    cursor = con.cursor()
                    cursor.execute("DELETE FROM customer WHERE Loan_id=%s", (self.Loan_id.get(),))
                    con.commit()
                    self.fetch()
                    self.reset()
                    messagebox.showinfo('Success', 'Record deleted successfully')
                except pymysql.Error as e:
                    messagebox.showerror('Database Error', f'Error: {str(e)}')
                finally:
                    if 'con' in locals() and con.open:
                        con.close()

    def reset(self):
        self.Loan_id.set('')
        self.Name.set('')
        self.Year.set('')
        self.rate.set('')
        self.monthly_payment.set('')
        self.Total_payment.set('')
        self.AadharNumber.set('')
        self.Address.set('')
        self.Pincode.set('')
        self.Amount.set('')

    def exit(self):
        if messagebox.askyesno('Exit', 'Do you really want to exit?'):
            self.root.destroy()

root = Tk()
obj = Customer(root)
root.mainloop()