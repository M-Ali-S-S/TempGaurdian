import psutil, tkinter as tk
import mouse, json, pynvml

with open("Temp Gaurdian\\data\\settings.json",'r') as file:
    data=json.load(file)
shown_info = data["shown"]

#________________GUI FUNCTIONS________________
def exit_win():
    window.destroy()
    exit()
def drag(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

#______________________________________________

#__________________FUNCTIONS___________________
def gpu_temperature():    
    if shown_info["gpuT"]=="True":     
        try:
            pynvml.nvmlInit()
            device_count = pynvml.nvmlDeviceGetCount()
            for i in range(device_count):
                handle = pynvml.nvmlDeviceGetHandleByIndex(i)
                gpu_name = pynvml.nvmlDeviceGetName(handle)
                temperature = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
                return f"GPU {i} temp: {temperature}°C \n"
            pynvml.nvmlShutdown()
        except pynvml.NVMLError as error:
            return "Error: {error}\n"
    else:
        return ""
def cpu_percentage():
    if shown_info["cpuP"]=="True":
        return f"CPU : {psutil.cpu_percent(1)}%\n"
    else:
        return ""
def cpu_usage():
    if shown_info["cpuU"]=="False":
        return f"CPU : {psutil.cpu_stats()}%\n"
    else:
        return ""
def ram_usage():
    if shown_info["ramU"]=="True":
        return f"RAM : {int(psutil.virtual_memory()[3]/1000000)} MB\n"
    else:
        return ""
def ram_percentage():
    if shown_info["ramP"]=="True":
        return f"RAM : {psutil.virtual_memory()[2]}%\n"
    else:
        return ""
def status():
    return f"{gpu_temperature()}{ram_usage()}{ram_percentage()}{cpu_percentage()}{cpu_usage()}"

#______________________________________________

#_____________________GUI______________________
window = tk.Tk()
window.attributes("-fullscreen",True)
window.wm_attributes('-transparentcolor',"#de23de")
window.wm_attributes("-topmost", 1)
window.attributes('-alpha',float(data['opacity']))
window.config(bg="#de23de",)
window.iconbitmap("Temp Gaurdian\\files\\TempGaurd.ico")


exitB = tk.Button(window,text="EXIT",command=exit_win,bg="yellow",fg="red")
exitB.pack()
text = tk.Label(window,font=f"b {data['font']}",bg=data['background_color'], fg=data['text_color'])
text.place(x=0,y=0)

def tick():
   stat = status()
   text_pos = (text.winfo_rootx(),text.winfo_rooty())
   button_pos = (exitB.winfo_rootx(),exitB.winfo_rooty())
   x=text.winfo_rootx()+text.winfo_width()
   y=text.winfo_rooty()+text.winfo_height()
   xB=exitB.winfo_rootx()+exitB.winfo_width()
   yB=exitB.winfo_rooty()+exitB.winfo_height()

   text_pos_plus = (x,y)
   button_pos_plus=(xB,yB)
   Xs=text_pos[0]<=mouse.get_position()[0]<=text_pos_plus[0]
   Ys=text_pos[1]<=mouse.get_position()[1]<=text_pos_plus[1]
   XsB=button_pos[0]<=mouse.get_position()[0]<=button_pos_plus[0]
   YsB=button_pos[1]<=mouse.get_position()[1]<=button_pos_plus[1]

   if (Xs and Ys) or (XsB and YsB):
      pass
   else:
      text.config(text=stat)
   window.after(500,tick)
text.bind("<Button-3>",drag)
text.bind("<B3-Motion>",motion)
exitB.bind("<Button-3>",drag)
exitB.bind("<B3-Motion>",motion)


tick()
window.mainloop()