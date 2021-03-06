import requests
import tkinter as tk
from tkinter import *
import datetime
from time import strftime
import time
import threading
import os
from time import sleep

def widget():
    #provide your current locations latitude,longitude and key.
    link="http://api.breezometer.com/air-quality/v2/current-conditions?lat={}&lon={}&key=440655dfcb1d4099a8689788038fca95".format(12.9719,77.5937)
    res = requests.get(link)
    Air_quality= res.json()
    #getting datas from server API
    AQI="Air Quality Index - {}".format(Air_quality['data']['indexes']['baqi']['aqi'])
    i=Air_quality['data']['indexes']['baqi']['aqi']
    Category="Category - {}".format(Air_quality['data']['indexes']['baqi']['category'])
    dominant_pollutant="Dominant Pollutant - {} ".format(Air_quality['data']['indexes']['baqi']['dominant_pollutant'])
        
    date = datetime.datetime.now().strftime('%d-%m-%y')
    
    cate = StringVar()
    cate.set(Category)
    
    aqiStr = StringVar()
    aqiStr.set(AQI)
    
    dominantStr = StringVar()
    dominantStr.set(dominant_pollutant)
    tk.Label(root, 
             textvariable = aqiStr,
             fg = "orange",
             bg="black",
             font = "Times").pack()
    tk.Label(root, 
             textvariable = cate,
             fg = "white",
             bg="black",
             font = "Times").pack()
    tk.Label(root,
             textvariable = dominantStr,
             fg = "yellow",
             bg="black",
             font = "Times").pack()
    tk.Label(root,
             text=date,
             fg = "blue",
             bg="black",
             font = "Times").pack()
    root.configure(background='black')
    root.attributes("-topmost", True)
    root.overrideredirect(1)
    root.update()
    while True:
        link="http://api.breezometer.com/air-quality/v2/current-conditions?lat={}&lon={}&key=440655dfcb1d4099a8689788038fca95".format(12.9719,77.5937)
        res = requests.get(link)
        Air_quality= res.json()
        #getting datas from server API
        AQI="Air Quality Index - {}".format(Air_quality['data']['indexes']['baqi']['aqi'])
        aqi=Air_quality['data']['indexes']['baqi']['aqi']
        Category="Category - {}".format(Air_quality['data']['indexes']['baqi']['category'])
        
        dominant_pollutant="Dominant Pollutant - {} ".format(Air_quality['data']['indexes']['baqi']['dominant_pollutant'])
        #condition to check weather the content is changed after some time.   
        if aqi != i:
            cate.set(Category)
            aqiStr.set(AQI)
            dominantStr.set(dominant_pollutant)
        root.update()
#This function is used to display time on the label you can call this function if needed
def time():
    string = strftime('%H:%M:%S') 
        # Styling the label widget clock
    lbl = tk.Label(root, font = ('calibri', 10, 'bold'), 
                    fg = 'white',bg="black") 
        # Placing clock at the centre
    lbl.config(text = string) 
    lbl.after(1000, time)  
    lbl.pack(anchor = 'center') 

if __name__ == '__main__':
    root = tk.Tk()
    widget()
    
    
