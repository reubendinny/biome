import customtkinter, tkinter
from math import trunc
from PIL import Image


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


        self.my_image1 = customtkinter.CTkImage(light_image=Image.open("D:\Studies\Engineering\Hackus2\biome\images\hand.png"), size=(130, 130))
        self.my_image2 = customtkinter.CTkImage(light_image=Image.open("D:\Studies\Engineering\Hackus2\biome\images\peas.jpg"), size=(130, 130))
        self.my_image3 = customtkinter.CTkImage(light_image=Image.open("D:\Studies\Engineering\HHackus2\biome\images\hand2.jpeg"), size=(130, 130))

        self.db = [["Tomato",75, 27, 13,self.my_image1], ["Peas", 90, 22, 5, self.my_image2], ["brinjal", 60, 24, 7,self.my_image3]]
        self.plant = 0

        self.geometry("600x400")
        self.title("small example app")
        self.minsize(800, 600)

        # create 2x2 grid system
        self.grid_rowconfigure(7, weight=0)
        self.grid_columnconfigure((0, 1, 2, 3,4), weight=1)

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

        self.slider2 = customtkinter.CTkSlider(master=self, from_=-20, to=70, command=self.slider_temp)
        self.slider2.grid(row=2, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.slider3 = customtkinter.CTkSlider(master=self, from_=0, to=24, command=self.slider_light)
        self.slider3.grid(row=3, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label4 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.Chumid,2)))
        self.label4.grid(row=1, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label5 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.Ctemp,2)))
        self.label5.grid(row=2, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label6 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.Clight,2)))
        self.label6.grid(row=3, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        
        self.label7 = customtkinter.CTkLabel(master=self, text="Required Humidity : " + str(round(self.idealH,2)))
        self.label7.grid(row=4, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label8 = customtkinter.CTkLabel(master=self, text="Required Temperature : " + str(round(self.idealT,2)))
        self.label8.grid(row=5, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label9 = customtkinter.CTkLabel(master=self, text="Required Light : " + str(round(self.idealL,2)))
        self.label9.grid(row=6, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        # label containing image
        self.back_image1 = customtkinter.CTkImage(light_image=Image.open("D:\Studies\Engineering\Hackus2\python_gui\images\logo1.jpg"), size=(200, 200))    
        self.labe20 = customtkinter.CTkLabel(master=self, image=self.back_image1, text = " ")
        self.labe20.grid(row=4, column=3, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")


        # #ends

        self.button1 = customtkinter.CTkButton(master=self, text=self.db[self.plant][0],image=self.db[self.plant][4], command=self.button_event)
        self.button1.grid(row=4, column=0, rowspan = 1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

    def button_event(self):
        print("button pressed")
        self.plant = (self.plant+1)%len(self.db)
        self.button1 = customtkinter.CTkButton(master=self, text=self.db[self.plant][0],image=self.db[self.plant][4], command=self.button_event)
        self.button1.grid(row=4, column=0, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.idealH = self.db[self.plant][1]
        self.idealT = self.db[self.plant][2]
        self.idealL = self.db[self.plant][3]
        
        self.label7 = customtkinter.CTkLabel(master=self, text="Required Humidity : " + str(round(self.idealH,2)))
        self.label7.grid(row=4, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label8 = customtkinter.CTkLabel(master=self, text="Required Temperature : " + str(round(self.idealT,2)))
        self.label8.grid(row=5, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

        self.label9 = customtkinter.CTkLabel(master=self, text="Required Light : " + str(round(self.idealL,2)))
        self.label9.grid(row=6, column=1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")




    def slider_humid(self, value):
        self.humid = value
        self.Chumid = self.idealH - self.humid
        print("Humidity ", self.humid)
        print("Correction ", self.Chumid)
        self.label4 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.Chumid,2)))
        self.label4.grid(row=1, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.label1 = customtkinter.CTkLabel(master=self, text="Humidity : " + str(round(self.humid,2)))
        self.label1.grid(row=1, column=0,rowspan =1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")

    def slider_temp(self, value):
        self.temp = value
        self.Ctemp = self.idealT - self.temp
        print("Temperature ", self.temp)
        print("Correction ", self.Ctemp)
        self.label5 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.Ctemp,2)))
        self.label5.grid(row=2, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.label2 = customtkinter.CTkLabel(master=self, text="Temperature : " + str(round(self.temp,2)))
        self.label2.grid(row=2, column=0,rowspan =1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        
    
    def slider_light(self, value):
        self.light = value
        self.Clight = self.idealL - self.light
        print("Light ", self.light)
        print("Correction ", self.Clight)
        self.label6 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.Clight,2)))
        self.label6.grid(row=3, column=2, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
        self.label3 = customtkinter.CTkLabel(master=self, text="Light : " + str(round(self.light,2)))
        self.label3.grid(row=3, column=0,rowspan =1, columnspan=1, padx=20, pady=(20, 0), sticky="nsew")
    
    # img1 = Image.open(r"BACKGROUND_IMAGE_PATH")
    # img2 = Image.open(r"OVERLAY_IMAGE_PATH")
    # img1.paste(img2, (0,0), mask = img2)
    # img1.show()

                                              

if __name__ == "__main__":
    app = App()
    app.mainloop()