from tkinter import *
from PIL import ImageTk, Image
import PIL
import glob
import os
import shutil
import numpy as np


class imagelablerGUI:
	def __init__(self, master):
		self.master = master
		self.counter = 0
		self.black_screen = PIL.Image.fromarray(np.zeros((75,150), dtype=int))


		master.title("Sort images into folders by keypress for labeling")
		master.geometry("880x470")

		#all about the path input
		self.path_in_box = Entry(master, width=400)
		self.path_in_box.place(x = 70, y = 10, width=410, height=20)

		self.l1_path_in_box = Label(master, text="Enter path:  ")
		self.l1_path_in_box.place(x = 10, y = 10, width=60, height=20)
		
		self.get_path = Button(master, text="Get path", command=self.get_path_clicker)
		self.get_path.place(x=500,y=10)

		self.path_example = Label(master, text="like this:  C:\\Users\\DeepLearning\\lable_image")
		self.path_example.place(x = 70, y=30)

		#set an keyhandler


		#the Entrys, Labels, Button for the keyboard keys and the folder/labels

		self.l1_key = Label(master, text="Push:")
		self.l2_key = Label(master, text="Push:")
		self.l1_key.place(x = 10, y=400, width=40, height=20)
		self.l2_key.place(x = 10,y=420,width=40,height=20)

		self.l1_class = Label(master, text="to classify image as: ")
		self.l2_class = Label(master, text="to classify image as: ")
		self.l1_class.place(x=85, y=400, width=120, height=20)
		self.l2_class.place(x=85,y=420,width=120,height=20)

		self.key1 = Entry(master, width=5)
		self.class1 = Entry(master, width=40)

		self.class2 = Entry(master, width=40)
		self.key2 = Entry(master, width=5)

		self.key1.place(x=50,y=400)
		self.class1.place(x=200,y=400)
		
		self.key2.place(x=50,y=420)
		self.class2.place(x=200,y=420)

		self.commit = Button(master, text="Commit Connection", command=self.commit_clicker)
		self.commit.place(x=500,y=410)


		#Start Button
		self.start = Button(master,text="Start labeling", command=self.start_clicker)
		self.start.place(x= 250,y=440)



	def get_path_clicker(self):
		self.target_path = self.path_in_box.get()
		print(self.target_path)
		pathlist_png = glob.glob(self.target_path+"\\*.png")
		pathlist_jpg = glob.glob(self.target_path+"\\*.jpg")
		print(self.target_path+"\\*.png")
		self.pathlist = pathlist_png + pathlist_jpg

		self.next_imag = ImageTk.PhotoImage(Image.open(self.pathlist[1]))
		self.main_imag = ImageTk.PhotoImage(Image.open(self.pathlist[0]))
		self.prev_imag = ImageTk.PhotoImage(self.black_screen)

		self.frame_next_imag = Label(self.master, image = self.next_imag, height=75, width=150)
		self.frame_main_imag = Label(self.master, image = self.main_imag, height=250, width=500)
		self.frame_prev_imag = Label(self.master, image = self.prev_imag, height=75, width=150)
		
		self.frame_next_imag.place(x=680, y=100)
		self.frame_main_imag.place(x=170, y=80)
		self.frame_prev_imag.place(x=10 ,y=100)

	def commit_clicker(self):
		self.readkey1 = self.key1.get()
		self.readclass1 = self.class1.get()
		self.readkey2 = self.key2.get()
		self.readclass2 = self.class2.get()
		os.mkdir(self.target_path+"\\"+self.readclass1)
		os.mkdir(self.target_path+"\\"+self.readclass2)

	def start_clicker(self):
		self.master.bind("<Key>", self.im_changer)

	def im_changer(self, event):
		if event.char == self.readkey1:
			#copy to folder
			shutil.copy(self.pathlist[self.counter], self.target_path+"\\"+self.readclass1)
			#show new image
			self.new_main_img = ImageTk.PhotoImage(Image.open(self.pathlist[self.counter+1]))
			self.frame_main_imag.configure(image=self.new_main_img)
			self.frame_main_imag.image = self.new_main_img

			self.new_next_img = ImageTk.PhotoImage(Image.open(self.pathlist[self.counter+2]))
			self.frame_next_imag.configure(image=self.new_next_img)
			self.frame_next_imag.image = self.new_next_img

			self.new_prev_img = ImageTk.PhotoImage(Image.open(self.pathlist[self.counter]))
			self.frame_prev_imag.configure(image=self.new_prev_img)
			self.frame_prev_imag.image = self.new_prev_img


		if event.char == self.readkey2:
			shutil.copy(self.pathlist[self.counter], self.target_path+"\\"+self.readclass2)
			#show new image
			self.new_main_img = ImageTk.PhotoImage(Image.open(self.pathlist[self.counter+1]))
			self.frame_main_imag.configure(image=self.new_main_img)
			self.frame_main_imag.image = self.new_main_img

			self.new_next_img = ImageTk.PhotoImage(Image.open(self.pathlist[self.counter+2]))
			self.frame_next_imag.configure(image=self.new_next_img)
			self.frame_next_imag.image = self.new_next_img

			self.new_prev_img = ImageTk.PhotoImage(Image.open(self.pathlist[self.counter]))
			self.frame_prev_imag.configure(image=self.new_prev_img)
			self.frame_prev_imag.image = self.new_prev_img

		
		self.counter+=1



if __name__ == "__main__":
	root = Tk()
	labler = imagelablerGUI(root)
	root.mainloop()