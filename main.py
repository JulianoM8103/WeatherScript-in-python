import json
import requests
from tkinter import *
from tkinter.messagebox import *


class Index(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Accueil")
        self.geometry("1000x600")
        self.window()

    def window(self):
        menubar = Menu(self)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Quitter", command=self.exit)
        menubar.add_cascade(label="Menu", menu=menu1)

        self.config(menu=menubar)

        label1 = Label(self, text="WeatherScript", font=("Helvetica", 26))
        label1.pack()
        label2 = Label(self, text="L'interface vous permettant d'obtenir la météo de n'importe quelle ville du monde\n\n",
                        font=("Helvetica", 19))
        label2.pack()

        self.cityEntry = Entry(self)
        self.cityEntry.pack()

        confirmButton = Button(self, text="Obtenir la météo", command=self.next)
        confirmButton.pack()

        self.mainloop()

    def next(self):
        self.city = self.cityEntry.get()
        self.destroy()
        Weather(self.city)

    def exit(self):
        if askyesno('Quitter', 'Êtes-vous sûr de vouloir faire ça?'):
            self.destroy()


class Weather(Tk):
    def __init__(self, city):
        Tk.__init__(self)
        self.title("Météo de " + city)
        self.geometry("1000x600")
        self.city = city
        self.request()
        self.window()

    def request(self):
        url = "https://api.openweathermap.org/data/2.5/weather?q=" + str(self.city) + "&appid=eb3e55ca0093756f2541d5ad27c5021c&units=metric"

        self.data = requests.get(url)
        self.data = self.data.json()

        self.temp = self.data["main"]["temp"]
        self.ressentis = self.data["main"]["feels_like"]
        self.humidite = self.data["main"]["humidity"]
        self.vent = self.data["wind"]["speed"]


    def window(self):
        menubar = Menu(self)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="Menu Principal", command=self.mainMenu)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.exit)
        menubar.add_cascade(label="Menu", menu=menu1)

        self.config(menu=menubar)

        label1 = Label(self, text="Météo de " + self.city, font=("Helvetica", 26))
        label1.pack()

        temperatureLabel = Label(self, text="\nTempérature actuelle : " + str(self.temp) + "°C", font=("Helvetica", 18))
        temperatureLabel.pack()

        ressentisLabel = Label(self, text="\nTempérature ressentie : " + str(self.ressentis) + "°C", font=("Helvetica", 18))
        ressentisLabel.pack()

        humiditeLabel = Label(self, text="\nTaux d'humidité : " + str(self.humidite) + "%", font=("Helvetica", 18))
        humiditeLabel.pack()

        ventLabel = Label(self, text="\nVitesse du vent : " + str(self.vent) + "m/s", font=("Helvetica", 18))
        ventLabel.pack()
    
    def exit(self):
        if askyesno('Quitter', 'Êtes-vous sûr de vouloir faire ça?'):
            self.destroy()

    def mainMenu(self):
        if askyesno('Menu principal', 'Êtes-vous sûr de vouloir faire ça?'):
            self.destroy()
            Index()

window = Index()