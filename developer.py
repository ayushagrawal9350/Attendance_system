from tkinter import * #To make powerful Ui
from tkinter import ttk #It contain special tools
from PIL import Image,ImageTk #(PIL-Pillow library)To use images in our website and ImageTk is used to set the dimension of that image.
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer Info")
        
        title_lbl = Label(self.root, text="DEVELOPER",font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #Make Top Images
        # First Image
        img_top = Image.open(r"images\background3.jfif")
        img_top = img_top.resize((1530, 735), Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab1 = Label(self.root, image=self.photoimg_top)
        f_lab1.place(x=0, y=55, width=1530, height=735)
        
        #Make Main Frame
        main_frame = Frame(f_lab1,bd=2,bg="white")
        main_frame.place(x=500,y=150,width=550,height=350)
        
        #Put text
        title_lb2 = Label(main_frame, text="CREDITS:-",font=("times new roman", 25, "bold"), bg="white", fg="black")
        title_lb2.place(x=0, y=0, width=550, height=55)
        
        title_lb3 = Label(main_frame, text="AAYUSH",font=("times new roman", 18, "bold"), bg="white", fg="red")
        title_lb3.place(x=20, y=60,height=40) 
        
        title_lb4 = Label(main_frame, text="PRASHANT KUMAR YADAV",font=("times new roman", 18, "bold"), bg="white", fg="red")
        title_lb4.place(x=20, y=110,height=40) 
        
        title_lb5 = Label(main_frame, text="SWATI SINGH",font=("times new roman", 18, "bold"), bg="white", fg="red")
        title_lb5.place(x=20, y=160,height=40) 
        
        title_lb6 = Label(main_frame, text="SAGAR GIRI",font=("times new roman", 18, "bold"), bg="white", fg="red")
        title_lb6.place(x=20, y=210,height=40) 
        
        title_lb7 = Label(main_frame, text="SAHIL GUPTA",font=("times new roman", 18, "bold"), bg="white", fg="red")
        title_lb7.place(x=20, y=260,height=40) 
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()