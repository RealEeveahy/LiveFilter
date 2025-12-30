from camera import Camera
from tkinter import *

class Editor():
   def __init__(self, parent, action):
      inputl = Label(parent,
                     text="Write a script here that transforms var [self.frame], typeof numpy.ndarray.",)
      inputl.pack()
      
      self.script_entry = Text(parent)
      self.script_entry.pack()

      buttons = Frame(parent)
      buttons.pack(fill=X)
      
      submit = Button(buttons, text="Submit",
                      command=lambda:action(
                         self.script_entry.get("1.0", "end-1c")
                         ))
      submit.pack(side=LEFT, fill=X)

      save = Button(buttons, text="Save", command=self.save_filter)
      save.pack(side=LEFT, fill=X)

   def save_filter(self):
      return

class GUI():
   def set_filter(self, raw):
      self.cam.filter_text=raw
      
   def __init__(self):
      self.root = Tk()
      self.root.title(" LiveFilter  ")
      
      self.left = Frame(self.root)
      self.left.grid(row=0,column=0)

      self.right = Frame(self.root)
      self.right.grid(row=0,column=1)

      self.cam = Camera(self.left)
      self.editor = Editor(self.right, self.set_filter)
      
GUI()
