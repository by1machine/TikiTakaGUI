import serial
import tkinter

arduinoData = serial.Serial('/dev/ttyUSB0',4800)
def led_on():
    arduinoData.write("RUN".encode())

def led_off():
    arduinoData.write("STOP".encode())


led_control_window = tkinter.Tk()

Button = tkinter.Button

btn = Button(led_control_window, text="BASLAT", command=led_on)
btn1 = Button(led_control_window, text="BITIR", command=led_off)

btn.grid(row=0,column=1)
btn1.grid(row=1,column=1)
led_control_window.mainloop()
