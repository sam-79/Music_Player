from tkinter import *
import glob
from tkinter import filedialog 
from tkinter import ttk
from Title import get_title
from PIL import ImageTk,Image
#from tkinter.ttk import *
from icons import get_icon
from kivy.core.audio import SoundLoader
import time
from mutagen.mp3 import MP3
#from multiprocessing import Process

import pygame
 
 
 
 
root=Tk()
root.title("Music")
root.geometry("1700x1000")
root.resizable(False,False)


 
 
pygame.init()

	
def seek():
	pygame.mixer.music.play(start=int(bar.get()))
	print(e,type(e),"xxx")


def resume():
	#print("doNe")
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
	pygame.mixer.music.play()
	play_btn.config(image=pause_icon)
	play_btn.config(command=pause)



def load_sound(dir):
	global length
	pygame.mixer.music.load(dir)
	audio=MP3(dir)
	length=audio.info.length
	#print(length)
	bar.config(to=int(length))
	bar.set(0)
	play()
#	p1=Process(target=play())
#	p2=Process(target=slide())
#	p1.start()
#	p2.start()




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




title_label=Label(root,width=22)
title_label.place(relx=0.01,rely=0.12)




play_list=Label(root,text="Playlist")
play_list.pack(padx=20,anchor=E)

folder_icon=get_icon("/sdcard/python/myAPP/Music/Folder.png")
btn=Button(root,image=folder_icon,command=open)
btn.pack(anchor=E)


#pan=PanedWindow(root, orient=VERTICAL,background="red")
#pan.pack(side=RIGHT,expand=1)


pre_icon=get_icon("/sdcard/python/myAPP/Music/pre.png")
pre_btn=Button(root,image=pre_icon,command=lambda:select_item(0))
pre_btn.pack(anchor=W,side=LEFT,pady=(550,00),padx=50)#,before=title_label)
#pre_btn.place(rely=0.8, relx=0.01)


pause_icon=get_icon("/sdcard/python/myAPP/Music/pause.png")
play_icon=get_icon("/sdcard/python/myAPP/Music/Play.png")
play_btn=Button(root,image=play_icon)
play_btn.pack(anchor=W,side=LEFT,pady=(550,00),padx=50)#before=title_label)
#play_btn.place(rely=0.8, relx=0.19)
#play_btn.config(borderwidth=0)


nxt_icon=get_icon("/sdcard/python/myAPP/Music/next.png")
nxt_btn=Button(root,image=nxt_icon,command=lambda:select_item(1))
nxt_btn.pack(anchor=W,side=LEFT,pady=(550,0),padx=50)# , before=title_label)
#nxt_btn.place(rely=0.8, relx=0.35)


#bar=ttk.Progressbar(root,length=524,mode='determinate')
bar=ttk.Scale(root,length=524,from_=0,command=seek)
bar.place(relx=0.03,rely=0.7)
#ttk.Style.theme_use(bar,"alt")


scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )



song_listbox=Listbox(root ,borderwidth=5,selectmode=SINGLE,width=30,background="White",foreground="red" , yscrollcommand = scrollbar.set)
song_listbox.pack( side = RIGHT, fill = Y , ipadx=15,ipady=5)
root.mainloop()
