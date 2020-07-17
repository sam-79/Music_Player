from tkinter import *
import glob
from tkinter import filedialog 
from tkinter import ttk
from Title import get_title
from PIL import ImageTk,Image
#from tkinter.ttk import *
from icons import get_icon

import time , tempfile
from mutagen.mp3 import MP3

from album_art import get_art
import pygame

from play_online import main

 
root=Tk()
root.title("Music")
root.geometry("1700x1050")
root.resizable(False,False)


pygame.init()


def seek(e):
	pygame.mixer.music.play(start=int(bar.get()))

def resume():
	pygame.mixer.music.unpause()
	play_btn.config(image=pause_icon,command=lambda:pause())
	


def pause():
	pygame.mixer.music.pause()
	play_btn.config(image=play_icon)
	#rsm_time=pause_time-srt_time
	#print(rsm_time,"\n",int(rsm_time))
	play_btn.config(command=resume)
	


def play():
	#print(time.time())
	pygame.mixer.music.play(-1)
	play_btn.config(image=pause_icon,command=pause)
	pre_btn.config(command=lambda:select_item(0))
	nxt_btn.config(command=lambda:select_item(1))
	bar.config(command=seek)
	


def load_sound(dir):
	global length
	#pho=get_art(dir)
#	img=Image.open("/sdcard/Download/img.png")
#	photo = ImageTk.PhotoImage(img)
#	canvo.create_image(canvo.canvasx(300),canvo.canvasy(300),image=pho)
	
	pygame.mixer.music.load(dir)
	audio=MP3(dir)
	length=audio.info.length
	#print(length)
	bar.config(to=int(length))
	#bar.set(0)
	play()



def select_item(e):
	item=song_listbox.curselection()
	#print(item,type(item),"cvc")
	try:
		#item=song_listbox.curselection()
		index=item[0]
		if(e.num==1):
			#print("doNEM")
			item_dir=files[index]
			title_label.config(text=song_listbox.get(index),font=("Arial",10))
			
	except:
		
		if(e==1):
			song_listbox.selection_clear(item[0])
			song_listbox.selection_set(index+1)
			item_dir=files[index+1]
			title_label.config(text=song_listbox.get(index+1),font=("Arial",10))
		elif(e==0):
			song_listbox.selection_clear(item[0])
			song_listbox.selection_set(index-1)
			item_dir=files[index-1]
			title_label.config(text=song_listbox.get(index-1),font=("Arial",10))
		
	
	load_sound(item_dir)
	


def open():
	global files
	try:
		if(len(files)>0):
			pass
	except:
		files=[]
	#print(len(files),files)
	
	global slice
	dir=filedialog.askdirectory()
	#print(dir,type(dir))
	song=dir+"/*.mp3"
	slice=len(dir)
	#print(song)
	for i in glob.glob(song):
		files.append(i)
		title=get_title(i,slice)
		song_listbox.insert(END,title)
	
	
	scrollbar.config( command = song_listbox.yview )
	song_listbox.bind("<Double-1>",select_item)




def down():
	f= tempfile.TemporaryDirectory(dir = "/storage/emulated/0/")
	dir=f.name
	main(dir)
	location=dir+"/song.mp3"
	#print(location)
	load_sound(location)



# Menu Bar configurations
m=Menu(root)
op_menu=Menu(m,tearoff=0)


op_menu.add_command(label="Play Online",command=down)
m.add_cascade(label="Options  ",menu=op_menu)

m.add_cascade(label="help  ")
m.add_command(label="exit",command=exit)
m.config(background="#BDBDBD")
root.config(menu=m)


title_label=Label(root,width=22)
title_label.place(relx=0.02,rely=0.04)




play_list=Label(root,text="Playlist",font=("Arial",15))
play_list.place(relx=0.47)

folder_icon=get_icon("/sdcard/python/myAPP/Music/Folder.png")
btn=Button(root,image=folder_icon,command=open)
btn.pack(anchor=E)



canvo=Canvas(root,width=600,height=600,background="black")
canvo.place(relx=0.03,rely=0.13)
#img_lbl.place(relx=0,rely=0)
img=Image.open("/sdcard/Download/img.png")
pho= ImageTk.PhotoImage(img)
canvo.create_image(canvo.canvasx(300),canvo.canvasy(300),image=pho)



pre_icon=get_icon("/sdcard/python/myAPP/Music/pre.png")
pre_btn=Button(root,image=pre_icon)
pre_btn.pack(anchor=W,side=LEFT,pady=(750,00),padx=50)#,before=title_label)
#pre_btn.place(rely=0.8, relx=0.01)


pause_icon=get_icon("/sdcard/python/myAPP/Music/pause.png")
play_icon=get_icon("/sdcard/python/myAPP/Music/Play.png")
play_btn=Button(root,image=play_icon)
play_btn.pack(anchor=W,side=LEFT,pady=(750,00),padx=90)#before=title_label)
#play_btn.place(rely=0.8, relx=0.19)
#play_btn.config(borderwidth=0)


nxt_icon=get_icon("/sdcard/python/myAPP/Music/next.png")
nxt_btn=Button(root,image=nxt_icon)
nxt_btn.pack(anchor=W,side=LEFT,pady=(750,0),padx=50)# , before=title_label)
#nxt_btn.place(rely=0.8, relx=0.35)


bar=ttk.Progressbar(root,length=524,mode='determinate')
bar=ttk.Scale(root,length=600)
bar.place(relx=0.03,rely=0.79)
#ttk.Style.theme_use(bar,"alt")


scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )



song_listbox=Listbox(root , width=30, yscrollcommand = scrollbar.set)
song_listbox.pack( side = RIGHT, fill =Y, ipadx=15,ipady=5)


root.mainloop()
