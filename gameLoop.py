from sys import argv
import time
import os
import shutil
import flask_app
import threading


def actualGame(turnTimer):
    toggleLive()
    startTime = time.time()
    if(checkBuffer()):
		loadBuffer()

    while(time.time()-startTime < turnTimer):
		if(checkQueue()):
		    parseOrder(queuePath + '\\' + getNextInQueue())
		    os.remove(queuePath + '\\' + getNextInQueue())

    toggleLive()
    convert()
	#calcPrice()



def checkBuffer():
	temp = os.listdir(bufferPath)
	if len(temp) > 1:
		return  True
	else:
		return False

def checkQueue():
	temp = os.listdir(queuePath)
	if len(temp) > 1:
		return  True
	else:
		return False

def loadBuffer():
	bufferList = os.listdir(bufferPath)
	for i in range (len(bufferList)):
		shutil.move(bufferPath + '\\' + bufferList[i], queuePath + '\\')




def getNextInQueue():
	temp = os.listdir(queuePath)
	return temp[1]


def isLive():
	status = open(liveStatus, 'r')
	if int(status.next()) == 1:
		return True
	else:
		return False

def toggleLive():
	status = open(liveStatus, 'r')
	if int(status.readline()) == 1:
		status = open(liveStatus, 'w')
		status.write("0")
	else:
		status = open(liveStatus, 'w')
		status.write("1")


#for the sheet parameter the entire path needs to be included

#pass in full path to sheet
	line = []
	dockSheet = open(sheet, 'r')
	for i in range(int(row)):
		line = dockSheet.readline().split()

	if int(row) == 0:
		line = dockSheet.readline().split()

	return line[int(column)]



#todo
def sellConverter(identUser, identConverter, amount):
    price = getConverterPrice(identConverter)
    price = int(price) * int(amount)
    QT = getUserConverterQT(identConverter, identUser)
    if int(QT) - int(amount) >= 0:
        setBalance(identUser, (int(getBalance(identUser)) + int(price)))
        setUserConverterQT(identConverter, identUser, (int(getUserConverterQT(identConverter, identUser)) - int(amount)))
    else:
        return -1


#todo
def buyConverter(identUser, identConverter, amount):
    price = getConverterPrice(identConverter)
    price = int(price) * int(amount)
    balance = getBalance(identUser)
    if int(balance) >= int(price):
        setBalance(identUser, (int(balance) - int(price)))
    else:
        return -1

def getConverterPrice(identConverter, pkt):
    return pkt.marketConverterSheet[(int(identConverter) * pkt.marketResourceSheetNumCol) + 2]


def getBalance(identUser, pkt):
	return pkt.userInformationSheet[(int(identUser) * pkt.userInformationSheetNumCol) + 3]


def setBalance(identUser, newBalance, pkt):
	pkt.userInformationSheet[(int(identUser) * pkt.userInformationSheetNumCol) + 3] = newBalance






def getUserConverterQT(identConverter, identUser, pkt):
    return pkt.userResourceSheet[(int(identUser) * pkt.userResourceSheetNumCol) + (identConverter * 2) + 1]




def setUserConverterQT(identConverter, identUser, newQT, pkt):
    pkt.userResourceSheet[(int(identUser) * pkt.userResourceSheetNumCol) + (identConverter * 2) + 1] = newQT

def writeToSheet(sheet, row, col, content, numRow):
	sheet[(row * numRow) + col] = content

#pass in full path to sheet
def readFromsheet(sheet, row, column, numRow):
	return sheet[(row * numRow) + column]

def createNewPlayer(username, password, pkt):
	newID = pkt.userInformationSheetNumRow + 1
	pkt.userInformationSheet.append(newID)
	pkt.userInformationSheet.append(username)
	pkt.userInformationSheet.append(password)
	pkt.userInformationSheet.append(0)

	pkt.userResourceSheet.append(newID)
	for i in range(pkt.userResourceSheetNumCol - 1):
		pkt.userResourceSheet.append(0)

	pkt.userConverterSheet.append(newID)
	for i in range(pkt.userConverterSheetNumCol - 1):
		pkt.userConverterSheet.append(0)

	pkt.userInformationSheetNumRow += 1
	pkt.userResourceSheetNumRow += 1
	pkt.userConverterSheetNumRow += 1

