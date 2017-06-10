#LeukiDoc by Zoe Tagboto and Munira Adam
#Oracking Amenreynolds(2020) and Stephan Ofosuhene(2018) helped with debugging 

#This is what we used for our graphical interface.
import tkinter as tk

#We used this to import the graph and integrate it to tkinter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter.messagebox
import matplotlib.animation as animation
from matplotlib import style

#This was needed to save registrants into a csv file
import csv

import urllib
import json
import pandas as py
import numpy as np

#These are the different fonts used in our app
Heading = ("Verdana",12)
Styling = ("Helvetica",8)

#Lists for the equation, registrant and sign in person
myList = []
regList = []
signInList = []
emptyList =[]


#class to control screens done using the help of sentdex youtube video
class GUI(tk.Tk):

#creats the main screen
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        leukiDoc = tk.Frame(self)
        self.leukiDoc = leukiDoc

        leukiDoc.pack(fill="both",expand = True)

        self.frames = {}

#contais a list of all screens in gui
    def instantiate(self):

        for F in (homeScreen, inputScreen, graphWin, adviceScreen,SignReg):
        
            display = F(self.leukiDoc,self,[0,0,0,0,0,0,0],[0,0,0,0,0,0,0])
            
            self.frames[F]=display

            display.grid(row=0, column=0, stick="nsew")

        self.displayPage(homeScreen)
        
#creates and displays graph
    def createGraphWin(self,x,y):
        
        display = graphWin(self.leukiDoc,self,x,y)
            
        self.frames[graphWin] = display

        display.grid(row=0, column=0, stick="nsew") 

#displays the frame called by the user
    def displayPage(self,cont):
##        print(cont)
        change = self.frames[cont]
        change.tkraise()
        
#creates and displays homescreen
class homeScreen(tk.Frame):
    def __init__(self,parent,controller,useless1,useless2):
        tk.Frame.__init__(self,parent)
        self.logo = tk.PhotoImage(file = "Prof.png")
        logo = tk.Label(self, image = self.logo)
        label = tk.Label(self,text="Click anywhere to continue", font = Heading, bg='lightblue')
        logo.bind("<Button-1>",lambda x:controller.displayPage(SignReg))
        logo.pack()
        label.pack()
        
#creates and displays inputscreen
class inputScreen(tk.Frame):
    def __init__(self,parent,controller,useless1,useless2):
        tk.Frame.__init__(self,parent)
        
        self.background_image = tk.PhotoImage(file="Prof.png")
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)

        self.inputs= tk.Frame(self,bg='lightblue')
        self.inputs.pack(side=tk.TOP)
 
        label = tk.Label(self.inputs,text="Kindly Input Patient Data", font = Heading, bg='lightblue')
        label.grid(row=1,columnspan=2)
        
        #This is where the user inputs the dat 
        rbcLabel = tk.Label(self.inputs, text="RBC",bg='lightblue')
        wbcLabel = tk.Label(self.inputs, text="WBC",bg='lightblue')
        protLabel = tk.Label(self.inputs, text="Protein",bg='lightblue')
        platLabel = tk.Label(self.inputs, text="Platelets",bg='lightblue')
        chemDlabel = tk.Label(self.inputs, text="Chemo Dose",bg='lightblue')
        self.rbcData = tk.Entry(self.inputs)
        self.wbcData = tk.Entry(self.inputs)
        self.protData = tk.Entry(self.inputs)
        self.platData = tk.Entry(self.inputs)
        self.chemDoData = tk.Entry(self.inputs)

        #This puts the data into the GUI
        rbcLabel.grid(row=2,column=0, stick='E')
        wbcLabel.grid(row=3,column=0, stick='E')
        protLabel.grid(row=4,column=0, stick='E')
        platLabel.grid(row=5,column=0, stick='E')
        chemDlabel.grid(row=6,column=0, stick='E')
    
        self.rbcData.grid(row=2,column=1)
        self.wbcData.grid(row=3,column=1)
        self.protData.grid(row=4,column=1)
        self.platData.grid(row=5,column=1)
        self.chemDoData.grid(row=6,column=1)

        button = tk.Button(self.inputs, text="Save", command=lambda: self.getData(myList))
        button.grid(column=2)
        
        button2 = tk.Button(self.inputs, text="Patient Advice", command=lambda:controller.displayPage(adviceScreen))
        button2.grid(column=2)

