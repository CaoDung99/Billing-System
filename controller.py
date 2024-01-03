from tkinter import messagebox
from model import BillingModel
from view import BillingView
from tkinter import *

class BillingController:
    def __init__(self):
        self.model = BillingModel()
        self.root = Tk()
        self.view = BillingView(self.root, self)

    def total(self):
        self.model.calculate_total(self.view)
        messagebox.showinfo("Thông báo", "Tính toán hoàn tất!")

    def txtarea(self):
        self.model.bill_area(self.view)

    def search_bill(self):
        self.model.search_bill(self.view)

    def print_bill(self):
        self.model.print_bill(self.view)
    def google_drive(self):
        self.model.google_drive(self.view)

    def delete_bill(self):
        self.model.delete_bill(self.view)

    def exit_app(self):
        self.model.exit_app(self.view)
        
    def run(self):
        self.root.mainloop()

controller = BillingController()
controller.run()