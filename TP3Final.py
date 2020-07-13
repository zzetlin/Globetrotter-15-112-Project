#################################################
# My name: Zara Zetlin
# My andrew id: zzetlin
#################################################

from cmu_112_graphics import *

# https://docs.python.org/3/library/csv.html
import csv, random


#i'm using my tetris (hw 6) for the layout 

#initialize the attributes the app has
def appStarted(app):
    app.width = 1000
    app.height = 900
    app.started = True 
    app.isGameOver = False
    app.tripColors = [ "red", "cyan", "mediumorchid", "lime", "lightcoral","darkorange" ,"dodgerblue", "purple", "green", 
                             "darkred", "chartreuse", "indigo", "navy", "rosybrown","lightcoral","olive", "teal", "violet"]
    app.dTripsAndColor = dict() #each tuple is a list of a trip randomIndex = random.randint(0, len(app.tripColors) - 1) #from tetris
    app.UsernamesAndPasswordsList = []
    app.trips = []
    app.tripsVisited = []
    app.tripsPlanned = []
    app.dictOfCities = dictOfCities(app)
    app.whereMouseIsPressed = (-1,-1)
    app.key = ''
    app.usernameEntered = ""
    app.inUsernameBox = False
    app.passwordEntered = ""
    app.inPasswordBox = False
    app.continueLoginPressed = False
    app.count = 0 #for adding username/pass to dict
    app.planTripPressed = False
    app.tripPressedWasClicked = False
    app.logoutPressed = False
    app.tripsVisitedPressed = False
    app.tripsPlannedPressed= False
    app.minusButtonPressed = False 
    app.plusButtonPressed = False 
    app.leftButtonPressed = False 
    app.rightButtonPressed = False 
    app.inTripNameBox = False
    app.inTripInputBox = False
    app.tripNameEntered = ""   
    app.tripEntered = ""     
    app.wasInTripInputBox = False
    app.continuePlanTripPressed = False
    app.continuePlanTripWasPressed = False
    app.drawTripCount = 0
    app.yesPlanTripPressed = False
    app.noPlanTripPressed = False
    app.zoomWidth = 950
    app.zoomHeight = 900
    app.zoomLeftRight = 0
    app.recommendation = [] 
    app.addRecommendationPressed = True 
    app.addCityCounter = 0
    with open('userdata.csv', 'r') as csvfile: #https://stackoverflow.com/questions/42537194/how-to-check-if-xls-and-csv-files-are-empty?rq=1
        csv_dict = [row for row in csv.DictReader(csvfile)]
        if len(csv_dict) == 0:
            list1 = app.UsernamesAndPasswordsList
            if (app.yesPlanTripPressed == True) or (app.noPlanTripPressed == True):
                with open('userdata.csv', 'w', newline='') as csvfile:
                    fieldnames = ['Username','Password','Trip Name','Trip','Visited Yet'] #add trips
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()


#view the game accordingly 
def redrawAll(app, canvas):
    if (app.isGameOver == True):
        canvas.create_rectangle(app.width/3,app.height/3 ,app.width*(2/3), app.height*(2/3),fill = "black")
        canvas.create_text(app.width//2, app.height//2, text="Game Over", 
                    font="Times 28 bold italic" )
        return 
    canvas.create_rectangle( 0, 0, app.width, app.height, fill = "white")
    drawAllCities(app, canvas)
    drawScore(app, canvas)
    drawButtons(app,canvas)
    if (app.started == True):
        drawLogin(app,canvas)
    elif (app.planTripPressed == True):
        drawPlanTrip(app,canvas) 
    elif (app.tripsVisitedPressed == True):
        drawTripsVisited(app,canvas) 
    elif (app.tripsPlannedPressed == True):
        drawTripsPlanned(app,canvas)   
    elif (app.logoutPressed == True): 
        drawLogout(app,canvas)  
    # elif (app.noPlanTripPressed == True):
    #     drawRecommendation(app,canvas)
    #     drawRecCity(app,canvas)
    else:
        drawTrip(app,canvas)
        if (app.recommendation != []): 
            drawRecommendation(app,canvas)
            drawRecCity(app,canvas)
        
      

#draw the login box when app started
def drawLogin(app,canvas):
    canvas.create_rectangle(app.width*(1/3),app.height*(1/3),app.width*(2/3), app.height*(2/3),fill = "white")
    canvas.create_text(app.width*(1.5/3), app.height*(1.2/3), text="Login", font="Times 28 bold italic" )
    canvas.create_text(app.width*(1.2/3), app.height*(1.4/3), text="Username:", font="Times 20 bold italic" )
    canvas.create_rectangle(app.width*(1.4/3), app.height*(1.35/3),app.width*(1.9/3), app.height*(1.45/3),fill = "white")
    usernameEntry(app,canvas)
    canvas.create_text(app.width*(1.2/3), app.height*(1.6/3), text="Password:", font="Times 20 bold italic" )
    canvas.create_rectangle(app.width*(1.4/3), app.height*(1.55/3),app.width*(1.9/3), app.height*(1.65/3), fill = "white")
    passwordEntry(app,canvas)
    canvas.create_rectangle(app.width*(1.3/3),app.height*(1.7/3),app.width*(1.7/3), app.height*(1.9/3),fill = "white")
    canvas.create_text(app.width*(1.5/3), app.height*(1.8/3), text="Continue", font="Times 20 bold italic" )
    continuePressed(app,canvas)



#display the username in the text entry box
def usernameEntry(app,canvas):         
    canvas.create_rectangle(app.width*(1.4/3), app.height*(1.35/3),app.width*(1.9/3), app.height*(1.45/3),fill = "white")
    if (app.inUsernameBox == True):
        canvas.create_rectangle(app.width*(1.4/3), app.height*(1.35/3),app.width*(1.9/3), app.height*(1.45/3),fill = "mistyrose")
        canvas.create_text(app.width*(1.65/3), app.height*(1.4/3), text = app.usernameEntered, font="Times 20 bold italic" )
    canvas.create_text(app.width*(1.65/3), app.height*(1.4/3), text = app.usernameEntered, font="Times 20 bold italic" )



#display the password in the text entry box
def passwordEntry(app,canvas):
    canvas.create_rectangle(app.width*(1.4/3), app.height*(1.55/3),app.width*(1.9/3), app.height*(1.65/3), fill = "white")
    if (app.inPasswordBox == True):
        canvas.create_rectangle(app.width*(1.4/3), app.height*(1.55/3),app.width*(1.9/3), app.height*(1.65/3),fill = "mistyrose")
        canvas.create_text(app.width*(1.65/3), app.height*(1.6/3), text = app.passwordEntered, font="Times 20 bold italic" )
    canvas.create_text(app.width*(1.65/3), app.height*(1.6/3), text = app.passwordEntered, font="Times 20 bold italic" )



