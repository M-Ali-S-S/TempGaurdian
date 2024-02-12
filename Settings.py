from tkinter import colorchooser
import tkinter as tk
import json , os

address = "Temp Gaurdian\\data\\settings.json"

if os.path.exists(address):
    with open(address,'r') as file:
        data=json.load(file)
else :
    with open(address,'w') as file:
        json.dump({"text_color": "#000000", "background_color": "#5463ed", "font": "12", "opacity": "0.9"},file,indent=4)
    with open(address,'r') as file:
        data=json.load(file)

#________________FUNCTIONS__________________
def save_json(key,value):
    with open("Temp Gaurdian\\data\\settings.json",'r') as file:
        data = json.load(file)
        data[key]=value
        file.close()
    with open("Temp Gaurdian\\data\\settings.json",'w') as file:
        json.dump(data,file,indent=4)
        file.close()

def colorpicker(widget,variable,string_key):
    color = colorchooser.askcolor()
    variable = f"{color[1]}"
    if variable=="None":
        variable="#ffffff"
    save_json(string_key,variable)
    widget.config(bg=variable,text=variable)
    
def save_settings(text):
    t=str(text)
    with open("setting.txt",'w') as file :
        file.write(t)
        file.close()
def op_check(opa):

    if 0.0<=float(opa) and float(opa)<=1.0:
        save_json('opacity',opa)
    else:
        save_json('opacity',"0.9")
def p():
    print("djcnsdlnsdjndk")

#___________________________________________

settings = tk.Tk()
settings.title("Settings")
settings.geometry("400x200")
settings.iconbitmap("Temp Gaurdian\\files\\TempGaurd.ico")
settings.config(bg="#000c29")

box = tk.Frame(settings,pady=8)
box.config(bg="#000c29")
box.pack()
bg_color =""
txt = tk.Label(settings,text="Drag widgets with right click ",font='b 16',borderwidth=3,relief="solid",bg='yellow',fg='red').pack()
bg_text = tk.Label(box,text="Background Color : ",pady=4,font="b",bg="#000c29",fg="#db0917")
bg_label = tk.Label(box,text="     ",bg=data['background_color'],borderwidth=3,relief="solid")
bg_button = tk.Button(box,text="Choose",command=lambda:colorpicker(bg_label,bg_color,"background_color"))

bg_text.grid(row="0",column="0")
bg_label.grid(row="0",column="1")
bg_button.grid(row="0",column="2")
#-------------------------------------
t_color =""
t_text = tk.Label(box,text="Text Color : ",pady=4,font="b",bg="#000c29",fg="#db0917")
t_label = tk.Label(box,text="     ",bg=data['text_color'],borderwidth=3,relief="solid")
t_button = tk.Button(box,text="Choose",command=lambda: colorpicker(t_label,t_color,"text_color"))

t_text.grid(row="1",column="0")
t_label.grid(row="1",column="1")
t_button.grid(row="1",column="2")

info = str(t_color)+ " " + str(bg_color)

t_font=tk.Label(box,text=f"Font size :",pady=4,font="b",bg="#000c29",fg="#db0917")
font_input = tk.Entry(box)
B_font=tk.Button(box,text="    Set    ",command=lambda: save_json('font',font_input.get()))
font_input.insert(0,data['font'])

t_font.grid(row='2',column='0')
font_input.grid(row='2',column='1')
B_font.grid(row='2',column='2',)

t_opacity=tk.Label(box,text=f"Opacity :",pady=4,font="b",bg="#000c29",fg="#db0917")
opacity_input = tk.Entry(box)
B_opacity=tk.Button(box,text="    Set    ",command=lambda: op_check(opacity_input.get()))
opacity_input.insert(0,data['opacity'])

t_opacity.grid(row='3',column='0')
opacity_input.grid(row='3',column='1')
B_opacity.grid(row='3',column='2')


# cpuU= tk.Checkbutton(box,text="CPU usage",value=)
while True:
    settings.update()
