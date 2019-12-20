from tkinter import *

'''
import serial
ser = serial.Serial('/dev/ttyUSB0', 4800)
ser.flushInput()

while True:
    s = ser.readLine()
    s = s.strip()
    print(s.decode("utf-8"))
    if s.decode("utf-8") == "READY":
        ans = 'RUN"\n"'
        ans = ans.encode("utf-8")
        ser.write(ans)
'''

root = Tk()
var = StringVar()
var.set(5.0)

after = None

def countdown(count):
    var.set(float("%.2f" % count))
    baslatbutton.configure(state=DISABLED)
    global after
    after = root.after(100, countdown, count - 0.1)
    if count < 0.1:
        root.after_cancel(after)
        var.set(5.0)
        baslatbutton.configure(state=NORMAL)
    if count > 0.1:
        after


def bitir():
    baslatbutton.configure(state=NORMAL)
    root.after_cancel(after)
    var.set(60.0)


sizex = 800
sizey = 300
posx = 40
posy = 20
root.title("TikiTaka")
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

puanLabel = Label(root, text="Puan: ", font=("Helvetica", 18))
puanLabel.grid(row=0, column=0, padx=(320, 0), pady=10, sticky=W)

puanSayi = Label(root, font=("Helvetica", 18))
puanSayi.grid(row=0, column=1, padx=(0, 320), pady=10, sticky=W)

sureLabel = Label(root, text="Süre: ", font=("Helvetica", 18))
sureLabel.grid(row=1, column=0, padx=(320, 0), pady=10, sticky=W)

sureSayi = Label(root, textvariable=var, font=("Helvetica", 18))
sureSayi.grid(row=1, column=1, padx=(0, 320), pady=10, sticky=W)

baslatbutton = Button(root, text="Başlat", font=("Helvetica", 18), width=15, command=lambda: countdown(5))
baslatbutton.grid(row=2, column=0, sticky=S, pady=10)

bitirbutton = Button(root, text="Bitir", font=("Helvetica", 18), width=15, command=bitir)
bitirbutton.grid(row=2, column=1, sticky=S, pady=10)

root.mainloop()