#Gets input and stores it in a list
    def getData(self,myList):
        data = [self.rbcData, self.wbcData, self.protData, self.platData, self.chemDoData]
        chemoDose = self.chemDoData
        broken = False

        #If there is something in the list it appends data to a list
        for i in data:
            i = str(i.get())
            if i != "":
                myList.append(int(i))

            #If there is nothing in the list alerts the user
            else:
                tk.messagebox.showinfo("Alert", "The box is empty")
                broken = True
                break
                    
        #Then calls the equation
        if broken == False:
            Equation(myList)
            
#plots graph this was done with the help of sentdex youtube video
class graphWin(tk.Frame):
    
     def __init__(self,parent,controller,xVar,yVar):
        tk.Frame.__init__(self,parent)

        #This is the size and characteristics for our graph
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        x = xVar
        y = yVar
        a.plot(x,y)

        #This puts the matplotlib graph into a tkinter canvas
        canvas = FigureCanvasTkAgg(f,self)

        #This is to import the Navigation toolbar
        toolbar = NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        canvas._tkcanvas.pack(fill=tk.BOTH, expand = True)

       
        #Displays the graph and places it at the bottom of the tkinter screen 
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True)

        #Buttons for navigation
        button = tk.Button(self, text="Back", command=lambda:controller.displayPage(inputScreen))
        button.pack(side=tk.TOP)
        
        button2 = tk.Button(self, text="Patient Advice", command=lambda:controller.displayPage(adviceScreen))
        button2.pack(side=tk.TOP)
        
##        self.slider= tk.Scale(self,from_=0, to=200, orient="horizontal", length=300)
##        self.slider.pack()

       
#passes variable through an equation to get x and y values
class Equation():
    def __init__(self,myList):

        #Sets the time frame for a period of 20 months 
        time = 20
        x=[0]
        y=[]
        y.append(myList[0]+myList[1]+myList[2]+myList[3])

        # Calculates x and y values over the specified time frame
        for i in range (1,time+1):
            cancerCells = (myList[0]+myList[1]+myList[2]+myList[3])/(myList[4]*i)
            x.append(i)
            y.append(cancerCells)

        print(x,y)

        #calls the graph
        app.createGraphWin(x,y)

#Displays an advice screen
class adviceScreen(tk.Frame):
    
     def __init__(self,parent,controller,useless1, useless2):
        tk.Frame.__init__(self,parent)

        #Sets the background image 
        self.background_image = tk.PhotoImage(file="Prof.png")
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        label = tk.Label(self,text="Advice", font = Heading)
        label.pack(pady=10,padx=10)

        #Navigation Buttons
        button = tk.Button(self, text="Graph",bg='lightblue', command=lambda: controller.displayPage(graphWin))
        button.pack()
        button = tk.Button(self, text="Log Out",bg='lightblue', command=lambda: controller.displayPage(SignReg))
        button.pack()
    