def vote():
	print("TODO1")
	return True
def calcPrice():
	print("TODO2")
def calcPrice0():
	print("TODO3")
def newConverter(name, outputID, inputQT, outputQT, pkt):
	print("TODO4")

def newResource(name, pkt):
	if vote():
		newID = pkt.resourceSheetNumRow
		pkt.resourceSheet.append(newID)
		pkt.resourceSheet.append(name)
		pkt.resourceSheetNumRow += 1
		return 0
	else: 
		return -1

	#Column Format(ID, name, resourceInID, numIn, resourceOutID, numOut)
def newConverter(name, resourceInID, numIn, resourceOutID, numOut, pkt):
	if vote():
		newID = pkt.converterSheetNumRow
		pkt.converterSheet.append(newID)
		pkt.converterSheet.append(name)
		pkt.converterSheet.append(resourceInID)
		pkt.converterSheet.append(numIn)
		pkt.converterSheet.append(resourceOutID)
		pkt.converterSheet.append(numOut)
		pkt.converterSheetNumRow += 1
		return 0
	else: 
		return -1

def sellResource(identUser, identResource, amount, pkt):
	price = getResourcePrice(identResource)
	price = int(price) * int(amount)
	QT = getUserResourceQT(identResource, identUser)
	if int(QT) - int(amount) >= 0:
		setBalance(identUser, (int(getBalance(identUser)) + int(price)))
		setMarketResourceQT(identResource, (int(QT) + int(amount)))
		setUserResourceQT(identResource, identUser, (int(getUserResourceQT(identResource, identUser)) - int(amount)))
	else:
		return -1

def buyResource(identUser, identResource, amount, pkt):
	price = getResourcePrice(identResource)
	price = int(price) * int(amount)
	balance = getBalance(identUser)
	QT = getMarketResourceQT(identResource)
	if int(balance) >= int(price) and int(QT) >= int(amount):
		setBalance(identUser, (int(balance) - int(price)))
		setMarketResourceQT(identResource, (int(QT) - int(amount)))
		setUserResourceQT(identResource, identUser, (int(getUserResourceQT(identResource, identUser)) + int(amount)))
	else:
		return -1

def getResourcePrice(identResource, pkt):
	return pkt.marketResourceSheet[(int(identResource) * pkt.marketResourceSheetNumCol) + 2]

def getBalance(identUser, pkt):
	return pkt.userInformationSheet[(int(identUser) * pkt.userInformationSheetNumCol) + 3]
	
def setBalance(identUser, newBalance, pkt):
	pkt.userInformationSheet[(int(identUser) * pkt.userInformationSheetNumCol) + 3] = newBalance

def getMarketResourceQT(identResource, pkt):
	return pkt.marketResourceSheet[(int(identResource) * pkt.marketResourceSheetNumCol) + 1]

def getUserResourceQT(identResource, identUser, pkt):
	return pkt.userResourceSheet[(int(identuser) * pkt.userInformationSheetNumCol) + int(identResource) + 1]

def setUserResourceQT(identResource, identUser, newQT, pkt):
	pkt.userResourceSheet[(int(identuser) * pkt.userInformationSheetNumCol) + int(identResource) + 1] = int(newQT)

def setMarketResourceQT(identResource, newQT, pkt):
	pkt.marketResourceSheet[(int(identResource) * pkt.marketResourceSheetNumCol) + 1] = int(newQT)





