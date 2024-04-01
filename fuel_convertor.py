from tkinter import Tk, ttk
from tkinter import *

from PIL import Image, ImageTk
import requests
import json

color0 = "#FFFFFF"
color1 = "#333333"
color2 = "#E85051"

window = Tk()
window.geometry('300x320')
window.title('Fuel Convertor')
window.resizable(height = FALSE, width = FALSE)

#frames
top = Frame(window, width=300, height=60, bg=color2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=color0)
main.grid(row=1, column=0)

def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    curr = combo1.get()
    amnt = amount.get()

    querystring = {"from":curr,"to":"USD","amount":amnt}

    headers = {
	    "X-RapidAPI-Key": "ea619428efmshddc64539f1a9fbfp1a64b7jsnce93392a05aa",
	    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    converted_amount = data["result"]["convertedAmount"]
    liters = converted_amount / 3.69
    formatted = "{:,.2f}".format(liters)
    result['text'] = formatted + "liters"

#top frame
icon = Image.open('images/icon.png')
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)
app_name = Label(top, image=icon, compound=LEFT, text="FUEL CONVERTER", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=color2, fg=color0)
app_name.place(x=0, y=0)

#main frame
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", font=('Ivy 15 bold'), anchor=CENTER,bg=color0, fg=color1)
result.place(x=50, y=10)

curr_vale = ['CAD', 'GHS', 'USD', 'INR', 'GBP', 'JPY']

currency = Label(main, text="Currency", width=8, height=1, padx=0, pady=0, relief="flat", font=('Ivy 10'), anchor=NW,bg=color0, fg=color1)
currency.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo1['values'] = (curr_vale)
combo1.place(x=50, y=115)

amount_label = Label(main, text="Amount", width=8, height=1, padx=0, pady=0, relief="flat", font=("Ivy 10"), anchor=NW, bg=color0, fg=color1)
amount_label.place(x=158, y=90)
amount = Entry(main, width=12, justify=CENTER, font=('Ivy 12 bold'))
amount.place(x=160, y=115)
 
button = Button(main, text='CONVERT', justify=CENTER, width=15, padx=5, height=1, bg=color2, fg=color0, font=('Ivy 15 bold'), command=convert)
button.place(x=50, y=210)

window.mainloop()


