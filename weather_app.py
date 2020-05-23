import os
import tkinter as tk
from tkinter import font
import requests

#* Logic
def test(entry):
    print(f"{entry} testing button")

def response_fromatter(weather):
    try:
        city_name = weather['name']
        weather_dec = weather['weather'][0]['description']
        city_temp = weather['main']['temp']
        city_humidity = weather['main']['humidity']
        
        weather_info = 'City: %s \nConditions: %s \nTemperature (°C): %s \nHumidity : %s  ' % (city_name, weather_dec, city_temp,city_humidity)
    except:
        weather_info = "Cannot fetch information for given city"

    return weather_info
    

def get_weather(city):
    weather_key = os.environ.get('weather_key')
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key,'q':city,'units':'metric'}
    response =requests.get(url,params=params)
    
    # Storing response in a variable
    weather = response.json()
    
    label['text'] = response_fromatter(weather)



# Creating root
root = tk.Tk()
# The code for our app goes in between  tk and mainloop

#* Basics layout and GUI design in tkinter

#* Canvas for placing our widget insdie it
# The Canvas widget is used to draw shapes
canvas = tk.Canvas(root,height='500',width='600')
canvas.pack()

#* Background image
background_image = tk.PhotoImage(file='sunny.png')
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

#* frmae
# The Frame widget is used as a container widget to organize other widgets.
frame = tk.Frame(root,bg="#45beff",bd ="5")

#relwidth and relheight are height and width relative to parent element
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')  


#* Entry
entry = tk.Entry(frame,font=('Arial',15)) 
entry.place(relwidth="0.65",relheight="1")

#*  Button
# 1st arg= position of element, text=that we want to show     
# get method in command takes entry only once and does not update on each iteration
# For resolving this we will use lambda function                
button1 = tk.Button(frame,text="Get info.",bg="#fff",fg="black",font=('Arial',15),command= lambda:get_weather(entry.get())) 
button1.place(relx=0.7,rely=0,relwidth="0.3",relheight="1")

# creating lower frame
lower_frame = tk.Frame(root,bg="#45beff",bd ="5")
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')  

#* Label
# The Label widget is used to provide a single-line caption for other widgets. 
# It can also contain images.
label = tk.Label(lower_frame,bg="#fff",font=('Arial',15))
label.place(relwidth="1",relheight="1")

root.mainloop()



