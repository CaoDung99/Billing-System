from tkinter import *
from datetime import datetime
import pytz
import tkinter as tk

class BillingView:
    def __init__(self, root, controller):
        self.root = root
        self.root.geometry("1450x700+0+0")
        icon_path = "./on2.ico"
        self.root.iconbitmap(icon_path)
        self.root.title("Billing Software")
        bg_color = "#B8E1FF"

        # Tạo label frame và đặt vị trí
        F0 = LabelFrame(self.root, bd=12, relief=GROOVE, font=("times new roman", 40, "bold"), fg="Black", bg=bg_color,
                        pady=2)
        F0.place(x=0, y=0, relwidth=1)

        # Tạo label "Phần mềm thanh toán" và căn giữa
        self.title_lbl = Label(F0, text="Phần mềm thanh toán", bg=bg_color, fg="Black",
                               font=("times new roman", 18, "bold"))
        self.title_lbl.grid(row=0, column=0, padx=20, pady=5, columnspan=3)

        self.time_txt = Entry(F0, width=20, font="arial 15", bd=7, relief=SUNKEN)
        self.time_txt.grid(row=0, column=3, padx=5, pady=10)
        self.time_txt.config(state='disabled')

        self.controller = controller
        self.update_time()

        #============= Khung chi tiết khách hàng
        F1 = LabelFrame(self.root, text="Chi tiết khách hàng", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        self.cname_lbl = Label(F1,text="Tên khách hàng", bg=bg_color, fg="Black", font=("times new roman", 18, "bold"))
        self.cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        self.cname_txt = Entry(F1,width=20, font="arial 15", bd=7, relief=SUNKEN)
        self.cname_txt.grid(row=0, column=1, padx=5, pady=10)

        self.cphn_lbl = Label(F1,text="SĐT", bg=bg_color, fg="Black", font=("times new roman", 18, "bold"))
        self.cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        self.cphn_txt = Entry(F1,width=20, font="arial 15", bd=7, relief=SUNKEN)
        self.cphn_txt.grid(row=0, column=3, padx=5, pady=10)

        self.c_bill_lbl = Label(F1,text="ID hóa đơn", bg=bg_color, fg="Black", font=("times new roman", 18, "bold"))
        self.c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        self.c_bill_txt = Entry(F1,width=20, font="arial 15", bd=7, relief=SUNKEN)
        self.c_bill_txt.grid(row=0, column=5, padx=5, pady=10)

        self.bill_btn = Button(F1,text="Tìm kiếm", width=10, bd=9,  font=("arial 12 bold"), command= controller.search_bill)
        self.bill_btn.grid(row=0, column=6, padx=10, pady=10)
        
        #============= Khung chi tiết Món khai vị
        F2 = LabelFrame(self.root, text="Món khai vị", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F2.place(x=0,y=185,width=325, height=380)

       

        self.bath_lbl = Label(F2, text="Gỏi cuốn", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.bath_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.bath_txt = Entry(F2, width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.bath_txt.insert(0,0)
        self.bath_txt.grid(row=0, column=1, padx=10, pady=10)

        self.face_cream_lbl = Label(F2,text="Cá sốt me", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.face_cream_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.face_cream_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.face_cream_txt.insert(0,0)
        self.face_cream_txt.grid(row=1, column=1, padx=10, pady=10)

        self.face_w_lbl = Label(F2,text="Bò tái chanh", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.face_w_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.face_w_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.face_w_txt.insert(0,0)
        self.face_w_txt.grid(row=2, column=1, padx=10, pady=10)

        self.Hair_s_lbl = Label(F2,text="Gà rang muối", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.Hair_s_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.Hair_s_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.Hair_s_txt.insert(0,0)
        self.Hair_s_txt.grid(row=3, column=1, padx=10, pady=10)

        self.hair_g_lbl = Label(F2,text="Cơm gà Hainan", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.hair_g_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.hair_g_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.hair_g_txt.insert(0,0)
        self.hair_g_txt.grid(row=4, column=1, padx=10, pady=10)

        self.body_lbl = Label(F2,text="Mì xào hải sản", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.body_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.body_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.body_txt.insert(0,0)
        self.body_txt.grid(row=5, column=1, padx=10, pady=10)

        #============= Khung chi tiết Món Lẩu
        F3 = LabelFrame(self.root, text="Lẩu", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F3.place(x=339,y=185,width=325, height=380)

        self.g1_lbl = Label(F3,text="Lẩu Thái", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.g1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.g1_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g1_txt.insert(0,0)
        self.g1_txt.grid(row=0, column=1, padx=10, pady=10)

        self.g2_lbl = Label(F3,text="Lẩu Sichuan", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.g2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.g2_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g2_txt.insert(0,0)
        self.g2_txt.grid(row=1, column=1, padx=10, pady=10)

        self.g3_w_lbl = Label(F3,text="Lẩu Kim Chi", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.g3_w_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.g3_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g3_txt.insert(0,0)
        self.g3_txt.grid(row=2, column=1, padx=10, pady=10)

        self.g4_lbl = Label(F3,text="Lẩu Miso", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.g4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.g4_s_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g4_s_txt.insert(0,0)
        self.g4_s_txt.grid(row=3, column=1, padx=10, pady=10)

        self.g5_lbl = Label(F3,text="Lẩu riêu cua", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.g5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.g5_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g5_txt.insert(0,0)
        self.g5_txt.grid(row=4, column=1, padx=10, pady=10)

        self.g6_lbl = Label(F3,text="Lẩu đuôi bò", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.g6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.g6_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.g6_txt.insert(0,0)
        self.g6_txt.grid(row=5, column=1, padx=10, pady=10)

        #============= Khung chi tiết Món Nước Uống
        F4 = LabelFrame(self.root, text="Nước Uống", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F4.place(x=678,y=185,width=325, height=380)

        self.n1_lbl = Label(F4,text="Nước ép trái cây", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.n1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.n1_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.n1_txt.insert(0,0)
        self.n1_txt.grid(row=0, column=1, padx=10, pady=10)

        self.n2_lbl = Label(F4,text="Nước ngọt", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.n2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.n2_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.n2_txt.insert(0,0)
        self.n2_txt.grid(row=1, column=1, padx=10, pady=10)

        self.n3_w_lbl = Label(F4,text="Sữa", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.n3_w_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.n3_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.n3_txt.insert(0,0)
        self.n3_txt.grid(row=2, column=1, padx=10, pady=10)

        self.n4_lbl = Label(F4,text="Rượu", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.n4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.n4_s_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.n4_s_txt.insert(0,0)
        self.n4_s_txt.grid(row=3, column=1, padx=10, pady=10)

        self.n5_lbl = Label(F4,text="Bia", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.n5_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.n5_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.n5_txt.insert(0,0)
        self.n5_txt.grid(row=4, column=1, padx=10, pady=10)

        self.n6_lbl = Label(F4,text="Nước Suối", font=("times new roman", 16, "bold"), bg=bg_color, fg="black")
        self.n6_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.n6_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN)
        self.n6_txt.insert(0,0)
        self.n6_txt.grid(row=5, column=1, padx=10, pady=10)

        #============= Khung chi Hóa đơn
        F5 = LabelFrame(self.root,bd=10, relief=GROOVE)
        F5.place(x=1017,y=185,width=430, height=380)
        bill_title = Label(F5, text="Hóa Đơn", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #============= Các nút trong hóa đơn
        F6 = LabelFrame(self.root, text="Menu hóa đơn", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1, height=140)

        self.m1=Label(F6,text="Tổng giá Khai Vị",bg=bg_color, fg="Black",font=("times new roman", 15, "bold"))
        self.m1.grid(row= 0, column=0, padx=20, pady=1, sticky="w")
        self.m1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN)
        self.m1_txt.grid(row=0, column=1, padx=10, pady=1)       
        
        self.m2=Label(F6,text="Tổng giá Lẩu",bg=bg_color, fg="Black",font=("times new roman", 15, "bold"))
        self.m2.grid(row= 1, column=0, padx=20, pady=1, sticky="w")
        self.m2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN)
        self.m2_txt.grid(row=1, column=1, padx=10, pady=1)       
        
        self.m3=Label(F6,text="Tổng giá Nước",bg=bg_color, fg="Black",font=("times new roman", 15, "bold"))
        self.m3.grid(row= 2, column=0, padx=20, pady=1, sticky="w")
        self.m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN)
        self.m3_txt.grid(row=2, column=1, padx=10, pady=1)  


        self.c1=Label(F6,text="Thuế món khai vị",bg=bg_color, fg="Black",font=("times new roman", 15, "bold"))
        self.c1.grid(row= 0, column=2, padx=20, pady=1, sticky="w")
        self.c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN)
        self.c1_txt.grid(row=0, column=3, padx=10, pady=1)       
        
        self.c2=Label(F6,text="Thuế món chính",bg=bg_color, fg="Black",font=("times new roman", 15, "bold"))
        self.c2.grid(row= 1, column=2, padx=20, pady=1, sticky="w")
        self.c2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN)
        self.c2_txt.grid(row=1, column=3, padx=10, pady=1)       
        
        self.c3=Label(F6,text="Thuế nước",bg=bg_color, fg="Black",font=("times new roman", 15, "bold"))
        self.c3.grid(row= 2, column=2, padx=20, pady=1, sticky="w")
        self.c3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN)
        self.c3_txt.grid(row=2, column=3, padx=10, pady=1)       
        
        btn_F= Frame(F6, bd=7,relief=GROOVE)
        btn_F.place(x=750, width=680, height=105)
        
        self.total_btn=Button(btn_F, text="Tổng", bg="cadetblue", fg="black", bd=2, pady=15, width=10, font="arial 11 bold", command= controller.total).grid(row=0, column=0, padx=5, pady=5)
        self.GBill_btn=Button(btn_F, text="Tạo Hóa đơn", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold", command= controller.txtarea).grid(row=0, column=1, padx=5, pady=5)
        self.Clear_btn=Button(btn_F, text="Xóa", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold", command=controller.delete_bill).grid(row=0, column=2, padx=5, pady=5)
        self.Print_btn=Button(btn_F, text="In Hóa Đơn", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold",command=controller.print_bill).grid(row=0, column=3, padx=5, pady=5)
        self.email_btn=Button(btn_F, text="Email", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold", command=controller.email_bill).grid(row=0, column=4, padx=5, pady=5)
        self.Exit_btn=Button(btn_F, text="Thoát", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold", command=controller.exit_app).grid(row=0, column=5, padx=5, pady=5)


    def update_time(self):
        vn_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
        current_time = datetime.now(tz=vn_timezone).strftime("%H:%M:%S %d/%m/%Y")
        self.time_txt.config(state='normal')
        self.time_txt.delete(0, tk.END)
        self.time_txt.insert(0, current_time)
        self.time_txt.config(state='disabled')
        self.root.after(1000, self.update_time)