def convert():
	users = []
	for i in range(int(numRow(userInformationSheet))):
	    users.append(readFromSheet(userInformationSheet, i + 1, 0))
	converters = []

	for i in range(int(numRow(converterSheet))):
		converters.append(readFromSheet(converterSheet, i + 1, 0))

	for i in range(len(users)):

		for j in range(len(converters)):
			converterQT = int(readFromSheet(userConverterSheet, getRow(userConverterSheet, users[i]) + 1, (int(converters[j]) + 1)))

			if converterQT > 0:
				numIn = readFromSheet(converterSheet, converters[j], 3)
				resourceInID = readFromSheet(converterSheet, converters[j], 2)
				numOut = readFromSheet(converterSheet, converters[j], 5)
				resourceOutID = readFromSheet(converterSheet, converters[j], 4)

				for k in range(converterQT):
					userQt = getUserResourceQT(resourceInID, users[i])

					if int(userQt) >= int(numIn):
						setUserResourceQT(resourceInID, users[i], (int(userQt) - int(numIn)))
						setUserResourceQT(resourceOutID, users[i], (int(getUserResourceQT(resourceOutID, users[i])) + int(numOut)))
def calcPrice():
	resources = []
	for i in range(int(numRow(resourceSheet))):
		resources.append(readFromSheet(resourceSheet, i+1, 0))


	if int(amount) >= int(initPrice) / 10:
		writeToSheet(marketResourceSheet, getRow(marketResourceSheet, identResource), 2, int(initPrice) - (int(amount) * (1/2)))
	else:
		writeToSheet(marketResourceSheet, getRow(marketResourceSheet, identResource), 2, int(initPrice) / 10)


def getInitPrice(identResource):
	return (100 * int(identResource))



def calcPrice(initPrice, identResource):
	amount = getMarketResourceQT(identResource)
	if int(amount) >= int(initPrice) / 10:
		writeToSheet(marketResourceSheet, getRow(marketResourceSheet, identResource), 2, int(initPrice) - (int(amount) * (1/2)))
	else:
		writeToSheet(marketResourceSheet, getRow(marketResourceSheet, identResource), 2, int(initPrice) / 10)

def calcInitPrice(identResource):
	writeToSheet(marketResourceSheet, getRow(marketResourceSheet, identResource), 2, (100 * int(identResource)))

def parseOrder(sheet):
    toOpen = open(sheet, 'r')
    order = toOpen.next().split()
    if str(order[0]) == 'buy':
        if str(order[1]) == 'resource':
            buyResource(order[2], order[3], order[4])
        else:
            buyConverter(order[2], order[3], order[4])

    elif str(order[0]) == 'sell':
        if str(order[1]) == 'resource':
            sellResource(order[2], order[3], order[4])
        else:
            sellConverter(order[2], order[3], order[4])

    elif str(order[0]) == 'converter':
        newConverter(order[1], order[2], order[3], order[4], order[5])

    elif str(order[0]) == 'resource':
        newResource(order[1])
    toOpen.close()
    #elif str(order[0]) == 'vote':

class packet():
	print "If you re seeing this send help"
	def __init__(self, userInformationSheet = [], userInformationSheetNumCol = 4, userInformationSheetNumRow = 1,
		userResourceSheet = [] , userResourceSheetNumCol = 3, userResourceSheetNumRow = 1,
		userConverterSheet = [], userConverterSheetNumCol = 3, userConverterSheetNumRow = 1
		, resourceSheetNumCol = 2, resourceSheetNumRow = 1, resourceSheet = []
		, converterSheetNumCol = 6, converterSheetNumRow= 1, converterSheet = []
		, marketConverterSheetNumCol = 3, marketConverterSheetNumRow = 1
		, marketConverterSheet = [], marketResourceSheetNumCol = 3
		, marketResourceSheetNumRow = 1, marketResourceSheet = []):
		self.userInformationSheetNumCol = userInformationSheetNumCol
		self.userInformationSheetNumRow = userInformationSheetNumRow
		self.userInformationSheet = userInformationSheet

		self.userResourceSheetNumCol = userResourceSheetNumCol
		self.userResourceSheetNumRow = userResourceSheetNumRow
		self.userResourceSheet = userResourceSheet

		self.userConverterSheetNumCol = userConverterSheetNumCol
		self.userConverterSheetNumRow = userConverterSheetNumRow
		self.userConverterSheet = userConverterSheet

		self.resourceSheetNumCol = resourceSheetNumCol
		self.resourceSheetNumRow = resourceSheetNumRow
		self.resourceSheet = resourceSheet

		self.converterSheetNumCol = converterSheetNumCol
		self.converterSheetNumRow = converterSheetNumRow
		self.converterSheet = converterSheet

		self.marketConverterSheetNumCol = marketConverterSheetNumCol
		self.marketConverterSheetNumRow = marketConverterSheetNumRow
		self.marketConverterSheet = marketConverterSheet

		self.marketResourceSheetNumCol = marketResourceSheetNumCol
		self.marketResourceSheetNumRow = marketResourceSheetNumRow
		self.marketResourceSheet = marketResourceSheet

		
