import cv2
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import skimage

class Camera():
   def __init__(self, parent):
      self.cap = self.open_cam()

      #text to run eval() on then transform the webcam feed with
      self.filter_text = "cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)"
      
      self.frame = None

      self.main = Frame(parent)
      self.main.pack()
      
      self.label = Label(self.main)
      self.label.pack()

      button = Button(self.main,
                              text="Snap!",
                              command=self.capture)
      button.pack(fill=X)

      self.main.after(1,self.update)

   def open_cam(self):
      cap = cv2.VideoCapture(0)
      if not cap.isOpened():
         print("Error")
         exit()
      return cap

   def start(self):
      self.main.mainloop()

      #after closing
      self.cap.release()

   def update(self):
      ret, self.frame = self.cap.read()
      if not ret:
         print("Error 2")
         
      if self.filter_text.strip():
         try:
            exec(self.filter_text)
         except SyntaxError:
            print("Filter was not valid")
            self.filter_text = "cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)"

      img = ImageTk.PhotoImage(image=Image.fromarray(self.frame))

      self.label.configure(image=img)
      self.label.image = img
      
      self.main.after(1,self.update)

   def capture(self):
      stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
      cv2.imwrite(f"MAE_{stamp}.png", self.frame)
      print("Took a photo!")
