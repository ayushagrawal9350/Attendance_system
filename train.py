from tkinter import * #To make powerful Ui
from tkinter import ttk #It contain special tools
from PIL import Image,ImageTk #(PIL-Pillow library)To use images in our website and ImageTk is used to set the dimension of that image.
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")

        title_lbl = Label(self.root, text="TRAIN DATA SET",font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #Make Top Images
        # First Image
        img_top = Image.open(r"images\3.jfif")
        img_top = img_top.resize((510, 325), Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
        self.photoimg_top = ImageTk.PhotoImage(img_top)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab1 = Label(self.root, image=self.photoimg_top)
        f_lab1.place(x=0, y=55, width=510, height=325)

        # Second Image
        img1_top = Image.open(r"images\4.jfif")
        img1_top = img1_top.resize((510, 325), Image.ANTIALIAS)
        self.photoimg1_top = ImageTk.PhotoImage(img1_top)

        f_lab2 = Label(self.root, image=self.photoimg1_top)
        f_lab2.place(x=510, y=55, width=510, height=325)

        # Third Image
        img2_top = Image.open(r"images\6.jfif")
        img2_top = img2_top.resize((510, 325), Image.ANTIALIAS)
        self.photoimg2_top = ImageTk.PhotoImage(img2_top)

        f_lab3 = Label(self.root, image=self.photoimg2_top)
        f_lab3.place(x=1020, y=55, width=510, height=325)

        #Button
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier,font=("times new roman", 30, "bold"),bg="darkred", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        #Bottom Image
        #First Image
        img_bottom = Image.open(r"images\12.jfif")
        img_bottom = img_bottom.resize((510, 325),Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab4 = Label(self.root, image=self.photoimg_bottom)
        f_lab4.place(x=0, y=440, width=510, height=325)

        #Second_Image
        img_bottom1 = Image.open(r"images\12.jfif")
        img_bottom1 = img_bottom1.resize((510, 325),Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
        self.photoimg_bottom1 = ImageTk.PhotoImage(img_bottom1)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab5 = Label(self.root, image=self.photoimg_bottom1)
        f_lab5.place(x=510, y=440, width=510, height=325)

        #Third Image
        img_bottom2 = Image.open(r"images\12.jfif")
        img_bottom2 = img_bottom2.resize((510, 325),Image.ANTIALIAS)  # Image.ANTIALIAS convert the image from high level to low level.
        self.photoimg_bottom2 = ImageTk.PhotoImage(img_bottom2)  # one of the built-in methods which has been used to add the user-defined images in the application.

        f_lab6 = Label(self.root, image=self.photoimg_bottom2)
        f_lab6.place(x=1020, y=440, width=510, height=325)

    def train_classifier(self):
        data_dir = ("data") #Copy the Directory of path
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)] #Convert directory to list

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #Gray scale image
            imageNp = np.array(img,'uint8') #Convert Gray image to grid image
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #====================== Train The Classifier And Save ===========================
        clf =  cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets Completed!!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()