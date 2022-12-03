import customtkinter, tkinter
from math import trunc


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #variables
        self.humid = 100
        self.temp = 30
        self.light = 20

        
        self.Chumid = 100
        self.Ctemp = 30
        self.Clight = 20

        self.idealH = 75
        self.idealT = 27.5
        self.idealL = 13

        self.geometry("600x300")
        self.title("small example app")
        self.minsize(300, 200)

        # create 2x2 grid system
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.envlabel = customtkinter.CTkLabel(master=self, text="Environment")
        self.envlabel.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        self.syslabel = customtkinter.CTkLabel(master=self, text="System corrections")
        self.syslabel.grid(row=0, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label1 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.humid,2)))
        self.label1.grid(row=1, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label2 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.temp,2)))
        self.label2.grid(row=2, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label3 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.light,2)))
        self.label3.grid(row=3, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.slider1 = customtkinter.CTkSlider(master=self, from_=0, to=100, command=self.slider_humid)
        self.slider1.grid(row=1, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.slider2 = customtkinter.CTkSlider(master=self, from_=0, to=100, command=self.slider_temp)
        self.slider2.grid(row=2, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.slider3 = customtkinter.CTkSlider(master=self, from_=0, to=100, command=self.slider_light)
        self.slider3.grid(row=3, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label4 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.Chumid,2)))
        self.label4.grid(row=1, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label5 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.Ctemp,2)))
        self.label5.grid(row=2, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label6 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.Clight,2)))
        self.label6.grid(row=3, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        
        
    def slider_humid(self, value):
        self.humid = value
        self.Chumid = self.idealH - self.humid
        print("Humidity ", self.humid)
        print("Correction ", self.Chumid)
        self.label4 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.Chumid,2)))
        self.label4.grid(row=1, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.label1 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.humid,2)))
        self.label1.grid(row=1, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

    def slider_temp(self, value):
        self.temp = value
        self.Ctemp = self.idealT - self.temp
        print("Temperature ", self.temp)
        print("Correction ", self.Ctemp)
        self.label5 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.Ctemp,2)))
        self.label5.grid(row=2, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.label2 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.temp,2)))
        self.label2.grid(row=2, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        
    
    def slider_light(self, value):
        self.light = value
        self.Clight = self.idealL - self.light
        print("Light ", self.light)
        print("Correction ", self.Clight)
        self.label6 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.Clight,2)))
        self.label6.grid(row=3, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.label3 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.light,2)))
        self.label3.grid(row=3, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
    

if __name__ == "__main__":
    app = App()
    app.mainloop()