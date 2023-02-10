from tkinter import * #To make powerful Ui
from tkinter import ttk #It contain special tools
from PIL import Image,ImageTk #(PIL-Pillow library)To use images in our website and ImageTk is used to set the dimension of that image.
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #==========================Variables===========================================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        
        # First Image
        img = Image.open(r"images\Student-Attendance-Automation-1024x538.png")
        img = img.resize((800, 200), Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
        self.photoimg = ImageTk.PhotoImage(img)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab1 = Label(self.root, image=self.photoimg)
        f_lab1.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1 = Image.open(r"images\student2.jfif")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lab2 = Label(self.root, image=self.photoimg1)
        f_lab2.place(x=800, y=0, width=800, height=200)
        
        # Background Image
        img3 = Image.open(r"images\background2.jfif")
        img3 = img3.resize((1530, 660), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=660)
        
        # Add title on background image
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        #Make Main Frame
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        #Left Label Frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=550)

        img_left = Image.open(r"images\attendance.jfif")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lab1 = Label(Left_frame, image=self.photoimg_left)
        f_lab1.place(x=5, y=0, width=720, height=130)
        
        left_inside_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=5,y=135,width=720,height=350)
        
        # Labels Entry
        
        #Attendance Id
        attendanceId_label = Label(left_inside_frame, text="Attendance_Id :", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=(10,5),sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame,width=19,textvariable=self.var_atten_id,font=("times new roman", 13))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=(10,5),sticky=W)
        
        #Roll
        rolllabel = Label(left_inside_frame, text="Roll :", font=("times new roman", 13, "bold"),bg="white")
        rolllabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        atten_roll = ttk.Entry(left_inside_frame, width=19, textvariable=self.var_atten_roll,font=("times new roman", 13))
        atten_roll.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        
        #Name
        nameLabel = Label(left_inside_frame, text="Name :", font=("times new roman", 13, "bold"),
                                bg="white")
        nameLabel.grid(row=1, column=0, padx=10, pady=(10,5), sticky=W)

        atten_name = ttk.Entry(left_inside_frame,width=19, textvariable=self.var_atten_name,font=("times new roman", 13))
        atten_name.grid(row=1, column=1, padx=10, pady=(10,5), sticky=W)
        
        #Department
        depLabel = Label(left_inside_frame, text="Department :", font=("times new roman", 13, "bold"),
                                bg="white")
        depLabel.grid(row=1, column=2, padx=10, pady=(10,5), sticky=W)

        atten_dep = ttk.Entry(left_inside_frame,width=19, textvariable=self.var_atten_dep,font=("times new roman", 13))
        atten_dep.grid(row=1, column=3, padx=10, pady=(10,5), sticky=W)
        
        
        #time
        timeLabel = Label(left_inside_frame, text="Time :", font=("times new roman", 13, "bold"),
                                bg="white")
        timeLabel.grid(row=2, column=0, padx=10, pady=(10,5), sticky=W)

        atten_time = ttk.Entry(left_inside_frame,width=19,textvariable=self.var_atten_time, font=("times new roman", 13))
        atten_time.grid(row=2, column=1, padx=10, pady=(10,5), sticky=W)
        
        #Date
        dateLabel = Label(left_inside_frame, text="Date :", font=("times new roman", 13, "bold"),
                                bg="white")
        dateLabel.grid(row=2, column=2, padx=10, pady=(10,5), sticky=W)

        atten_date = ttk.Entry(left_inside_frame,width=19, textvariable=self.var_atten_date,font=("times new roman", 13))
        atten_date.grid(row=2, column=3, padx=10, pady=(10,5), sticky=W)
        
        #Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status :", font=("times new roman", 13, "bold"),
                                bg="white")
        attendanceLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance,font=("times new roman", 12), state="readonly",width=19)
        self.atten_status["values"] = ("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        #Button Frame
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=34)

        save_btn = Button(btn_frame,text="Import csv",command=self.importCsv,width=18,font=("times new roman", 11, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=2)

        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv,width=18, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2,padx=2)

        delete_btn = Button(btn_frame, text="Update", width=18, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=4,padx=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,width=18, font=("times new roman", 11, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=6,padx=2)

        
        #Rigth Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=470)
        
        #=====================Scroll Bar Table =======================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        
        self.AttendanceReportTable["show"] = "headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #=============================Fetch Data=========================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     
    #import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir= os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    #export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No Data Found to export",parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir= os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL Files","*.*")),parent=self.root) 
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
                
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
    #Cursor Function
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    #Reset Button
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")  
                
                

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()