#for the sheet parameter the entire path needs to be included

def main():
	# coding: utf-8
	#Setup Environment
	pkt = packet()
	print type(pkt.userConverterSheet)
	#Setup User Information Sheet 1(UIS1)
	playerTable = open(argv[1], 'r')
	#print(type(playerTable))
	iPlayer = int(playerTable.next())
	pkt.userInformationSheetNumRow = iPlayer
	pkt.userResourceSheetNumRow = iPlayer
	pkt.userConverterSheetNumRow = iPlayer

	for i in range(iPlayer - 1):
		#Column Format(ID, name,password, balance)
		bucket = playerTable.next().split()
		pkt.userInformationSheet.append(i)
		pkt.userInformationSheet.append(bucket[0])
		pkt.userInformationSheet.append(bucket[1])
		pkt.userInformationSheet.append(0)
	bucket = playerTable.next().split()
	pkt.userInformationSheet.append(iPlayer - 1)
	pkt.userInformationSheet.append(bucket[0])
	pkt.userInformationSheet.append(bucket[1])
	pkt.userInformationSheet.append(0)
	print type(pkt.userConverterSheet)
	for i in range(iPlayer):
		pkt.userConverterSheet.append(i)
		pkt.userConverterSheet.append(0)
		#Column Format(player, ID, resource0 quantity-resourceN quantity)
		pkt.userResourceSheet.append(i)
		pkt.userResourceSheet.append(0)

	#Setup Resource Sheet 1(RS1)	
	notResource = "String"
	#Resource Format(ID, name)
	pkt.resourceSheet.append(0)
	pkt.resourceSheet.append(notResource)

	#Setup Converter Sheet 1(CS1)
	notConverter = "String1"
	pkt.converterSheet.append(0)
	pkt.converterSheet.append(notConverter)
	pkt.converterSheet.append(0)
	pkt.converterSheet.append(0)
	pkt.converterSheet.append(0)
	pkt.converterSheet.append(1)
	#Column Format(ID, name, resourceInID, numIn, resourceOutID, numOut)

	#Setup Market Resource Sheet 1(MSR1)
	#Column Format(ID, quantity, price)
	pkt.marketResourceSheet.append(0)
	pkt.marketResourceSheet.append(0)
	pkt.marketResourceSheet.append(0)
	#Setup Market Converter Sheet 1(MS1)
	#Column Format(ID, quantity, price)
	pkt.marketConverterSheet.append(0)
	pkt.marketConverterSheet.append(0)
	pkt.marketConverterSheet.append(0)

	createNewPlayer("Mom", "dadissad", pkt)
	newResource("sadness",pkt)

class someThread(threading.Thread):
	print 'I dont need parenthesisis'
	def __init__(self, pkt, host, p0rt):

		threading.Thread.__init__(self)
		self.pkt = pkt
		self.host = host
		self.port = p0rt

	def run(self):

		instance = flask_app.flaskKit(self.host, self.port, self.pkt)
		instance.startUp()

'''
if len(sys.argv) != 3:
            print('Usage: {0} host port'.format(sys.argv[0]), file=sys.stderr)
            exit()

'''
# make thread of flask
pkt =  packet()
print argv


instance = flask_app.flaskKit(self.host, self.port, self.pkt)
instance.startUp()
'''
a = someThread(pkt,argv[1], argv[2])

a.start()
'''
'''
counter = 0
while counter < 1:
    actualGame(1)
    counter += 1
    print(counter)
'''
