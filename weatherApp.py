import tkinter as tk
from tkinter import font
import requests

def test_function(entry):
    print("this is the entry:", entry)

def formatResponse(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        finalStr = "City: %s \nConditions: %s \nTemperature (°F): %s" % (name, description, temp)
    except:
        finalStr = "There was a problem retrieving that information."

    return finalStr
def getWeather(city):
    weatherKey = 'c03eeb08b471c10ca8057b5078e9ca0a'
    url = "http://api.openweathermap.org/data/2.5/weather"
    parameters = {'APPID': weatherKey, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=parameters)
    weather = response.json()

    label['text'] = formatResponse(weather)


HEIGHT = 500
WIDTH = 600

root = tk.Tk() # make root window

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

backgroundImage = tk.PhotoImage(file='weatherappbg2.png')
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx=0, relheight=1, relwidth=0.65)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: getWeather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lowerFrame = tk.Frame(root, bg='#80c1ff', bd=10)
lowerFrame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.5, anchor='n')

label = tk.Label(lowerFrame, font=('Courier', 20))
label.place(relwidth=1, relheight=1)

root.mainloop() # help run

#labelFont = font.Font(size=30)
#label['font'] = labelFont
