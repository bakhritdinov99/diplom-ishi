from tkinter import *
from PIL import Image, ImageTk
from itertools import cycle


def slide():
  def start():
    global i, show
    if i >= (len(images) - 1):
      i = 0
      slide_image.config(image=images[i])
    else:
      i = i + 1
      slide_image.configure(image=images[i])
    show = slide_image.after(200, start)

  def stop():
    global show
    slide_image.after_cancel(show)

  def resume():
    start()
  images = ["I.jpg", "K.jpg", "Y.jpg", "U.jpg"]
  photos = cycle(ImageTk.PhotoImage(Image.open(image), master=top) for image in images)

  def slideShow():
    img = next(photos)
    displayCanvas.config(image=img)
    top.after(500, slideShow)  # 0.5 seconds

  top = Tk()
  top.overrideredirect(True)
  width = top.winfo_screenwidth()
  height = top.winfo_screenwidth()
  top.geometry('%dx%d' % (640, 480))
  displayCanvas = Label(top)
  displayCanvas.pack()
  top.after(10, lambda: slideShow())

  btn1 = Button(top, text="Start", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE,
                command=start)
  btn1.pack(side=LEFT, padx=60, pady=50)
  btn2 = Button(top, text="Pause/Stop", bg='black', fg='gold', width=10, font=('ariel 20 bold'), relief=GROOVE,
                command=stop)
  btn2.pack(side=LEFT, padx=60, pady=50)
  btn3 = Button(top, text="Resume", bg='black', fg='gold', width=8, font=('ariel 20 bold'), relief=GROOVE,
                command=resume)
  btn3.pack(side=LEFT, padx=60, pady=50)
  btn4 = Button(top, text="Exit", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE,
                command=top.destroy)
  btn4.pack(side=LEFT, padx=30, pady=50)
  # top.mainloop()
  top.mainloop()

slide()
