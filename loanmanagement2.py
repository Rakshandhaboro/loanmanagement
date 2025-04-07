from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import math

class LoanManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Loan Management System')
        self.root.geometry('1350x720+0+0')
        self.root.configure(bg='#f0f0f0')
        
        # Title Label
        title = Label(self.root, text='Loan Management System',
                     font=('Helvetica', 35, 'bold'),
                     bg='#003366', fg='white', bd=10, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # Variables
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
        self.Status = StringVar()

        # Details Frame
        Detail_F = Frame(self.root, bd=4, relief=RIDGE, bg='white')
        Detail_F.place(x=10, y=90, width=520, height=620)

        lbls = ['Loan ID', 'Full Name', 'Loan Years', 'Interest Rate', 'Monthly Payment',
                'Total Payment', 'Aadhar Number', 'Address', 'Pincode', 'Loan Amount', 'Status']
        vars = [self.Loan_id, self.Name, self.Year, self.rate, self.monthly_payment,
                self.Total_payment, self.AadharNumber, self.Address, self.Pincode, self.Amount, self.Status]
        
        for i, (lbl, var) in enumerate(zip(lbls, vars)):
            Label(Detail_F, text=lbl, font=('Helvetica', 14, 'bold'), bg='white').grid(row=i, column=0, padx=20, pady=10, sticky='w')
            Entry(Detail_F, font=('Helvetica', 14), bd=3, relief=GROOVE, textvariable=var).grid(row=i, column=1)

        # Buttons
        Button(self.root, text='Loan Calculator', font='Helvetica 16 bold', bg='#009688', fg='white', command=self.open_calculator).place(x=10, y=720)
        Button(self.root, text='Submit Loan', font='Helvetica 16 bold', bg='#007BFF', fg='white', command=self.submit_loan).place(x=200, y=720)
        Button(self.root, text='Clear', font='Helvetica 16 bold', bg='#FF5722', fg='white', command=self.clear_fields).place(x=380, y=720)

    def open_calculator(self):
        calculator = Toplevel(self.root)
        calculator.title("Loan Calculator")
        calculator.geometry("400x300")
        Label(calculator, text="Loan Calculator", font=('Helvetica', 20, 'bold')).pack()
        
        def calculate():
            try:
                P = float(self.Amount.get())
                r = float(self.rate.get()) / 100 / 12
                n = int(self.Year.get()) * 12
                monthly_payment = P * (r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1) if r > 0 else P / n
                self.monthly_payment.set(f"{monthly_payment:.2f}")
                self.Total_payment.set(f"{monthly_payment * n:.2f}")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
        
        Button(calculator, text='Compute Payment', font='Helvetica 12 bold', bg='#4CAF50', fg='white', command=calculate).pack(pady=20)

    def submit_loan(self):
        messagebox.showinfo("Success", "Loan Submitted Successfully")

    def clear_fields(self):
        for var in [self.Loan_id, self.Name, self.Year, self.rate, self.monthly_payment,
                    self.Total_payment, self.AadharNumber, self.Address, self.Pincode, self.Amount, self.Status]:
            var.set("")

if __name__ == "__main__":
    root = Tk()
    app = LoanManagementSystem(root)
    root.mainloop()
