from tkinter import*

class Bill_App:

    # Functionality part
    def total():
        print('asd')




    # GUI Part
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#fffe54"
        title = Label(self.root, text="Phần mềm thanh toán", bd=12, relief=GROOVE, bg=bg_color, fg="Black", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        #============= Khung chi tiết khách hàng
        F1 = LabelFrame(self.root, text="Chi tiết khách hàng", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text="Tên khách hàng", bg=bg_color, fg="Black", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1,width=20, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=5, pady=10)

        cphn_lbl = Label(F1,text="SĐT", bg=bg_color, fg="Black", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1,width=20, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=5, pady=10)

        c_bill_lbl = Label(F1,text="ID hóa đơn", bg=bg_color, fg="Black", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1,width=20, font="arial 15", bd=7, relief=SUNKEN).grid(row=0, column=5, padx=5, pady=10)

        bill_btn = Button(F1,text="Tìm kiếm", width=10, bd=9,  font=("arial 12 bold")).grid(row=0, column=6, padx=10, pady=10)
        
        #============= Khung chi tiết mỹ phẩm
        F2 = LabelFrame(self.root, text="Mỹ Phẩm", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F2.place(x=0,y=185,width=325, height=380)

        bath_lbl = Label(F2,text="Xà phòng tắm", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        face_cream_lbl = Label(F2,text="Dưỡng da mặt", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        face_cream_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        face_w_lbl = Label(F2,text="Sửa rửa mặt", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        face_w_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        Hair_s_lbl = Label(F2,text="Xịt tóc", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_s_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        hair_g_lbl = Label(F2,text="Sáp vuốt tóc", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        hair_g_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        body_lbl = Label(F2,text="Dưỡng thể", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        body_txt = Entry(F2,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #============= Khung chi tiết tạp hóa
        F3 = LabelFrame(self.root, text="Tạp hóa", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F3.place(x=339,y=185,width=325, height=380)

        g1_lbl = Label(F3,text="Gạo", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F3,text="Dầu ăn", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_w_lbl = Label(F3,text="Đậu", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F3,text="Thịt", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_s_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F3,text="Đường", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F3,text="Trà", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F3,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #============= Khung chi tiết nuoc
        F4 = LabelFrame(self.root, text="Nước", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F4.place(x=678,y=185,width=325, height=380)

        g1_lbl = Label(F4,text="Nước ngọt", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        g1_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)

        g2_lbl = Label(F4,text="Nước ép", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        g2_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)

        g3_w_lbl = Label(F4,text="Sữa", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        g3_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        g4_lbl = Label(F4,text="Rượu", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        g4_s_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        g5_lbl = Label(F4,text="Bia", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        g5_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        g6_lbl = Label(F4,text="Nước Suối", font=("times new roman", 16, "bold"), bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        g6_txt = Entry(F4,width=10, font=("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        #============= Khung chi tiết tạp hóa
        F5 = LabelFrame(self.root,bd=10, relief=GROOVE)
        F5.place(x=1017,y=185,width=325, height=380)
        bill_title = Label(F5, text="Hóa Đơn", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        #============= Các nút trong hóa đơn
        F6 = LabelFrame(self.root, text="Menu hóa đơn", bd=7, relief=GROOVE, font=("times new roman", 15, "bold"), fg="Black",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1, height=140)

        m1=Label(F6,text="Tổng giá mỹ phẩm",bg=bg_color, fg="Black",font=("times new roman", 15, "bold")).grid(row= 0, column=0, padx=20, pady=1, sticky="w")
        m1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=1)       
        
        m2=Label(F6,text="Tổng giá tạp hóa",bg=bg_color, fg="Black",font=("times new roman", 15, "bold")).grid(row= 1, column=0, padx=20, pady=1, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)       
        
        m3=Label(F6,text="Tổng giá nước",bg=bg_color, fg="Black",font=("times new roman", 15, "bold")).grid(row= 2, column=0, padx=20, pady=1, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=1)  


        c1=Label(F6,text="Thuế mỹ phẩm",bg=bg_color, fg="Black",font=("times new roman", 15, "bold")).grid(row= 0, column=2, padx=20, pady=1, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)       
        
        c2=Label(F6,text="Thuế tạp hóa",bg=bg_color, fg="Black",font=("times new roman", 15, "bold")).grid(row= 1, column=2, padx=20, pady=1, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=1)       
        
        c3=Label(F6,text="Thuế nước",bg=bg_color, fg="Black",font=("times new roman", 15, "bold")).grid(row= 2, column=2, padx=20, pady=1, sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=1)       
        
        btn_F= Frame(F6, bd=7,relief=GROOVE)
        btn_F.place(x=750, width=580, height=105)
        
        total_btn=Button(btn_F, text="Tổng", bg="cadetblue", fg="black", bd=2, pady=15, width=10, font="arial 11 bold").grid(row=0, column=0, padx=5, pady=5)
        GBill_btn=Button(btn_F, text="Tạo Hóa đơn", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold").grid(row=0, column=1, padx=5, pady=5)
        Clear_btn=Button(btn_F, text="Xóa", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold").grid(row=0, column=2, padx=5, pady=5)
        email_btn=Button(btn_F, text="Email", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold").grid(row=0, column=3, padx=5, pady=5)
        Exit_btn=Button(btn_F, text="Thoát", bg="cadetblue", fg="black",bd=2, pady=15, width=10, font="arial 11 bold").grid(row=0, column=4, padx=5, pady=5)

        
root = Tk()
obj = Bill_App(root)
root.mainloop()