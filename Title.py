import mutagen
from mutagen.easyid3 import EasyID3
from mutagen import id3 #, APIC


	#time_bar.start(interval=1000)




def get_title(location,start):
	try:
		mp3 = EasyID3(location)
		x = mp3["title"]
		return x[0]
	except:
		x = location[start+1: -4]
		return x


#loc="/storage/8C21-9F58/downloads/Garmi - Street Dancer 3D.mp3"
#lc="/sdcard/Download/Laal_Chunariya.mp3"
#p=id3.print(p)







