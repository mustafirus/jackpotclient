import json
from tkinter import *
import tkinter
import time
from PIL import Image, ImageTk
import urllib

canvas = None
jackpot1 = None
jackpot2 = None
jackpot3 = None

def tick():
    canvas.after(200, tick)
    jacks = get_jack()
    canvas.itemconfigure(jackpot1, text="{}".format(jacks[0]['value']))
    canvas.itemconfigure(jackpot2, text="{}".format(jacks[1]['value']))
    canvas.itemconfigure(jackpot3, text=time.strftime('%H:%M:%S'))


JACKPOT_ENDPOINT = 'http://la.ssx.com.ua:8069/slot_machine_counters/jackpot/'

def get_jack():
    url = JACKPOT_ENDPOINT + 'r101?db=test10'
    # headers = {"Content-type": "application/x-www-form-urlencoded"}
    headers = {}

    try:
        req = urllib.request.Request(url, None, headers)
        content = urllib.request.urlopen(req, timeout=200).read()
    except urllib.error.HTTPError:
        raise
    content = json.loads(content.decode())
    # err = content.get('error')
    # if err:
    #     e = urllib.error.HTTPError(req.get_full_url(), 999, err, headers, None)
    #     raise e
    return content


pilImage = Image.open("/home/golubev/Pictures/park/20070218_016.jpg")
# def showPIL(pilImage):
root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.update_idletasks()
# root.overrideredirect(1)
root.attributes('-fullscreen', True)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
canvas = tkinter.Canvas(root,width=w,height=h)
canvas.pack()
canvas.configure(background='white')
imgWidth, imgHeight = pilImage.size
# if imgWidth > w or imgHeight > h:
ratio = min(w/imgWidth, h/imgHeight)
imgWidth = int(imgWidth*ratio)
imgHeight = int(imgHeight*ratio)
pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(w/2,h/2,image=image)
label1 = canvas.create_text(w/10,h/4,text="Gold",font='sans 60', anchor=W)
label2 = canvas.create_text(w/10,h/2,text="Silver",font='sans 60', anchor=W)
label3 = canvas.create_text(w/10,h*3/4,text="Blonze",font='sans 60', anchor=W)
jackpot1 = canvas.create_text(w/2,h/4,text="Hello world!",font='sans 60')
jackpot2 = canvas.create_text(w/2,h/2,text="Hello world!",font='sans 60')
jackpot3 = canvas.create_text(w/2,h*3/4,text="Hello world!",font='sans 60')
canvas.after(1000, tick)
root.mainloop()

# showPIL(pilImage)
exit()

# root=Tk()
# label = Label(font='sans 20')
# label.pack()
# label.after_idle(tick)
# root.mainloop()
#
