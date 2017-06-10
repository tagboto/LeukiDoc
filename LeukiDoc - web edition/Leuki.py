#Written by Munira Adam and Zoe Tagboto
#HTML, css and Javascript by Ronald Nettey 

from flask import Flask, jsonify, request,render_template,url_for,redirect
import json
import csv
import collections

myList=[]
patId = 0
dispName =''
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/',methods=['GET','POST'])
def main():
    if request.method == "POST":
        authentication = True
        
        #This is to request data from the forms 
        dispName = userName = request.form['reg_Username']
        password = request.form['reg_Password']
        firstName = request.form['reg_Firstname']
        lastName = request.form['reg_Lastname']
        email = request.form['reg_Email']
        

        #Appended the data from a form into a list 
        regList = [userName,password,firstName,lastName,email]

        #Checks whether any of the entry boxes are empty
        for i in regList:
            if i == "":
                authentication = False

        if authentication == True:

            #Writes the data from the form into a csv file
            #If entry boxes are not empty 
            file = open("reglist.csv", "a",newline='')
            z = csv.writer(file,delimiter=',')
            data = []
            data.append(regList)
            z.writerows(data)
            del regList[0:len(regList)]
            file.close()

            return render_template('dashboard.html')

        #refreshes the page if entry boxes are
        #empty 
        else:
            return render_template('register.html')
    else:
        #send the user to the registration page
        return render_template('register.html')


#The login page 
@app.route('/log-in', methods=['GET','POST'])
def logIn():
    #If the post method is called 
    if request.method == "POST":
        
        #Takes the details entered by the user 
        dispName = logName = request.form['login_username']
        logPassword = request.form['login_password']

        

        #Opens file and sets authentication to False
        doctorList = open("reglist.csv", "r")
        doctorReader = csv.reader(doctorList)
        authentication = False
    
        #Checks each row in the file to find a match 
        for row in doctorReader:
            if len(row)!= 0:

                
                #If found a match sets authentication to true 
                if row[0]== logName and row[1]== logPassword:
                  authentication = True

        #If authentication is true takes use to dashbord 
        if authentication == True:
            return render_template('dashboard.html',dispName = logName )
 
        #If false it refreshes the page 
        else:
            return render_template('login.html')

    #Takes user to the registration page 
    else:
        return render_template('login.html')

#This is takes in data for graph and draws graph
@app.route('/calculation', methods=['GET','POST'])
def calculation(chartID='chart_ID', chart_type='line', chart_height=350):

    #If post method called stores the data 
    if request.method == 'POST':
        _rbc = int(request.form['rbc'])
        _wbc = int(request.form['wbc'])
        _protein = int(request.form['protein'])
        _platelet = int(request.form['platelet'])
        _chemoDose = int(request.form['cdose'])
        time = 20
        x=[0]
        y=[]
        y.append(_rbc+_wbc+_protein+_platelet)

        #Makes an x and y list over a time frame 
        for i in range (1,time+1):
            cancerCells = (_rbc+_wbc+_protein+_platelet)/(_chemoDose*i)
            x.append(i)
            y.append(cancerCells)


        #Name and parts of the graph
        chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
        series = [{"name": 'Cancer Cells', "data": list(y)}]
        title = {"text": 'Effect of Chemotherapy'}
        xAxis = {"title":"Time","categories": list(x)}
        yAxis = {"title": {"text": 'Number of Cancer Cells'}}
        

        #Sends information to the graph     
        return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis)
    #json.dumps(chemoData)
    else:
        #Takes user to data entry page
        return render_template('data.html')
    
@app.route('/add', methods = ['GET','POST'])
def addPatient():
#If post is called you can type in user details

    authentication = True
    #Collects details entered by the use

    patName = request.form["add_Firstname"]
    patLastName = request.form["add_Lastname"]
    patAge = request.form["add_Age"]
    patWeight = request.form["add_Weight"]
    patHeight = request.form["add_Height"]

    patRBC = request.form["add_RBC"]
    patWBC = request.form["add_WBC"]
    patProtein = request.form["add_Protein"]
    patPlatelets = request.form["add_Platelets"]
    patChemoDose = request.form["add_Chemodose"]

    patList = [patName,patLastName,patAge,patWeight,patHeight,patRBC,patWBC,patProtein,patPlatelets,patChemoDose]
    
    #Checks whether any of the entry boxes are empty
    for i in patList:
        if i == "":
            authentication = False

    if authentication == True:
        print("Autenticated")
        #Writes the data from the form into a csv file
        #If entry boxes are not empty 
        file = open("patList.csv", "a",newline='')
        z = csv.writer(file,delimiter=',')
        data = []
        data.append(patList)
        z.writerows(data)
        del patList[0:len(patList)]
        file.close()

    else:
        return render_template('dashboard.html')

        


#Runs our code 
if __name__ == "__main__":
    app.run(debug=True,port=8080, passthrough_errors=True)

