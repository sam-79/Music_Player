
from tkinter import *

import requests , json , tempfile , os , time

class Root(Tk):
        
        global url_list
        url_list=[]
        
        def __init__(self,dir):
        	super().__init__()
        	global f_dir
        	f_dir=dir
        	self.geometry("800x1000")
        	self.title_label = Label(self, text="Search Song")
        	self.title_label.pack(padx=30,pady=(80,0),anchor=W)
        	self.entry = Entry(self,width=30)
        	self.entry.pack(padx=30)
        	self.button = Button(self, text="search", command=self.onclick)
        	self.button.pack(pady=30)
        	self.listbox = Listbox(self, width=30)
        	self.listbox.pack(padx=30,pady=(60,0))
        	self.mainloop()
        
        
        def onclick(self):
        	print(time.time(),"étime")
        	query=self.entry.get()
        	
        	base_url = f"https://www.saavn.com/api.php?__call=autocomplete.get&_marker=0&query={query}&ctx=android&_format=json&_marker=0"
        	response=requests.get(base_url)
        	
        	songs_json = list(filter(lambda x: x.startswith("{"), response.text.splitlines()))[0]
        	songs_json = json.loads(songs_json)
        	songs_data = songs_json['songs']['data']
        	songs = []
        	
        	for song in songs_data:
        		print("andaraaya")
        		song_id = song['id']
        		song_base_url = "https://www.jiosaavn.com/api.php?cc=in&_marker=0%3F_marker%3D0&_format=json&model=Redmi_5A&__call=song.getDetails&pids="+song_id
        		song_response = requests.get(song_base_url)
        		songs_json = list(filter(lambda x: x.startswith("{"), song_response.text.splitlines()))[0]
        		songs_json = json.loads(songs_json)
        		
        		self.listbox.insert(END,songs_json[song_id]["song"])
        		self.generate_url(songs_json[song_id]['media_preview_url'])
        	
        	self.listbox.bind("<Double-1>",self.download)
        	
        
        
        def generate_url(self,url):
        	url = url.replace("preview", "h")
        	url = url.replace("_96_p.mp4", "_320.mp3")
        	#print(url)
        	url_list.append(url)
        
        
        def download(self,e):
        	cur_sel=self.listbox.curselection()
        	url=url_list[cur_sel[0]]
        	loc=f_dir+"song.mp3"
        	r = requests.get(url, allow_redirects=True)
        	open(loc, 'wb').write(r.content)
        	self.destroy()
        	
        	     	
        	

def main(f):
	root = Root(f)
	
#	root.mainloop()

#f= tempfile.TemporaryDirectory(dir = "/storage/emulated/0/")
#dir=f.name
#print(dir)
#main(dir)