#cretaes and displays signin page
class SignReg(tk.Frame):
    def __init__(self,parent,controller,useless1,useless2):
        tk.Frame.__init__(self,parent)

        #This is to create and display the logo as a background image
        self.background_image = tk.PhotoImage(file="Prof.png")
        background_label = tk.Label(self, image=self.background_image)
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
        
        #This is to create frames where a user can either log in or register 
        self.frameReg= tk.Frame(self,bg='white')
        self.frameReg.pack(side=tk.LEFT)
        self.frameLog = tk.Frame(self,bg='white',pady=15)
        self.frameLog.pack(side=tk.RIGHT)

        #Creates form for registration.
        labelReg = tk.Label(self.frameReg,text="Register", font = Heading, bg='white')
        labelReg.grid(row=1,column=1,pady=10,padx=20)
        
        nameLabel = tk.Label(self.frameReg,text="NAME",bg='white',font=Styling)
        emailLabel = tk.Label(self.frameReg, text="EMAIL",bg='white',font=Styling)
        passwordLabel = tk.Label(self.frameReg, text="PASSWORD",bg='white',font=Styling)
       
        self.nameData = tk.Entry(self.frameReg)
        self.emailData = tk.Entry(self.frameReg)
        self.passwordData = tk.Entry(self.frameReg)
        

        nameLabel.grid(row=3, stick='E')
        emailLabel.grid(row=4, stick='E')
        passwordLabel.grid(row=5, stick='E')
        
    
        self.nameData.grid(row=3,column=1)
        self.emailData.grid(row=4,column=1)
        self.passwordData.grid(row=5,column=1)

        
        #Creates form for log in 
        label2 = tk.Label(self.frameLog,text="Log In", font = Heading,bg='white')
        label2.grid(row=0,column =1,pady=10,padx=20)


        nameSLabel = tk.Label(self.frameLog, text="NAME",bg='white',font=Styling)
        passwordSLabel = tk.Label(self.frameLog, text="PASSWORD",bg='white',font=Styling)
       
        self.nameSData = tk.Entry(self.frameLog,bg='white')
        self.passwordSData = tk.Entry(self.frameLog,bg='white',show='*')
        

        nameSLabel.grid(row=3, stick='E', column=0)
        passwordSLabel.grid(row=4, stick='E', column=0)
        
    
        self.nameSData.grid(row=3,column=1)
        self.passwordSData.grid(row=4,column=1)
        
        #Navigation Buttons
        button = tk.Button(self.frameReg, text="Register",bg='lightblue', command=lambda: self.regData(regList))
        button.grid(row=6,column =3)
        
        button2 = tk.Button(self.frameLog, text="Log in",bg='lightblue', command=lambda: self.signInData(signInList))
        button2.grid(row=5,column=3)

#stores registration data in a list and writes in a file
    def regData(self,regList):

        #Takes the registration data from the form 
        data = [self.nameData, self.emailData, self.passwordData]

        #If form has something append to the regList list 
        broken = False
        for i in data:
            i = str(i.get())
            if i != "":
                regList.append(i)

            #If the form is empty an alert box will pop up 
            else:
                tk.messagebox.showinfo("Alert", "The box is empty")
                broken = True
                break
                    
        #Calls the fileWrite function
        if broken == False:
            fileWrite(regList)
            
            
#Stores signin data
    def signInData(self, signInList):
        #Takes data from the sign in form
        data = [self.nameSData,self.passwordSData]

        #If form has something append to the signInList list 
        broken = False
        for i in data:
            i = str(i.get())
            if i != "":
                signInList.append(i)

            #If the form is empty an alert box will pop up
            else:
                tk.messagebox.showinfo("Alert", "The box is empty")
                broken = True
                break
        
         #Calls the fileRead function
        if broken == False:
            fileFind(signInList)
            

    
#writes registration data into csv file
class fileWrite():

    def __init__(self, regList):

        #Opens reglist file to append documents to 
            file = open("reglist.csv", "a",newline='')
            z = csv.writer(file,delimiter=',')
            data = []
            data.append(regList)

            #Writes the data to the file
            z.writerows(data)

            #Empties the list and closes the file
            del regList[0:len(regList)]
            file.close()

            #Displays the input screen 
            app.displayPage(inputScreen)

#searches registation file to find data for an old user to log in
class fileFind():
    def __init__(self,signInList):

        #Opens reglist file to read 
        doctorList = open("reglist.csv", "r")
        doctorReader = csv.reader(doctorList)
        whoRegList = []
        authentication = False 

        #Searches in file
        for row in doctorReader:
            if len(row)!= 0:
                #If the corresponding lines are equal it logs you in 
                if row[0]== signInList[0] and row[2]==signInList[1]:
                  authentication = True 
        if authentication == True:
            app.displayPage(inputScreen)

        #If not an alert box pops up
        else:
            tk.messagebox.showinfo("Alert", "Invalid Name/Password Combo")

        # Deletes the list 
        del signInList[:]

        #closes the file
        doctorList.close()



#Runs our code
        
app = GUI()
app.instantiate()
app.mainloop()