#if while logging in the continue button is pressed, remove the login box
def continuePressed(app,canvas):
    if (app.continueLoginPressed == True):
        canvas.create_rectangle(app.width*(1.3/3),app.height*(1.7/3),app.width*(1.7/3), app.height*(1.9/3),fill = "mistyrose")
        canvas.create_text(app.width*(1.5/3), app.height*(1.8/3), text="Continue", font="Times 20 bold italic" )



#make a dictionary key=username password=value
def makeDictOfUsernamesNPasswords(app):
    if (app.usernameEntered != '') and (app.passwordEntered != ''):
        app.UsernamesAndPasswordsList += [app.usernameEntered]
        app.UsernamesAndPasswordsList += [app.passwordEntered]
    if (app.tripNameEntered != '') and  (app.tripEntered != ''):
        app.UsernamesAndPasswordsList += [app.tripNameEntered]
        app.UsernamesAndPasswordsList += [app.tripEntered]
    if (app.yesPlanTripPressed == True):
        app.UsernamesAndPasswordsList += ['Yes']
    elif (app.noPlanTripPressed == True):
        app.UsernamesAndPasswordsList += ["No"]
    saveUserData(app)


#save user's username/password/trips
def saveUserData(app): # from https://docs.python.org/3/library/csv.html
    list1 = app.UsernamesAndPasswordsList
    if (app.yesPlanTripPressed == True) or (app.noPlanTripPressed == True):
        with open('userdata.csv', 'w', newline='') as csvfile:
            fieldnames = ['Username','Password','Trip Name',"Trip",'Visited Yet'] #add trips
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Username': list1[0],'Password': list1[1],'Trip Name': list1[2],'Trip': list1[3], 'Visited Yet': list1[4]})


#draw to enter the trip planned pop up        
def drawPlanTrip(app,canvas): 
    if (app.planTripPressed == True):
        canvas.create_rectangle(app.width*(.05/4),app.height*(.5/3),app.width*(3.95/4), app.height*(2.5/3),fill = "white")
        canvas.create_text(app.width*(2/4), app.height*(.75/3), text="Plan A New Trip" , font="Times 28 bold italic" )
        canvas.create_text(app.width*(2/4), app.height*(.95/3), text="Enter the cities and countries of your trip capitalized, seperated by commas,  ", font="Times 20 bold italic"  )
        canvas.create_text(app.width*(2/4), app.height*(1.15/3), text="and without using spaces between them. Trips are made with at least two cities:  ", font="Times 20 bold italic"  )
        canvas.create_text(app.width*(2/4), app.height*(1.35/3), text="eg. New York,United States,Brussels,Belgium,Tokyo,Japan,Istanbul,Turkey ", font="Times 20 bold italic"  )
        canvas.create_text(app.width*(.5/4), app.height*(1.55/3), text="Trip name:", font="Times 20 bold italic"  )
        canvas.create_rectangle(app.width*(.95/4), app.height*(1.5/3),app.width*(3.9/4), app.height*(1.6/3),fill = "white")
        tripNameEntry(app,canvas)
        canvas.create_text(app.width*(.5/4), app.height*(1.75/3), text="Cities and Countries:" , font="Times 20 bold italic" )
        canvas.create_rectangle(app.width*(.95/4), app.height*(1.7/3),app.width*(3.9/4), app.height*(1.8/3), fill = "white")
        tripEntry(app,canvas)
        canvas.create_text(app.width*(.5/4), app.height*(1.95/3), text="Visited already?:" , font="Times 20 bold italic" )
        canvas.create_rectangle(app.width*(1.6/4),app.height*(1.9/3),app.width*(1.9/4), app.height*(2/3),fill = "white")
        canvas.create_text(app.width*(1.75/4), app.height*(1.95/3), text="Yes", font="Times 20 bold italic" )
        yesPressedInPlannedTrip(app,canvas)
        canvas.create_rectangle(app.width*(2.1/4),app.height*(1.9/3),app.width*(2.4/4), app.height*(2/3),fill = "white")
        canvas.create_text(app.width*(2.25/4), app.height*(1.95/3), text="Not yet", font="Times 20 bold italic" )
        noPressedInPlannedTrip(app,canvas)
        canvas.create_rectangle(app.width*(1.3/3),app.height*(2.1/3),app.width*(1.7/3), app.height*(2.3/3),fill = "white")
        canvas.create_text(app.width*(1.5/3), app.height*(2.2/3), text="Continue", font="Times 20 bold italic" )
        continuePressedInPlannedTrip(app,canvas)


# to close the trip plan pop up and draw trip 
def continuePressedInPlannedTrip(app,canvas):
    if (app.continuePlanTripPressed == True):
        canvas.create_rectangle(app.width*(1.3/3),app.height*(2.1/3),app.width*(1.7/3), app.height*(2.3/3),fill = "mistyrose")
        canvas.create_text(app.width*(1.5/3), app.height*(2.2/3), text="Continue", font="Times 20 bold italic" )


#display when the trip name is entered 
def tripNameEntry(app,canvas):
    canvas.create_rectangle(app.width*(.95/4), app.height*(1.5/3),app.width*(3.9/4), app.height*(1.6/3),fill = "white")
    if (app.tripPressedWasClicked == True) and (app.inTripNameBox == True):
        canvas.create_rectangle(app.width*(.95/4), app.height*(1.5/3),app.width*(3.9/4), app.height*(1.6/3),fill = "mistyrose")
        canvas.create_text(app.width*(1.75/3), app.height*(1.55/3), text = app.tripNameEntered, font="Times 20 bold italic" )
    canvas.create_text(app.width*(1.75/3), app.height*(1.55/3), text = app.tripNameEntered, font="Times 20 bold italic" )


#display when the trip is entered 
def tripEntry(app,canvas):
    canvas.create_rectangle(app.width*(.95/4), app.height*(1.7/3),app.width*(3.9/4), app.height*(1.8/3), fill = "white")
    if (app.tripPressedWasClicked == True) and (app.inTripInputBox == True):
        canvas.create_rectangle(app.width*(.95/4), app.height*(1.7/3),app.width*(3.9/4), app.height*(1.8/3), fill = "mistyrose")
        canvas.create_text(app.width*(1.75/3), app.height*(1.75/3), text = app.tripEntered, font="Times 20 bold italic" )
    canvas.create_text(app.width*(1.75/3), app.height*(1.75/3), text = app.tripEntered, font="Times 20 bold italic" )


# to mark the trip as visited 
def yesPressedInPlannedTrip(app,canvas):
    if (app.yesPlanTripPressed == True):
        canvas.create_rectangle(app.width*(1.6/4),app.height*(1.9/3),app.width*(1.9/4), app.height*(2/3),fill = "mistyrose")
        canvas.create_text(app.width*(1.75/4), app.height*(1.95/3), text="Yes", font="Times 20 bold italic" )


