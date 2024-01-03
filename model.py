import io
import os
import random
from view import BillingView
from tkinter import messagebox
from tkinter import END
from tkinter import *
import glob
from io import StringIO

class BillingModel:
    def calculate_total(self, billing_view_instance):
        global soapprice, facecreamprice, facewashprice, hairprayprice, hairgelpirece, bodylotionprice, riceprice, daalprice, oilprice, sugarprice, teaprice, wheatprice, maaprice, frootprice, dewprice, pepsiprice, spriteprice, cococolaprice
        global totalcosmeticprice, cosmetictax, totalgroceyprice, procerytax, totaldrinkprice, drinktax, totalbill
        soapprice = int(billing_view_instance.bath_txt.get()) *20
        facecreamprice = int(billing_view_instance.face_cream_txt.get()) *50
        facewashprice = int(billing_view_instance.face_w_txt.get()) *100
        hairprayprice = int(billing_view_instance.Hair_s_txt.get()) *150
        hairgelpirece = int(billing_view_instance.hair_g_txt.get()) *180
        bodylotionprice = int(billing_view_instance.body_txt.get()) *60
        
        
        totalcosmeticprice = soapprice + facecreamprice + facewashprice + hairprayprice + hairgelpirece + bodylotionprice
        billing_view_instance.m1_txt.delete(0,END)
        billing_view_instance.m1_txt.insert(0, f'{totalcosmeticprice} vnđ')


        cosmetictax = totalcosmeticprice*0.12
        billing_view_instance.c1_txt.delete(0, END)
        billing_view_instance.c1_txt.insert(0,str(cosmetictax) + 'vnđ')  
        


        riceprice = int(billing_view_instance.g1_txt.get()) *30
        daalprice = int(billing_view_instance.g2_txt.get()) *100
        oilprice = int(billing_view_instance.g3_txt.get()) *120
        sugarprice = int(billing_view_instance.g4_s_txt.get()) *50
        teaprice = int(billing_view_instance.g5_txt.get()) *140
        wheatprice = int(billing_view_instance.g6_txt.get()) *80
        
        
        totalgroceyprice = riceprice + daalprice + oilprice + sugarprice + teaprice + wheatprice
        billing_view_instance.m2_txt.delete(0,END)
        billing_view_instance.m2_txt.insert(0,f'{totalgroceyprice} vnđ')  


        procerytax = totalgroceyprice*0.05
        billing_view_instance.c2_txt.delete(0, END)
        billing_view_instance.c2_txt.insert(0,str(procerytax) + 'vnđ')  


        maaprice = int(billing_view_instance.n1_txt.get()) *50
        frootprice = int(billing_view_instance.n2_txt.get()) *20
        dewprice = int(billing_view_instance.n3_txt.get()) *30
        pepsiprice = int(billing_view_instance.n4_s_txt.get()) *20
        spriteprice = int(billing_view_instance.n5_txt.get()) *45
        cococolaprice = int(billing_view_instance.n6_txt.get()) *90
        
        
        totaldrinkprice = maaprice + frootprice + dewprice + pepsiprice + spriteprice + cococolaprice
        billing_view_instance.m3_txt.delete(0,END)
        billing_view_instance.m3_txt.insert(0, f'{totaldrinkprice} vnđ')

        drinktax = totaldrinkprice*0.08
        billing_view_instance.c3_txt.delete(0, END)
        billing_view_instance.c3_txt.insert(0,str(drinktax) + 'vnđ')

        totalbill = totalcosmeticprice + totalgroceyprice + totaldrinkprice

    
    def bill_area(self, billing_view_instance):
        global customer_name, customer_phone, customer_m1, customer_m2, customer_m3, customer_txtarea, bill_id
        customer_name = billing_view_instance.cname_txt.get()
        customer_phone = billing_view_instance.cphn_txt.get()
        customer_m1 = billing_view_instance.m1_txt.get()
        customer_m2 = billing_view_instance.m2_txt.get()
        customer_m3 = billing_view_instance.m3_txt.get()
        
        if customer_name == '' or customer_phone == '':
            # Hiển thị thông báo lỗi nếu tên hoặc số điện thoại khách hàng rỗng
            messagebox.showerror("Lỗi", "Vui lòng nhập tên và số điện thoại khách hàng.")
        elif customer_m1 == '' and customer_m2 == '' and customer_m3 == '':
            messagebox.showerror("Lỗi", "Không có sản phẩm nào được chọn.")
        elif customer_m1 == '0 vnđ' and customer_m2 == '0 vnđ' and customer_m3 == '0 vnđ':
            messagebox.showerror("Lỗi", "Không có sản phẩm nào được chọn.")
        bill_id = str(random.randint(1000000, 9999999))

        customer_txtarea = billing_view_instance.txtarea
        customer_txtarea.delete(1.0, END)
        customer_txtarea.insert(END, '\t Xin Chào Quý Khách\n')
        customer_txtarea.insert(END, f'\n ID hóa đơn: {bill_id}\n')
        customer_txtarea.insert(END, f'\n Tên khách hàng: {customer_name}\n')
        customer_txtarea.insert(END, f'\n SĐT: {customer_phone}\n')
        customer_txtarea.insert(END, '\n===================================')
        customer_txtarea.insert(END, '\nSản Phẩm \t\t Số lượng \t\t giá')
        customer_txtarea.insert(END, '\n===================================')
        if billing_view_instance.bath_txt.get()!='0':
            customer_txtarea.insert(END, f'\nGỏi cuốn \t\t{billing_view_instance.bath_txt.get()} \t\t {soapprice} vnđ')
        if billing_view_instance.face_cream_txt.get()!='0':
            customer_txtarea.insert(END, f'\nCá sốt me \t\t{billing_view_instance.face_cream_txt.get()} \t\t {facecreamprice} vnđ')
        if billing_view_instance.face_w_txt.get()!='0':
            customer_txtarea.insert(END, f'\nBò tái chanh \t\t{billing_view_instance.face_w_txt.get()} \t\t {facewashprice} vnđ')
        if billing_view_instance.Hair_s_txt.get()!='0':
            customer_txtarea.insert(END, f'\nGà rang muối \t\t{billing_view_instance.Hair_s_txt.get()} \t\t {hairprayprice} vnđ')
        if billing_view_instance.hair_g_txt.get()!='0':
            customer_txtarea.insert(END, f'\nCơm gà Hainan \t\t{billing_view_instance.hair_g_txt.get()} \t\t {hairgelpirece} vnđ')
        if billing_view_instance.body_txt.get()!='0':
            customer_txtarea.insert(END, f'\nMì xào hải sản \t\t{billing_view_instance.body_txt.get()} \t\t {bodylotionprice} vnđ')
        
        if billing_view_instance.g1_txt.get()!='0':
            customer_txtarea.insert(END, f'\nLẩu Thái \t\t{billing_view_instance.g1_txt.get()} \t\t {riceprice} vnđ')
        if billing_view_instance.g2_txt.get()!='0':
            customer_txtarea.insert(END, f'\nLẩu Sichuan \t\t{billing_view_instance.g2_txt.get()} \t\t {daalprice} vnđ')
        if billing_view_instance.g3_txt.get()!='0':
            customer_txtarea.insert(END, f'\nLẩu Kim Chi \t\t{billing_view_instance.g3_txt.get()} \t\t {oilprice} vnđ')
        if billing_view_instance.g4_s_txt.get()!='0':
            customer_txtarea.insert(END, f'\nLẩu Miso \t\t{billing_view_instance.g4_s_txt.get()} \t\t {sugarprice} vnđ')
        if billing_view_instance.g5_txt.get()!='0':
            customer_txtarea.insert(END, f'\nLẩu riêu cua \t\t{billing_view_instance.g5_txt.get()} \t\t {teaprice} vnđ')
        if billing_view_instance.g6_txt.get()!='0':
            customer_txtarea.insert(END, f'\nLẩu đuôi bò \t\t{billing_view_instance.g6_txt.get()} \t\t {wheatprice} vnđ')

        
        if billing_view_instance.n1_txt.get()!='0':
            customer_txtarea.insert(END, f'\nNước ép trái cây \t\t{billing_view_instance.n1_txt.get()} \t\t {maaprice} vnđ')
        if billing_view_instance.n2_txt.get()!='0':
            customer_txtarea.insert(END, f'\nNước ngọt \t\t{billing_view_instance.n2_txt.get()} \t\t {frootprice} vnđ')
        if billing_view_instance.n3_txt.get()!='0':
            customer_txtarea.insert(END, f'\nSữa \t\t{billing_view_instance.n3_txt.get()} \t\t {dewprice} vnđ')
        if billing_view_instance.n4_s_txt.get()!='0':
            customer_txtarea.insert(END, f'\nRượu \t\t{billing_view_instance.n4_s_txt.get()} \t\t {pepsiprice} vnđ')
        if billing_view_instance.n5_txt.get()!='0':
            customer_txtarea.insert(END, f'\nBia \t\t{billing_view_instance.n5_txt.get()} \t\t {spriteprice} vnđ')
        if billing_view_instance.n6_txt.get()!='0':
            customer_txtarea.insert(END, f'\nNước Suối \t\t{billing_view_instance.n6_txt.get()} \t\t {cococolaprice} vnđ')

        customer_txtarea.insert(END, '\n-------------------------------------------')
        if billing_view_instance.c1_txt.get()!='0':
            customer_txtarea.insert(END, f'\nThuế món khai vị  \t\t\t {cosmetictax} vnđ')
        if billing_view_instance.c2_txt.get()!='0':
            customer_txtarea.insert(END, f'\nThuế món chính \t\t\t {procerytax} vnđ')
        if billing_view_instance.c3_txt.get()!='0':
            customer_txtarea.insert(END, f'\nThuế nước \t\t\t {drinktax} vnđ')

        customer_txtarea.insert(END, f'\nTổng Hóa Đơn: \t\t\t  {totalbill} vnđ')

        
        result = messagebox.askyesno('Xác nhận', 'Bạn có muốn lưu hóa đơn không?')
        if result:
            bill_content = customer_txtarea.get(1.0, END)
            if not customer_name or not customer_phone or not bill_id:
                messagebox.showerror('Lỗi', 'Vui lòng nhập đầy đủ thông tin khách hàng và mã hóa đơn.')
            if not os.path.exists('bills'):
                os.mkdir('bills')
            else:
                file_path = f'bills/{bill_id}.txt'
                try:
                    with io.open(file_path, "w", encoding="utf-8") as file:
                        file.write(bill_content)
                        messagebox.showinfo('Thành công', f'{bill_id} đã được lưu thành công.')
                except Exception as e:
                    messagebox.showerror("Lỗi", f"Lỗi khi lưu hóa đơn: {str(e)}")


    def search_bill(self, billing_view_instance):
        search_id = billing_view_instance.c_bill_txt.get()

        if not search_id:
            messagebox.showerror("Lỗi", "Vui lòng nhập mã hóa đơn.")
            return

        file_path = f'bills/{search_id}.txt'

        if not os.path.exists(file_path):
            messagebox.showinfo("Thông báo", "Không tìm thấy hóa đơn.")
            return

        try:
            with io.open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                billing_view_instance.txtarea.delete(1.0, END)
                billing_view_instance.txtarea.insert(END, content)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi đọc hóa đơn: {str(e)}")

                
        
       



