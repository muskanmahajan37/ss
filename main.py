import os
import pygtk
import gtk

os.system("screencapture screen.png")
# os.system("brightness 0")

win = gtk.Window()

im = gtk.Image()
pixbuf = gtk.gdk.pixbuf_new_from_file("screen.png")
scaled_buf = pixbuf.scale_simple(1440,900,gtk.gdk.INTERP_BILINEAR)
im.set_from_pixbuf(scaled_buf)
im.show()

vbox = gtk.VBox()
vbox.pack_start (im)
win.add(vbox)

win.fullscreen()
win.show_all()

win.set_keep_above(True);
gtk.main()
