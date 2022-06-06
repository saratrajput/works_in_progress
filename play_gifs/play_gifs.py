# from PIL import Image


# Width = 100
# Height = 100
# canvas = Image.new("RGB",(Width,Height),"white")
# gif = Image.open('yolo.gif', 'r')
# # gif = Image.open('smile.webp', 'r')
# frames = []
# try:
#     while 1:
#         frames.append(gif.copy())
#         gif.seek(len(frames))
# except EOFError:
#     pass

# for frame in frames:
#      canvas.paste(frame)
#      canvas.show()


# from tkinter import *
# import time
# import os
# root = Tk()

# frameCnt = 12
# frames = [PhotoImage(file='yolo.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

# def update(ind):

#     frame = frames[ind]
#     ind += 1
#     if ind == frameCnt:
#         ind = 0
#     label.configure(image=frame)
#     root.after(100, update, ind)
# label = Label(root)
# label.pack()
# root.after(0, update, 0)
# root.mainloop()

# load and show an animated gif file using module pyglet
# download module pyglet from: http://www.pyglet.org/download.html
# the animated dinosaur-07.gif file is in the public domain
# download from http://www.gifanimations.com
# tested with Python2.5 and pyglet1.1a2  by  vegaseat   22apr2008

import pyglet

# pick an animated gif file you have in the working directory
ag_file = "yolo.gif"
animation = pyglet.resource.animation(ag_file)
sprite = pyglet.sprite.Sprite(animation)

# create a window and set it to the image size
win = pyglet.window.Window(width=sprite.width, height=sprite.height)

# set window background color = r, g, b, alpha
# each value goes from 0.0 to 1.0
green = 0, 1, 0, 1
pyglet.gl.glClearColor(*green)

@win.event
def on_draw():
    win.clear()
    sprite.draw()

pyglet.app.run()