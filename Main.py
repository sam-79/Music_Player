from tkinter import *
import glob
from tkinter import filedialog 
from tkinter import ttk
from Title import get_title
from PIL import ImageTk,Image
from tkinter.ttk import *
from icons import get_icon
from kivy.core.audio import SoundLoader



root=Tk()
root.title("Music")
root.geometry("1700x1000")
root.resizable(False,False)



def pause():
	sound.stop()
	play_btn.config(image=play_icon)
	play_btn.config(command=play)
	




def play():
	sound.play()
	play_btn.config(image=pause_icon)
	play_btn.config(command=pause)
	


def load_sound(dir):
	global sound
	
	try:
		if(len(str(sound))>0):
			sound.unload()
			sound = SoundLoader.load(dir)
			length=int(sound.length)
			play()
		else:
			sound = SoundLoader.load(dir)
			length=int(sound.length)
			play()
	except:
		sound = SoundLoader.load(dir)
		length=int(sound.length)
		play()




def select_item(e):
	item=song_listbox.curselection()
	item_dir=files[item[0]]
	title_label.config(text=song_listbox.get(item[0]),font=("Arial",10))
	load_sound(item_dir)
	


def open():
	global files
	files=[]
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
	#selected_item=song_listbox.curselection()
	#print(selected_item,"cv")


#lbl=Label(root,text="Playlist")
#lbl.pack()






title_label=Label(root,text="abcdefghijklmnopqrstuvwxyz",width=22)
title_label.place(relx=0.01,rely=0.12)




play_list=Label(root,text="Playlist")
play_list.pack(padx=20,anchor=E)

folder_icon=get_icon("/sdcard/python/myAPP/Music/Folder.png")
btn=Button(root,image=folder_icon,command=open)
btn.pack(anchor=E)


#pan=PanedWindow(root, orient=VERTICAL,background="red")
#pan.pack(side=RIGHT,expand=1)


pre_icon=get_icon("/sdcard/python/myAPP/Music/pre.png")
pre_btn=Button(root,image=pre_icon)
pre_btn.pack(anchor=W,side=LEFT,pady=(550,00),padx=50)#,before=title_label)
#pre_btn.place(rely=0.8, relx=0.01)


pause_icon=get_icon("/sdcard/python/myAPP/Music/pause.png")
play_icon=get_icon("/sdcard/python/myAPP/Music/Play.png")
play_btn=Button(root,image=play_icon)
play_btn.pack(anchor=W,side=LEFT,pady=(550,00),padx=50)#before=title_label)
#play_btn.place(rely=0.8, relx=0.19)



nxt_icon=get_icon("/sdcard/python/myAPP/Music/next.png")
nxt_btn=Button(root,image=nxt_icon)
nxt_btn.pack(anchor=W,side=LEFT,pady=(550,0),padx=50)# , before=title_label)
#nxt_btn.place(rely=0.8, relx=0.35)


scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )



song_listbox=Listbox(root ,selectmode=SINGLE,width=30,background="White",foreground="red" , yscrollcommand = scrollbar.set)
song_listbox.pack( side = RIGHT, fill = Y , ipadx=15,ipady=5)
root.mainloop()