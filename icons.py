from PIL import ImageTk,Image


def get_icon(location):
	img=Image.open(location)
	MS=(100,100)
	#img.resize(MS)
	img.thumbnail(MS)
	im=ImageTk.PhotoImage(img)
	return im