#to mark the trip as not visited
def noPressedInPlannedTrip(app,canvas):
    if (app.noPlanTripPressed == True):
        canvas.create_rectangle(app.width*(2.1/4),app.height*(1.9/3),app.width*(2.4/4), app.height*(2/3),fill = "mistyrose")
        canvas.create_text(app.width*(2.25/4), app.height*(1.95/3), text="Not yet", font="Times 20 bold italic" )


#when logout pressed draw login page
def drawLogout(app,canvas):
    if (app.logoutPressed == True): 
        app.started == True
        drawLogin(app,canvas)


#display trips visited 
def drawTripsVisited(app,canvas): 
    iterations = len(app.tripsVisited)
    width = app.zoomWidth
    height = app.zoomHeight
    leftRight = app.zoomLeftRight
    for trip in app.tripsVisited:
        i  = app.tripsVisited.index(trip)
        # if (i %2 == 1):
        for edge in trip:
            lat1 = trip[edge][1]
            lng1 = trip[edge][2]
            lat2 = trip[edge][3]
            lng2 = trip[edge][4]
            (xCoord1, yCoord1) = getXYCoords(app, lat1, lng1, width, height)
            (xCoord2, yCoord2) = getXYCoords(app, lat2, lng2, width, height)
            canvas.create_line(xCoord1 + leftRight, yCoord1, xCoord2 + leftRight, yCoord2, fill = app.tripColors[i])
        

#display trips planned   
def drawTripsPlanned(app,canvas):
    iterations = len(app.tripsPlanned)
    width = app.zoomWidth
    height = app.zoomHeight
    leftRight = app.zoomLeftRight
    for trip in app.tripsPlanned:
        i  = app.tripsPlanned.index(trip)
        # if (i %2 == 1):
        for edge in trip:
            lat1 = trip[edge][1]
            lng1 = trip[edge][2]
            lat2 = trip[edge][3]
            lng2 = trip[edge][4]
            (xCoord1, yCoord1) = getXYCoords(app, lat1, lng1, width, height)
            (xCoord2, yCoord2) = getXYCoords(app, lat2, lng2, width, height)
            canvas.create_line(xCoord1 + leftRight, yCoord1, xCoord2 + leftRight, yCoord2, fill = app.tripColors[i])
        
 
#make a dictionary of each of the cities, values are lat,lng,country
def dictOfCities(app):
    dictOfCities = dict()
    with open('worldcities.csv', newline='') as csvCities: #from https://docs.python.org/3/library/csv.html
        reader = csv.DictReader(csvCities)
        for row in reader:
            (city, lat, lng, country) = (row['city_ascii'], float(row['lat']), float(row['lng']), row['country']) 
            dictOfCities[city] = [lat,lng,country]
    return dictOfCities


#draw each of the cities in the csv file
def drawAllCities(app, canvas):
    for city in app.dictOfCities:
        lat = app.dictOfCities[city][0]
        lng = app.dictOfCities[city][1]
        country = app.dictOfCities[city][2]
        drawCity(app, canvas, city, lat, lng, country, fill="black")


#getting tetris started on a canvas
def playMaps():
    runApp( width = 1000, height = 900)


