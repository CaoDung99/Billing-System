import io
import os
import random
from tkinter import *


from pydrive import drive
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class BillingModel:

    def calculate_total(self, billing_view_instance):
        try:
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
        except ValueError:
            # Xử lý lỗi nếu giá trị nhập vào không phải là số hợp lệ
            messagebox.showerror("Lỗi", "Giá trị không hợp lệ. Vui lòng nhập lại.")

        # Tính tổng hóa đơn
        totalbill = totalcosmeticprice + totalgroceyprice + totaldrinkprice

        # Kiểm tra nếu totalbill là số
        if isinstance(totalbill, (int, float)):
            # Hiển thị thông báo tính toán thành công
            messagebox.showinfo("Thành công", "Tính toán thành công. Tổng hóa đơn là: " + str(totalbill))
        else:
            # Xóa giá trị totalbill và yêu cầu nhập lại
            totalbill = 0
            messagebox.showerror("Lỗi", "Tổng hóa đơn không hợp lệ. Vui lòng nhập lại.")
            
    
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

    def print_bill(self, billing_view_instance):
        gauth = GoogleAuth()
        gauth.LoadClientConfigFile(
            'client_secret_897380105403-p0bm8hfp9eathveid42uitdllordb42r.apps.googleusercontent.com.json')
        gauth.LocalWebserverAuth()
        customer_txtarea = billing_view_instance.txtarea.get(1.0, 'end-1c')
        if not customer_txtarea.strip():
            messagebox.showerror('Lỗi', 'Không thể in hóa đơn')
        else:
            folder_name = 'print'
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            bill_id = random.randint(1000, 9999)
            file_path = os.path.join(folder_name, f'{bill_id}.pdf')
            try:
                c = canvas.Canvas(file_path, pagesize=letter)
                c.setFont("Helvetica", 12)
                text = customer_txtarea.encode('latin-1', 'replace').decode('latin-1')
                c.drawString(100, 750, text)
                c.save()
                messagebox.showinfo('Thành công',
                                    f'Hóa đơn {bill_id} đã được lưu thành công dưới dạng tệp PDF trong thư mục "print".')

                # Tải lên Google Drive
                gauth.Authorize()
                drive = GoogleDrive(gauth)
                gfile = drive.CreateFile({'title': f'{bill_id}.pdf'})
                gfile.SetContentFile(file_path)
                gfile.Upload()
                messagebox.showinfo('Thành công',
                                    f'Hóa đơn {bill_id} đã được lưu và tải lên Google Drive thành công.')

            except Exception as e:
                messagebox.showerror("Lỗi", f"Lỗi khi lưu hóa đơn: {str(e)}")

    def delete_bill(self, billing_view_instance):
        search_id = billing_view_instance.c_bill_txt.get()

        if not search_id:
            messagebox.showerror("Lỗi", "Vui lòng nhập mã hóa đơn.")
            return

        file_path = f'bills/{search_id}.txt'

        if not os.path.exists(file_path):
            messagebox.showinfo("Thông báo", "Không tìm thấy hóa đơn.")
            return

        try:
            os.remove(file_path)
            messagebox.showinfo("Thông báo", "Hóa đơn đã được xóa thành công.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi khi xóa hóa đơn: {str(e)}")

    def exit_app(self, billing_view_instance):
        choice = messagebox.askquestion("Xác nhận", "Bạn có chắc chắn muốn thoát ứng dụng?")
        if choice == 'yes':
            # Thực hiện các thao tác cần thiết trước khi thoát ứng dụng (nếu có)
            billing_view_instance.root.destroy()
            
    


    def email_bill(self, billing_view_instance):
        label_frame = LabelFrame(billing_view_instance.root, text="Email Bill", bd=10, relief="groove")
        label_frame.place(x=380, y=80, width=550, height=600)


        senderFrame = LabelFrame(label_frame, text="Người gửi", bd=10, relief="groove")
        senderFrame.place(x=0, y=5, width=525, height=150)
        
        gmail_Label = Label(senderFrame,text="Tên khách hàng     ", fg="black", font=("times new roman", 12, "bold"))
        gmail_Label.grid(row=0, column=0, padx=20, pady=5)
        
        gmail_Entry = Entry(senderFrame,width=20, font="arial 15", bd=7, relief=SUNKEN)
        gmail_Entry.grid(row=0, column=1, padx=5, pady=10)
        
        pass_Label = Label(senderFrame,text="Mật khẩu       ", fg="black", font=("times new roman", 12, "bold"))
        pass_Label.grid(row=1, column=0, padx=20, pady=5)
        
        pass_Entry = Entry(senderFrame,width=20, font="arial 15", bd=7, relief=SUNKEN)
        pass_Entry.grid(row=1, column=1, padx=5, pady=10)
        
        
        recipientFrame = LabelFrame(label_frame, text="Người nhận", bd=10, relief="groove")
        recipientFrame.place(x=0, y=160, width=525, height=360)
        
        reciever_Label = Label(recipientFrame,text="Địa chỉ", fg="black", font=("times new roman", 12, "bold"))
        reciever_Label.grid(row=1, column=0, padx=20, pady=5)
        
        reciever_Entry = Entry(recipientFrame,width=20, font="arial 15", bd=7, relief=SUNKEN)
        reciever_Entry.grid(row=1, column=1, padx=5, pady=10)
        
        mess_Label = Label(recipientFrame,text="Nội dung:", fg="black", font=("times new roman", 12, "bold"))
        mess_Label.grid(row=2, column=0, padx=20, pady=5)
        
        mess_texttarea = Text(recipientFrame,width=43, height=12, bd=7, relief="sunken")
        mess_texttarea.grid(row=3, column=1, padx=5, pady=10)
        

        scrol_y = Scrollbar(recipientFrame, orient="vertical", command=mess_texttarea.yview)
        scrol_y.grid(row=3, column=4, sticky="ns")
        mess_texttarea.configure(yscrollcommand=scrol_y.set)
        
        send_btn=Button(label_frame, text="GỬi", bg="gray", fg="black",bd=2, pady=5, width=10, font="arial 11 bold").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        exit_btn=Button(label_frame, text="Thoát", bg="gray", fg="black",bd=2, pady=5, width=10, font="arial 11 bold").grid(row=4, column=1, padx=5, pady=5, sticky="w")
     
        label_frame.grid_columnconfigure(0, weight=1)
        label_frame.grid_columnconfigure(1, weight=1)
        label_frame.grid_rowconfigure(3, weight=1)