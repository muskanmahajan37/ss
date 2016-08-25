import os
import pygtk
import gtk

os.system("screencapture screen.png")
# os.system("brightness 0")

win = gtk.Window()

image = gtk.Image()
image.set_from_file("screen.png")
image.show()

vbox = gtk.VBox()
vbox.pack_start (image)
win.add(vbox)

win.fullscreen()
win.show_all()
gtk.main()
