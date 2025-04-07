from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class Customer:
    def __init__(self, root):
        self.root = root
        self.root.title('Loan Management System')
        self.root.geometry('1350x720+0+0')
        
        # Title
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