#get the x and y coordinate of the city on the canvas
def getXYCoords(app, lat, lng, width = 1000, height = 900):
    if (0 <= float(lat) <= 90) and (0 <= float(lng) <= 180): # first quadrant
        xCoord = (float(lng)/180)*(width//2) + width//2
        yCoord = (float(lat)/90)*(-height//2)+ height//2 
    if (0 <= float(lat) <= 90) and (-180 <= float(lng) < 0): # second quadrant
        xCoord = (width//2)-(float(lng)/(-180))*(width//2)
        yCoord = (float(lat)/90)*(-height//2)+ height//2      
    if (-90 <= float(lat) < 0) and (-180 <= float(lng) < 0): # third quadrant
        xCoord = (width//2)-(float(lng)/(-180))*(width//2)
        yCoord = (float(lat)/(-90))*(height//2)+height//2      
    if (-90 <= float(lat) < 0) and (0 <= float(lng) <= 180): # fourth quadrant
        xCoord = (float(lng)/180)*(width//2) + width//2
        yCoord = (float(lat)/(-90))*(height//2)+height//2
    return (xCoord, yCoord) 


#generate the piece on the board
def drawCity(app, canvas, city, lat, lng, country, fill):
    width = app.zoomWidth
    height = app.zoomHeight
    (xCoord, yCoord) = getXYCoords(app, lat, lng, width, height)
    leftRight = app.zoomLeftRight
    drawDot(canvas, xCoord + leftRight, yCoord, fill)


#draw a dot given the x and y coordinates
def drawDot(canvas, x, y, fill):
    canvas.create_oval(x, y, x, y, fill="black")


#get distance between two points
def getDist(app, xCoord1, yCoord1, xCoord2, yCoord2):
    dist = ((xCoord2-xCoord1)**2 + (yCoord2-yCoord1)**2)**(.5)
    return dist


#make a dictionary of the cities in the trip 
def makeTripDict(app):
    dTrip = dict()
    if (app.tripEntered != ''):
        citiesAndCountriesList = app.tripEntered.split(',')
        citiesList = []
        countriesList = []
        count= 0 
        for i in citiesAndCountriesList:
            if (count %2 == 0): 
                citiesList += [i] 
            else:
                countriesList += [i]
            count+= 1
        for city1 in app.dictOfCities:
            country1 = app.dictOfCities[city1][2]
            for city2 in citiesList:
                indexOfCity2 = citiesList.index(city2)
                country2 = countriesList[indexOfCity2]
                if ((repr(city1)== repr(city2)) or (repr(city1).lower == repr(city2))) and ((repr(country1)== repr(country2)) or (repr(country1).lower == repr(country2))):
                            (lat,lng) = (app.dictOfCities[city1][0], app.dictOfCities[city1][1])
                            dTrip[city1] = [lat,lng]
        for city in citiesList: # city not in data
            if city not in dTrip:
                print(f''"Sorry, we don't have {city}, please pick another."'')
        return dTrip


#for every trip, assume there's a hamilton graph between the cities of the trip,
#  generate a list that contains a variable for every edge in this hamilton graph
def makeDictOfEdgeVars(app,dTrip):
    dXVars = dict()  # dict where keys are the var names for each edge and value is the edge weight aka distance
    citiesSeen = []
    width = app.zoomWidth
    height = app.zoomHeight
    for key1 in dTrip:
        citiesSeen += [key1]
        for key2 in dTrip:
            if (key1 != key2) and (key2 not in citiesSeen): #and #want to make sure we don't have duplicate edges, ie. key2>key1
                (lat1, lng1) = (dTrip[key1][0], dTrip[key1][1])
                (xCoord1, yCoord1) = getXYCoords(app, lat1, lng1, width, height) 
                (lat2, lng2) = (dTrip[key2][0], dTrip[key2][1])
                (xCoord2, yCoord2) = getXYCoords(app, lat2, lng2, width, height) 
                dist = getDist(app, xCoord1, yCoord1, xCoord2, yCoord2)
                dXVars[f'(X{key1}{key2})'] = dist
    return dXVars


#formulate the variables into an integer program which we will do the simplex alg on 
def formulateAsIP(app,dTrip,dXVars):  
    # dTrip = makeTripDict(app) #key is a city, value is [lat,lng]
    # dXVars = makeDictOfEdgeVars(app) #key is Xcity1city2, value is dist between the two cities
    dEdgesOfCities = dict() #key is city, value is a list of the edges (in the hamilton cycle) connected to that city
    for city in dTrip:
        edgesOfCity = []
        for edge in dXVars:
            if city in edge:
                edgesOfCity += [edge]
        dEdgesOfCities[city] = edgesOfCity
    #IP: min c^Tx,  Ax =b, x >=0
    numOfCitiesInTrip = len(dTrip)
    lengthOfXVars = len(dXVars)
    xVarMatrix = [0]*lengthOfXVars #x   
    costMatrix = [0]*lengthOfXVars #c
    aMatrix = [ ([0] * lengthOfXVars) for city in range(numOfCitiesInTrip) ] #A
    bMatrix = [2]*len(aMatrix) #b
    count1 = 0 #for the order of the x variables, the order of the edges must be consistent 
    count2 = 0 #for the row of a city
    for key in dXVars:
        xVarMatrix[count1] = key
        costMatrix[count1] = dXVars[key] #distance of the edge
        count1+= 1
    count1 = 0 #for the order of the x variables, the order of the edges must be consistent 
    count2 = 0 #for the row of a city
    for city in dEdgesOfCities:
        for edge in xVarMatrix:
            if (count1 == lengthOfXVars):
                count1 = 0
            if str(edge) in dEdgesOfCities[city]:
                aMatrix[count2][count1] = 1
            else: 
                aMatrix[count2][count1] = 0
            count1 += 1
        count2 += 1
    return (dEdgesOfCities, xVarMatrix, costMatrix, aMatrix, bMatrix)


#turn the IP into standard equality form (just negate the costs)
def makeIntoSEF(app,dTrip,dXVars,dEdgesOfCities, xVarMatrix, costMatrix, aMatrix, bMatrix):
    #negate c to make it into max instead of min 
    for i in range(len(costMatrix)):
        costMatrix[i] = (-1)*costMatrix[i]
    return (xVarMatrix, costMatrix, aMatrix, bMatrix)


#add new aux vars and make their costs -1 while making other costs 0
def constructAuxilaryProb(app,xVarMatrix, costMatrix, aMatrix, bMatrix):
    lengthB = len(bMatrix)
    newCMatrix = [0]*len(costMatrix)
    for i in range(len(aMatrix)):
        newCMatrix += [-1]
        aMatrix[i] += [1]
        xVarMatrix += [f'X{i}']
        for z in range(len(aMatrix)):
            if (i != z):
                aMatrix[z] += [0]
    newLength = len(newCMatrix)
    basis = []
    for j in range(newLength-lengthB +1, newLength+1):
        basis += [j]
    return (xVarMatrix, newCMatrix, aMatrix, bMatrix, basis)


#turn the aux prob into canonical form
def firstCanonicalForm(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis):
    for i in range(len(bMatrix)): 
        for j in range(len(newCMatrix)): 
            newCMatrix[j] += aMatrix[i][j]
    count = 1
    prevNumsInBasis = []
    for num in basis:
        prevNumsInBasis += [num]
    return (count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, prevNumsInBasis) 



#check if the non basis variables for the cost are less than zero, if they all are then we are done iterating 
def checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis):
    for i in range(len(newCMatrix)):
        if (i+1) not in basis:
            if (newCMatrix[i] > 0):
                return True 
    return False

#using Bland's rule for pivoting 


#chose a variable not in the basis to enter 
def pivot(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, origBasis, prevNumsInBasis):
    for num in basis:
        if num not in prevNumsInBasis:
            prevNumsInBasis += [num]
    enteringVar = -1
    count = 0
    for k in range(len(newCMatrix)): 
        if (newCMatrix[k] >0) and ((k+1) not in prevNumsInBasis) and (count < 1) and (0<=k<=len(newCMatrix)):
            enteringVar = k + 1
            count += 1
    kCol = []
    for i in range(len(aMatrix)): 
        kCol += [aMatrix[i][enteringVar-1]]
    #check not unbounded, the kcol must not be all <=0
    count2 = 0
    for m in range(len(kCol)): 
        if (kCol[m] >0):
            count2 += 1
    if (count2 <1):
        return 'unbounded'
    ratios = [0]*len(kCol)
    for j in range(len(kCol)):
        if (kCol[j] <= 0):
            ratios[j] = None
        else:
            ratios[j] =  bMatrix[j]/kCol[j] 
    index = -1
    minOfRatios = 10000000
    prevMinOfRatios = []
    count3 = [0]*len(kCol) # each index shows the count of that ratio 
    currIndex = 0
    for e in ratios:
        currIndex += 1
        if (e != None):
            if (e< minOfRatios):
                if (e not in prevMinOfRatios):
                    prevMinOfRatios += [e]
                    minOfRatios = e
                    index = ratios.index(e)
    leavingVar = basis[index] 
    basis[index] = enteringVar 
    indexOfEnteringVarInBasis = index
    return (xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis,prevNumsInBasis,origBasis)



#to get the general canonical form of a given matrix, c_B = 0, A_B = Identity matrix
def generalCanonicalForm(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis,prevNumsInBasis,origBasis):
    #want the column of the entering Var in the AMatrix to be 0s and to have a 1 in the e row 
    #to get a 1 in the e index of the entering var K
    #e is the index of the leaving var in aMatrix[0]
    kCol = []
    for i in range(len(aMatrix)): #0,1,2
        kCol += [aMatrix[i][enteringVar-1]]
    if (aMatrix[indexOfEnteringVarInBasis][enteringVar-1] < 0): #divide the row by that elem to make that elem 1
        for j in kCol:
            if (j ==1):
                jIndex1 = kCol.index(j)
        val = aMatrix[indexOfEnteringVarInBasis][enteringVar-1]
        for i in range(len(aMatrix[indexOfEnteringVarInBasis])):
            aMatrix[indexOfEnteringVarInBasis][i] += (abs(val)+1)*aMatrix[jIndex2][i]
        value2 = abs(val+1)*bMatrix[jIndex1]#/val
        bMatrix[indexOfEnteringVarInBasis] += value2
    elif (aMatrix[indexOfEnteringVarInBasis][enteringVar-1] > 1): #divide that row by 1/value of the element to make the element 1
        val = aMatrix[indexOfEnteringVarInBasis][enteringVar-1]
        counter = 0
        for j in kCol:
            if (j ==1) and (counter<1):
                jIndex2 = kCol.index(j)
                counter += 1
        for i in range(len(aMatrix[indexOfEnteringVarInBasis])):
            aMatrix[indexOfEnteringVarInBasis][i] -= (abs(val)-1)*aMatrix[jIndex2][i]
        value2 = (abs(val)-1)*bMatrix[jIndex2]#/val
        bMatrix[indexOfEnteringVarInBasis] -= value2
    elif (aMatrix[indexOfEnteringVarInBasis][enteringVar-1] == 0): #add a different row to that row to make that element 1 
        count = 0
        for row in range(len(bMatrix)):
            if (aMatrix[row][enteringVar-1] == 1) and (count <1):
                for i in range(len(aMatrix[0])):
                    aMatrix[indexOfEnteringVarInBasis][i] += aMatrix[row][i]
                bMatrix[indexOfEnteringVarInBasis] += bMatrix[row]
                count += 1
            elif (aMatrix[row][enteringVar-1] > 1) and (count <1):
                vals = aMatrix[row][enteringVar-1]
                for i in range(len(aMatrix[0])):
                    aMatrix[indexOfEnteringVarInBasis][i] += aMatrix[row][i]/vals
                bMatrix[indexOfEnteringVarInBasis] += bMatrix[row]/vals
                count += 1
            elif (aMatrix[row][enteringVar-1] < 0):
                vals2 = aMatrix[row][enteringVar-1]
                for i in range(len(aMatrix[0])):
                    aMatrix[indexOfEnteringVarInBasis][i] += aMatrix[row][i]/vals2
                bMatrix[indexOfEnteringVarInBasis] += bMatrix[row]/vals2
                count += 1
    if (aMatrix[indexOfEnteringVarInBasis][enteringVar-1] != 1): #check if it !=1
        values = aMatrix[indexOfEnteringVarInBasis][enteringVar-1]
        for i in range(len(aMatrix[0])):
            aMatrix[indexOfEnteringVarInBasis][i] = aMatrix[indexOfEnteringVarInBasis][i]/values
        bMatrix[indexOfEnteringVarInBasis] = bMatrix[indexOfEnteringVarInBasis]/values
    if (aMatrix[indexOfEnteringVarInBasis][enteringVar-1] == 1): #once the element is equal to 1, set all other elems in the col to 0
        for i in range(len(aMatrix)):
            if (aMatrix[i][enteringVar-1] != 0) and (i != indexOfEnteringVarInBasis):
                q = aMatrix[i][enteringVar-1]
                if (aMatrix[i][enteringVar-1] < 0):
                    for j in range(len(aMatrix[0])):
                        aMatrix[i][j] += abs(q)*aMatrix[indexOfEnteringVarInBasis][j]
                    bMatrix[i] += abs(q)*bMatrix[indexOfEnteringVarInBasis]
                if (aMatrix[i][enteringVar-1] > 0):
                    for j in range(len(aMatrix[0])):
                        aMatrix[i][j] -= abs(q)*aMatrix[indexOfEnteringVarInBasis][j]
                    bMatrix[i] -= abs(q)*bMatrix[indexOfEnteringVarInBasis]
    #want the value of the entering Var in the cMatrix to be 0
    z = newCMatrix[enteringVar-1] 
    if (newCMatrix[enteringVar-1] >0):
        for r in range(len(aMatrix[0])): 
            newCMatrix[r] -= abs(z)*aMatrix[indexOfEnteringVarInBasis][r]
    if (newCMatrix[enteringVar-1] <0):
        for r in range(len(aMatrix[0])):
            newCMatrix[r] += abs(z)*aMatrix[indexOfEnteringVarInBasis][r]
    count = 2
    return (count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis, prevNumsInBasis,origBasis)
            

# finds the solution of the values for edge edge var to find which edges are in the shortest path
def simplexSolution(app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis):
    dXVarsValue = dict() #dict that shows the assigned value of each edge var
    for number in basis:
        for index in range(len(xVarMatrix)):
            if (index == number-1):
                dXVarsValue[xVarMatrix[index]] = 1
    for i in range(len(xVarMatrix)):
        edge = xVarMatrix[i]
        if edge not in dXVarsValue:
            dXVarsValue[xVarMatrix[i]] = 0
    return dXVarsValue


#uses the solution we got to confirm it satisfies the IP
def confirmSoln(dTrip,dXVars,app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,dXVarsValue):
    # dTrip = makeTripDict(app) #key is a city, value is [lat,lng]
    # dXVars = makeDictOfEdgeVars(app) #key is Xcity1city2, value is dist between the two cities
    dEdgesOfCities = dict() #key is city, value is a list of the edges (in the hamilton cycle) connected to that city
    for city in dTrip:
        edgesOfCity = []
        for edge in dXVars:
            if city in edge:
                edgesOfCity += [edge]
        dEdgesOfCities[city] = edgesOfCity
    for edgeVar in dXVarsValue:
        assert((dXVarsValue[edgeVar] == 0) or (dXVarsValue[edgeVar] == 1)) #edge vars are either in the path =1, or not in the path =0 
    for city in dEdgesOfCities:
        numOfEdges = len(dEdgesOfCities[city])
        listOf1s = []
        for i in range(numOfEdges):
            x = dEdgesOfCities[city][i]
            if (dXVarsValue[x] == 1):
                listOf1s += [dEdgesOfCities[city][i]]
        assert(len(listOf1s) == 2) #every city only has one edge connected to it


#for two cities draw a line 
def drawLine(app,dTrip,dXVars):
    dTripDetails = dict()
    width = app.zoomWidth
    height = app.zoomHeight
    for edge in dXVars:
        dTripDetails[edge] = [5]
        for city in dTrip:
            (lat,lng) = dTrip[city]
            dTripDetails[edge] += [lat,lng]
    app.trips += [dTripDetails] 
    if (app.noPlanTripPressed == True):
        app.tripsPlanned += [dTripDetails]
    elif (app.yesPlanTripPressed == True):
        app.tripsVisited += [dTripDetails]
    return dTripDetails


#the steps of solving the LP
def simplexAlgorithm(app):
    dTrip = makeTripDict(app)
    dXVars = makeDictOfEdgeVars(app,dTrip)
    lenDXvars = len(dXVars)
    if (len(dTrip) == 2):
        dTripDetails = drawLine(app, dTrip,dXVars)
        rec = recommendations(app,dTripDetails)
        return 42
    else:
        (dEdgesOfCities, xVarMatrix, costMatrix, aMatrix, bMatrix) = formulateAsIP(app,dTrip,dXVars) 
        (xVarMatrix, costMatrix, aMatrix, bMatrix) = makeIntoSEF(app,dTrip,dXVars,dEdgesOfCities, xVarMatrix, costMatrix, aMatrix, bMatrix)
        (xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) = constructAuxilaryProb(app,xVarMatrix, costMatrix, aMatrix, bMatrix)
        # firstCanonicalForm(app)
        (count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,prevNumsInBasis)  = firstCanonicalForm(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis)
        origBasis = basis 
        lenBMtx =len(bMatrix)
        if (checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) == False):
            dXVarsValue = simplexSolution(app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) #xbar is optimal
            confirmSoln(dTrip,dXVars,app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,dXVarsValue)
            dTripDetails = dictOfTripDetails(app, dTrip, dXVars, dEdgesOfCities, count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, dXVarsValue)
            rec = recommendations(app,dTripDetails)
            return 42
        else:
            countDracula = 0
            while (checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) != False) and (countDracula <= 50):
                (xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis, origBasis, prevNumsInBasis) = pivot(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, origBasis, prevNumsInBasis) 
                (count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis,prevNumsInBasis, origBasis) = generalCanonicalForm(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis,prevNumsInBasis, origBasis)
                countDracula += 1
            if (checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) == False):
                dXVarsValue = simplexSolution(app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) #xbar is optimal
                confirmSoln(dTrip,dXVars,app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,dXVarsValue)
                dTripDetails = dictOfTripDetails(app, dTrip, dXVars, dEdgesOfCities, count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, dXVarsValue)
                rec = recommendations(app,dTripDetails)
                return 42
            


#once recommendation is added to the trip do simplex without recommending another trip 
def simplexAlgorithm2(app):
    dTrip = makeTripDict(app)
    dXVars = makeDictOfEdgeVars(app,dTrip)
    lenDXvars = len(dXVars)
    if (len(dTrip) == 2):
        dTripDetails = drawLine(app, dTrip,dXVars)
        return dTripDetails
    else:
        (dEdgesOfCities, xVarMatrix, costMatrix, aMatrix, bMatrix) = formulateAsIP(app,dTrip,dXVars) 
        (xVarMatrix, costMatrix, aMatrix, bMatrix) = makeIntoSEF(app,dTrip,dXVars,dEdgesOfCities, xVarMatrix, costMatrix, aMatrix, bMatrix)
        (xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) = constructAuxilaryProb(app,xVarMatrix, costMatrix, aMatrix, bMatrix)
        # firstCanonicalForm(app)
        (count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,prevNumsInBasis)  = firstCanonicalForm(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis)
        origBasis = basis 
        lenBMtx =len(bMatrix)
        if (checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) == False):
            dXVarsValue = simplexSolution(app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) #xbar is optimal
            confirmSoln(dTrip,dXVars,app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,dXVarsValue)
            dTripDetails = dictOfTripDetails(app, dTrip, dXVars, dEdgesOfCities, count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, dXVarsValue)
            return dTripDetails
        else:
            countDracula = 0
            while (checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) != False) and (countDracula <= 50): 
                (xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis, origBasis, prevNumsInBasis) = pivot(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, origBasis, prevNumsInBasis) 
                (count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis,prevNumsInBasis, origBasis) = generalCanonicalForm(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, leavingVar, enteringVar, indexOfEnteringVarInBasis,prevNumsInBasis, origBasis)
                countDracula += 1
            if (checkCNLessThan0(app,xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) == False):
                dXVarsValue = simplexSolution(app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis) #xbar is optimal
                confirmSoln(dTrip,dXVars,app,count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis,dXVarsValue)
                dTripDetails = dictOfTripDetails(app, dTrip, dXVars, dEdgesOfCities, count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, dXVarsValue)
                return dTripDetails



#calculating the score of having full rows
def dictOfTripDetails(app, dTrip, dXVars, dEdgesOfCities, count, xVarMatrix, newCMatrix, aMatrix, bMatrix, basis, dXVarsValue):
    # dTrip = makeTripDict(app) #key is a city, value is [lat,lng]
    # dXVars = makeDictOfEdgeVars(app) #key is Xcity1city2, value is dist between the two cities
    # # dEdgesOfCities  #key is city, value is a list of the edges (in the hamilton cycle) connected to that city
    # dXVarsValue is a dict w key is edge value is 0,1 if in graph or not
    dTripDetails = dict()
    width = app.zoomWidth
    height = app.zoomHeight
    for edge in dXVarsValue:
        citiesOnEdge = []
        if (dXVarsValue[edge] == 1):
            edgeDistance = dXVars[edge]
            dTripDetails[edge] = [edgeDistance]
            for city in dEdgesOfCities:
                if edge in dEdgesOfCities[city]:
                    citiesOnEdge += [city]
                    (lat,lng) = dTrip[city]
                    dTripDetails[edge] += [lat,lng]
    app.trips += [dTripDetails] 
    if (app.noPlanTripPressed == True):
        app.tripsPlanned += [app.trips[-1]]
    elif (app.yesPlanTripPressed == True):
        app.tripsVisited += [app.trips[-1]]         
    return dTripDetails


#draw a trip when inputted
def drawTrip(app,canvas):
    # dTripDetails = simplexAlgorithm(app) #   dTripDetails[edge] = [edgeDistance, xCoord1, yCoord1, xCoord2, yCoord2] 
    iterations = len(app.trips)
    width = app.zoomWidth
    height = app.zoomHeight
    leftRight = app.zoomLeftRight
    for trip in app.trips:
        i = app.trips.index(trip)
        for edge in trip:
            lat1 = trip[edge][1]
            lng1 = trip[edge][2]
            lat2 = trip[edge][3]
            lng2 = trip[edge][4]
            (xCoord1, yCoord1) = getXYCoords(app, lat1, lng1, width, height)
            (xCoord2, yCoord2) = getXYCoords(app, lat2, lng2, width, height)
            canvas.create_line(xCoord1 + leftRight, yCoord1, xCoord2 + leftRight, yCoord2, fill = app.tripColors[i])
 


#draw all of the buttons
def drawButtons(app,canvas):
    #plan a new trip button  
    canvas.create_rectangle(app.width*(0.1/16),  5, app.width*(2.1/16), 45, fill="lavender", width=1)
    canvas.create_text(app.width*(1.1/16), 25, text="Plan A New Trip",fill="black", font="Times 17 bold italic")
    #logout button
    canvas.create_rectangle(app.width-80,  5, app.width-5, 45, fill="lavender", width=1)
    canvas.create_text(app.width-41, 25, text="Logout",fill="black", font="Times 17 bold italic")
    #Trips viewed button
    canvas.create_rectangle(app.width*(4/16), app.height-50, app.width*(6/16), app.height-10, fill="lavender", width=1)
    canvas.create_text(app.width*(5/16),app.height-30, text="Trips Visited",fill="black", font="Times 17 bold italic")
    #trips planned button
    canvas.create_rectangle(app.width*(8/16), app.height-50, app.width*(10/16), app.height-10, fill="lavender", width=1)
    canvas.create_text(app.width*(9/16),app.height-30, text="Trips Planned",fill="black", font="Times 17 bold italic")
    #left button
    canvas.create_rectangle(app.width-260,  app.height-50, app.width-195, app.height-10, fill="lavender", width=1)
    canvas.create_text(app.width-232,app.height-30, text="<=",fill="black", font="Times 17 bold ")
    #right button  
    canvas.create_rectangle(app.width-190, app.height-50, app.width-125, app.height-10, fill="lavender", width=1)
    canvas.create_text(app.width-152,app.height-30, text="=>",fill="black", font="Times 17 bold ")
    #+ button
    canvas.create_rectangle(app.width-120,  app.height-50, app.width-65, app.height-10, fill="lavender", width=1)
    canvas.create_text(app.width-92,app.height-30, text="+",fill="black", font="Times 17 bold ")
    #- button
    canvas.create_rectangle(app.width-60, app.height-50, app.width-5, app.height-10, fill="lavender", width=1)
    canvas.create_text(app.width-32,app.height-30, text="-",fill="black", font="Times 17 bold ")



#based off of https://www.cs.cmu.edu/~rdriley/112/notes/notes-animations-part1.html
def mousePressed(app,event):
    (x,y) = (event.x,event.y)
    app.whereMouseIsPressed = (x, y)
    #enter username 
    if  (app.width*(1.4/3)  <= x <=app.width*(1.9/3)) and (app.height*(1.35/3)  <= y <= app.height*(1.45/3)):
        app.inUsernameBox = True 
    else:
        app.inUsernameBox = False 
    #enter password
    if  (app.width*(1.4/3)  <= x <=app.width*(1.9/3)) and (app.height*(1.55/3)  <= y <= app.height*(1.65/3)):
        app.inPasswordBox = True
    else:
        app.inPasswordBox = False 
    #continue pressed in login
    if  (app.width*(1.3/3)  <= x <=app.width*(1.7/3)) and (app.height*(1.7/3)  <= y <= app.height*(1.9/3)):
        app.continueLoginPressed = True
    else:
        app.continueLoginPressed = False 
    #plan a new trip pressed 
    if  (app.width*(0.1/16)  <= x <= app.width*(2.1/16)) and (5  <= y <= 45):
        app.planTripPressed = True    
        app.tripPressedWasClicked = True 
        app.addCityCounter = 0
        app.tripEntered = ''
        app.tripNameEntered = ''
        app.recommendation = []
        app.noPlanTripPressed = False
        app.yesPlanTripPressed = False
    if (app.tripPressedWasClicked == True ):
        #enter trip name 
        if  (app.width*(.95/4)  <= x <=app.width*(3.9/4)) and (app.height*(1.5/3)  <= y <= app.height*(1.6/3)):
            app.inTripNameBox = True 
        else: 
            app.inTripNameBox = False 
        #enter trip
        if  (app.width*(.95/4)  <= x <=app.width*(3.9/4)) and (app.height*(1.7/3)  <= y <= app.height*(1.8/3)):
            app.inTripInputBox = True
            app.wasInTripInputBox = True
        else:
            app.inTripInputBox = False  
        #yes pressed in trip planned
        if  (app.width*(1.6/4)  <= x <=app.width*(1.9/4)) and (app.height*(1.9/3)  <= y <= app.height*(2/3)):
            app.yesPlanTripPressed = True
        if  (app.width*(2.1/4)  <= x <=app.width*(2.4/4)) and (app.height*(1.9/3)  <= y <= app.height*(2/3)):
            app.noPlanTripPressed = True
        if  (app.width*(1.3/3)  <= x <=app.width*(1.7/3)) and (app.height*(2.1/3)  <= y <= app.height*(2.3/3)):
            app.continuePlanTripPressed = True
            app.continuePlanTripWasPressed = True
        else:
            app.continuePlanTripPressed = False 
    #logout pressed 
    if  (app.width-80  <= x <= app.width-5) and (5 <= y <= 45):
        app.logoutPressed = True    
    else:
        app.logoutPressed = False 
    #tripsVisitedPressed  
    if  (app.width*(4/16)  <= x <= app.width*(6/16)) and (app.height-50  <= y <= app.height-10):
        app.tripsVisitedPressed = True           
    else:
        app.tripsVisitedPressed = False 
    #tripsPlannedPressed
    if  (app.width*(8/16)  <= x <= app.width*(10/16)) and (app.height-50  <= y <= app.height-10):
        app.tripsPlannedPressed = True  
    else:
        app.tripsPlannedPressed = False 
    #+ button pressed
    if  (app.width-120  <= x <= app.width-65) and (app.height-50  <= y <= app.height-10):
        app.plusButtonPressed = True  
        if (app.zoomWidth <= 2500):
            app.zoomWidth += 50 
        if (app.zoomHeight <= 2450):
            app.zoomHeight += 50 
    else:
        app.plusButtonPressed = False 
    #- button
    if  (app.width-60  <= x <= app.width-5) and (app.height-50  <= y <= app.height-10):
        app.minusButtonPressed = True   
        if (app.zoomWidth > 100):
            app.zoomWidth -= 50 
        if (app.zoomHeight > 100):
            app.zoomHeight -= 50 
    else:
        app.minusButtonPressed = False 
    #left button pressed
    if  (app.width-260 <= x <= app.width-195) and (app.height-50  <= y <= app.height-10):
        app.leftButtonPressed = True  
        if (app.zoomLeftRight <=250):
            app.zoomLeftRight +=50
    else:
        app.leftButtonPressed = False 
    #right button
    if  (app.width-190  <= x <= app.width-125) and (app.height-50  <= y <= app.height-10):
        app.rightButtonPressed = True 
        if (app.zoomLeftRight >= -250):
            app.zoomLeftRight -=50  
    else:
        app.rightButtonPressed = False 
    #add recommendation button
    if  (app.width-90  <= x <= app.width-30) and (app.height-85  <= y <= app.height-60):
        app.addRecommendationPressed = True   
    else:
        app.addRecommendationPressed = False 



#watches when keys are pressed 
def keyPressed(app, event):   
    app.key = event.key 
    if (event.key == 'Space'):
        app.key = " "
    if (app.inUsernameBox == True): 
        if (event.key == 'Delete'):
            app.usernameEntered = app.usernameEntered[:-1] 
        else:
            app.usernameEntered += app.key     
    if (app.inPasswordBox == True): 
        if (event.key == 'Delete'):
            app.passwordEntered = app.passwordEntered[:-1] 
        else:
            app.passwordEntered += app.key
    if (app.inTripNameBox == True):  
        if (event.key == 'Delete'):
            app.tripNameEntered = app.tripNameEntered[:-1] 
        else:
            app.tripNameEntered += app.key
    if (app.inTripInputBox == True):  
        if (event.key == 'Delete'):
            app.tripEntered = app.tripEntered[:-1] 
        else:
            app.tripEntered += app.key
    


#def draw the number of trips 
def drawScore(app, canvas):
    score = len(app.trips)
    canvas.create_text(75,app.height-30, text=f'Number Of Trips: {score}', font="Times 17 bold italic" )



#continually check different aspects of the app
def timerFired(app):  
    if (app.continueLoginPressed == True):
        app.started = False 
    if (app.logoutPressed == True): 
        app.passwordEntered = ''
        app.usernameEntered = ''
        app.started = True
        app.logoutPressed = False 
        app.trips = []   
    if (app.tripPressedWasClicked == True):
        app.planTripPressed = True
        # app.continuePlanTripPressed = False
    if (app.continuePlanTripWasPressed == True) and (app.yesPlanTripPressed == True):#visited already
        simplexAlgorithm2(app) #dont want recs
        app.tripPressedWasClicked = False
        app.planTripPressed = False
        # app.addCityCounter = 0
        app.tripEntered = ''
        app.tripNameEntered = ''
        app.yesPlanTripPressed = False
        app.continuePlanTripWasPressed = False
        # else: #trip is being planned app.noPlanTripPressed == True 
    if (app.continuePlanTripPressed == True) and (app.noPlanTripPressed == True):
        simplexAlgorithm(app)
        app.tripPressedWasClicked = False
        app.planTripPressed = False
        # app.addCityCounter = 0
        if (app.recommendation != [] ) and (app.addRecommendationPressed == True) and (app.addCityCounter == 0):
            app.tripEntered = app.tripEntered + ',' + app.recommendation[0] + ',' + app.recommendation[1]
            simplexAlgorithm2(app)
            app.addRecommendationPressed = False
            app.noPlanTripPressed = False
            app.tripEntered = ''
            app.tripNameEntered = ''
            app.continuePlanTripWasPressed = False
            app.recommendation = []
            app.addCityCounter += 1
            app.continuePlanTripPressed = False
        if (app.recommendation != [] ) and (app.noPlanTripPressed == True) and (app.continuePlanTripPressed == False): #(app.addRecommendationPressed == False):
            app.noPlanTripPressed = False
            app.tripEntered = ''
            app.tripNameEntered = ''
            app.continuePlanTripWasPressed = False
            app.recommendation = []



#generate the nearest city for a trip
def recommendations(app, dTripDetails):
    width = app.zoomWidth
    height = app.zoomHeight
    minDist = 500
    closestCity = ''
    countryOfClosestCity = ''
    xOfClosestCity = 0
    yOfClosestCity = 0
    counter = 0
    coords1 = ()
    coords2 = ()
    minDist1 = 500
    if (len(dTripDetails) <= 3) and (app.noPlanTripPressed == True): # number of edges
        for city in app.dictOfCities:
            lat = app.dictOfCities[city][0]
            lng = app.dictOfCities[city][1]
            country = app.dictOfCities[city][2]
            (xCoord1, yCoord1) = getXYCoords(app, lat, lng, width, height)
            for edge in dTripDetails: #   dTripDetails[edge] = [edgeDistance, lat1,lng1,lat2,lng2]  
                lat1 = dTripDetails[edge][1]
                lng1 = dTripDetails[edge][2]
                lat2 = dTripDetails[edge][3]
                lng2 = dTripDetails[edge][4]
                (xCoord2, yCoord2) = getXYCoords(app, lat1, lng1, width, height)
                (xCoord3, yCoord3) = getXYCoords(app, lat2, lng2, width, height)
                if (xCoord2 >= xCoord3):
                    maxX = xCoord2
                    minX = xCoord3
                if (xCoord2 < xCoord3):
                    minX = xCoord2
                    maxX = xCoord3
                if (yCoord2 >= yCoord3):
                    maxY = yCoord2
                    minY = yCoord3
                if (yCoord2 < yCoord3):
                    minY = yCoord2
                    maxY = yCoord3
                if ((minX <= xCoord1 <= maxX) and (minY <= yCoord1 <= maxY) and (city not in edge)):
                    dist1 = getDist(app, xCoord1, yCoord1, xCoord2, yCoord2)
                    dist2 = getDist(app, xCoord1, yCoord1, xCoord3, yCoord3)
                    totDist = dist1 + dist2
                    if (totDist < minDist1) and (city not in edge):
                        minDist1 = totDist
                        closestCity = city
                        countryOfClosestCity = country
                        xOfClosestCity = xCoord1
                        yOfClosestCity = yCoord1
                        counter += 1
    app.recommendation = (closestCity,countryOfClosestCity, xOfClosestCity, yOfClosestCity)
   


# find dist btw a given city and an edge of a trip
def distBtwCityAndEdge(app, xCoordCity, yCoordCity, xCoordVertex1, yCoordVertex1, xCoordVertex2, yCoordVertex2): 
    m = (yCoordVertex2-yCoordVertex1)/(xCoordVertex2-xCoordVertex1) #y = mx +b   , m=dy/dx    # y = yCoord2 + m*(x-xCoord2) 
    # m*x -y + (-m*xCoord2 + yCoord2) = 0 #in ax+by+c=0 form a = m, b = -1, c = (-m*xCoord2 + yCoord2) 
    # plug in (xCoord1, yCoord1) in dist = (abs(ax+by+c))/(a^2+b^2)^.5
    #y = mx +b   , m=dy/dx    # y = yCoord1 + m*x-xCoord1
    # m*x -y + (xCoord1 + yCoord1) = 0 #in ax+by+c=0 form a = m, b = -1, c = (xCoord1 + yCoord1)
    # plug in (xCoord1, yCoord1) in dist = (abs(ax+by+c))/(a^2+b^2)^.5
    d = (abs(m*xCoordCity -yCoordCity + (xCoordVertex1 + yCoordVertex1))) / ((m**2+1)**(.5))
    return d 



#draw the recommendation to trip
def drawRecommendation(app,canvas):
    if (app.recommendation == []):
        42
    else:
        if (app.recommendation[0] != '') and (app.recommendation[1] != ''):
            rec = app.recommendation[0], app.recommendation[1]
            canvas.create_text(app.width/2,app.height-70, text=f'Recommended to include {rec}', font="Times 17 bold italic" )
            canvas.create_rectangle(app.width-90,app.height-85,app.width-30, app.height-60,fill = "white")
            canvas.create_text(app.width-60,app.height-70, text='Add', font="Times 17 bold italic" )
            recommendationYesPressed(app,canvas)


#if recommendation is added remove the recommendation and update the trip
def recommendationYesPressed(app,canvas):
    if (app.addRecommendationPressed == True):
        canvas.create_rectangle(app.width-90,app.height-85,app.width-30, app.height-60,fill = "mistyrose")
        canvas.create_text(app.width-60,app.height-70, text='Add', font="Times 17 bold italic" )
        

#highlight recommended city on map 
def drawRecCity(app,canvas):
    width = app.zoomWidth
    height = app.zoomHeight
    leftRight = app.zoomLeftRight
    if (app.recommendation[0] != '') and (app.recommendation[1] != ''):
        # app.recommendation = (closestCity,countryOfClosestCity, xCoord1, yCoord1)
        x = app.recommendation[2]
        y = app.recommendation[3]
        canvas.create_oval(x + leftRight, y, x + leftRight + 12, y + 12, fill="mistyrose")




#################################################
# main
#################################################

def main():
    playMaps()

if __name__ == '__main__':
    main()
