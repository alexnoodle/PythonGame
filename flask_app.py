import cgitb
import os
import time
from flask import Flask, render_template, request
import gameLoop



class flaskKit():

   

    def __init__(self, host, port, pkt):
        print "jjiii"
        self.host = host
        self.port = port
        self.pkt = pkt
        print 'yay'
              


    def startUp(self):
    	print 'here'
        cgitb.enable()
        print 'also here'
        app = Flask(__name__)
        print 'why not here?'
        #if __name__ == '__main__':
       

        
        app.run(host=self.host, port=int(self.port))
        print 'everywhere'


        def checkLogin(name, password):
            for i in range(int(pkt.userInformationSheetNumRow)):

                if pkt.userInformationSheet[i * pkt.userInformationSheetNumRow + 1] == name and pkt.userInformationSheet[i * pkt.userInformationSheetNumRow + 2] == password:
                    return i
            return -1

        
        @app.route('/')
        def lala():
        	print 'render damn you'
        	return render_template('go.html')
        @app.route('/', methods = ['POST'])
        def login():
            print "hhhh"
            
            if request.method == 'POST':
                name = str(request.form['user_name'])
                password = str(request.form['user_password'])
                temp = checkLogin(name, password)
                if int(temp) >= 0:
                    return greeting(pkt.userInformationSheet[temp * pkt.userInformationSheetNumRow])
                else:
                    return render_template('login.html', check = True)
            
            return render_template('login.html')

       
        def greeting(playerID):
         #   print(os.getcwd()+"/static/gameDir/globals.txt")
            resourceArray = []
            resourceData = []
            resourceArray = pkt.userResourceSheet[pkt.userResourceSheetNumRow * playerID:pkt.userResourceSheetNumRow * playerID + pkt.userResourceSheetNumCol]
            resourceData = formatResourceData()
            converterArray = readFromSheet(userConverterSheet,getRow(userConverterSheet, playerID))[1:]
            converterData = formatConverterData()
            return render_template('player_home.html', resourceArray = resourceArray, resourceData = resourceData, converterData = converterData, converterArray = converterArray)


        def readFromSheet(sheet, row):
        #pass in full path to sheet
        	line = []
        	dockSheet = open(sheet, 'r')
        	print(row)
        	if row > 0:
        	    line = dockSheet.next().split()
        	    for i in range(int(row)):
        	    	line = dockSheet.next().split()
        	else:
        	    return dockSheet.next().split()
        	print(line)
        	return line


        def formatResourceData():
            resourceData = []
            for i in range (numRow(resourceSheet)):
                resourceData.append(readFromSheet(resourceSheet,getRow(resourceSheet, i))[1])
            return resourceData

        def formatConverterData():
            converterData = []
            for i in range (numRow(converterSheet)):
                converterData.append(readFromSheet(converterSheet,getRow(converterSheet, i))[1])
            return converterData



        def getRow(sheet, ident):
            row = 0
            openSheet = open(sheet, 'r')
            for i in range(numRow(sheet)):
                check = openSheet.readline().split()
                if int(check[0]) == ident:
                    return row
                row = row + 1
            return -1

        def numRow(sheet):
        	numRow = 0;
        	file = open(sheet, 'r')
        	while(True):
        		try:
        			waste = file.next()
        			numRow += 1


        		except StopIteration:
        			return numRow






        @app.route('/getResource', methods = ['POST'])
        @app.route('/getResource')
        def getsome():
            #print(request.form["user_name"])
            if request.method == 'POST':
                return render_template('printList.html',listView = readFromsheet(userResourceSheet, 2))
            else:
                return """
                    <h1>This is a Heading</h1>
                    <p1>Why did you have to do this?</p1>


                    """

        def toggleLive():
        	status = open(liveStatus, 'r')
        	if int(status.readline()) == 1:
        		status = open(liveStatus, 'w')
        		status.write("0")
        	else:
        		status = open(liveStatus, 'w')
        		status.write("1")

        def writeOrder(order):
            if isLive():
                orderSheet = open(bufferPath + '/buffer_order.txt_' + str(time.time()), 'w')
                for i in range(len(order)):
                    orderSheet.write(str(order[i]) + ' ')
                orderSheet.close()

            else:
                orderSheet = open(queuePath + '/order.txt_' + str(time.time()), 'w')
                for i in range(len(order)):
                    orderSheet.write(str(order[i]) + ' ')
                orderSheet.close()

        def isLive():
        	status = open(liveStatus, 'r')
        	if int(status.next()) == 1:
        		return True
        	else:
        		return False

        def readFromsheet(sheet, row):
        #pass in full path to sheet
        	line = []
        	dockSheet = open(sheet, 'r')
        	for i in range(int(row)):
        		line = dockSheet.next().split()

        	return line

        def loadGlobals(Path):
            globals = open(Path, 'r')

            global homeDirPath
            homeDirPath = globals.next()[:-1]

            global userInformationSheet
            userInformationSheet = globals.next()[:-1]

            global userResourceSheet
            userResourceSheet = globals.next()[:-1]

            global userConverterSheet
            userConverterSheet = globals.next()[:-1]

            global converterSheet
            converterSheet =  globals.next()[:-1]

            global resourceSheet
            resourceSheet = globals.next()[:-1]

            global marketConverterSheet
            marketConverterSheet =	globals.next()[:-1]

            global marketResourceSheet
            marketResourceSheet = globals.next()[:-1]

            global queuePath
            queuePath = globals.next()[:-1]

            global bufferPath
            bufferPath = queuePath + "/buffer"

            global liveStatus
            liveStatus = globals.next()[:-1]
            print("Done")
            return 1

        #loadGlobals((os.getcwd() + '/static/gameDir/globals.txt'))
        #order = ['sell', 'resource', 0, 0, 5]
        #print('time is: ' + str(time.time()))
        #toggleLive()
        #print('live: ' + str(isLive()))
        #writeOrder(order)

a = flaskKit("127.0.0.1", 8080, gameLoop.packet())
a.startUp()
        