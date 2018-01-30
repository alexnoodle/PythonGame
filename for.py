#for.py
#Details
#Activity
#YESTERDAY


#Jack D'Amelio uploaded an item
#Sat 10:36 PM
#Text
#for.py
#No recorded activity before December 10, 2016
#All selections cleared
#New Team Drive




from sys import argv
import os


#for the sheet parameter the entire path needs to be included
def writeToSheet(sheet, row, col, content, numRow):
	writeSheet = open(sheet, 'r')
	wanted = ''
	for i in range(numRow):
		if i == int(row):
			goodRow = writeSheet.next().split()
			goodRow[col] = content
			for j in range(len(goodRow)):
				wanted = (wanted + str(goodRow[j]) + " ")
			wanted = wanted + '\n'
		else:
			wanted = (wanted + writeSheet.next())
	writeSheet = open(sheet, 'w')
	writeSheet.write(wanted)
	writeSheet.close()


def readFromsheet(sheet, row, column):
#pass in full path to sheet
	line = []
	dockSheet = open(sheet, 'r')
	for i in range(int(row)):
		line = dockSheet.next().split()
		
	return line[column]


#This only works for the User sheets
def addRow(sheet, ident):
	addSheet = open(sheet, 'r')
	firstRow = addSheet.next().split()
	add = len(firstRow) - 1
	addSheet = open(sheet, 'a')
	addSheet.write(str(ident))
	for i in range(add):
		addSheet.write(' ' + '0')
	addSheet.close()	


def createNewPlayer(username, password):
	newID = readFromsheet
	UIS1 = open(userInformationSheet, 'r+')
	lastLine = []
	for i in range(numRow(userInformationSheet)):
		lastLine = UIS1.next().split()
	newID = int(lastLine[0])+1
	UIS1.write(str(newID) + " " + username + " " + password + " " + '0')
	UIS1.close()


	URS1 = open(userResourceSheet, 'a')
	newLine = str(newID) + " "
	for i in range(numCol(userResourceSheet)-1):
		newLine += '0' + " "


	URS1.write(newLine)
	URS1.close()


	UCS1 = open(userConverterSheet, 'a')
	newLine = str(newID) + " "
	for i in range(numCol(userConverterSheet)-1):
		newLine += '0' + " "


	UCS1.write(newLine)
	UCS1.close()


def vote():
	print("TODO")
	return True
def calcPrice():
	print("TODO")
def calcPrice0():
	print("TODO")
def newConverter(name, outputID, inputQT, outputQT):
	print("TODO")


def newResource(name):
	 
	if vote():
		
		newID = int(numRow(resourceSheet))
		RS1 = open(resourceSheet, 'a')
		RS1.write(str(newID) + " " + str(name) + "\n")
		return 0
	else: 
		return -1

	#Column Format(ID, name, resourceInID, numIn, resourceOutID, numOut)
def newConverter(name, resourceInID, numIn, resourceOutID, numOut):
	 
	if vote():
		
		newID = int(numRow(converterSheet))
		CS1 = open(converterSheet, 'a')
		CS1.write(str(newID) + " " + str(name) + " " + resourceInID + " " + numIn + " " + resourceOutID + " " + numOut + "\n")
		return 0
	else: 
		return -1









def addColumn(sheet, numRow):
	dockSheet = open(sheet, 'r')
	string = []
	for i in range (numRow):
			string.append(dockSheet.next()[:-1])
	newSheet = open(sheet, 'w')
	for i in range(numRow):
		newSheet.write(string[i]+ " " + "0" + "\n")


def sellResource(identUser, identResource, amount):
	price = getResourcePrice(identResource)
	price = int(price) * int(amount)
	QT = getUserResourceQT(identResource, identUser)
	if int(QT) - int(amount) >= 0:
		setBalance(identUser, (int(getBalance(identUser)) + int(price)))
		setMarketResourceQT(identResource, (int(QT) + int(amount)))
		setUserResourceQT(identResource, identUser, (int(getUserResourceQT(identResource, identUser)) - int(amount)))
	else:
		return -1


def buyResource(identUser, identResource, amount):
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


def getIdent(sheet, type, numRow):
	getSheet = open(sheet, 'r')
	want = -1
	wanted = []
	for i in range(numRow):
		wanted = getSheet.readline().split()
		for j in range(len(wanted)):
			if str(wanted[j]) == str(type):
				want = wanted[0]
	return want


def numRow(sheet):
	numRow = 0;
	file = open(sheet, 'r')
	while(True):
		try:
			waste = file.next()
			numRow += 1


		except StopIteration:
			return numRow


def numCol(sheet):
	numCol = 0
	file = open(sheet, 'r')
	return(len(file.next().split()))


def getResourcePrice(identResource):
	MRS1 = open(marketResourceSheet, 'r')
	toReturn = 0
	for i in range(numRow(marketResourceSheet)):
		line = MRS1.readline().split()
		if int(line[0]) == int(identResource):
			return line[2]


def getBalance(identUser):
	UIS1 = open(userInformationSheet, 'r')
	for i in range(numRow(userInformationSheet)):
		line = UIS1.readline().split()
		if int(line[0]) == int(identUser):
			return line[3]


def setBalance(identUser, newBalance):
	UIS1 = open(userInformationSheet, 'r')
	row = 0
	for i in range(numRow(userInformationSheet)):
		line = UIS1.readline().split()
		if int(line[0]) == int(identUser):
			writeToSheet(userInformationSheet, row, 3, newBalance, numRow(userInformationSheet))
		row = row + 1


def getMarketResourceQT(identResource):
	MRS1 = open(marketResourceSheet, 'r')
	for i in range(numRow(marketResourceSheet)):
		line = MRS1.readline().split()
		if int(line[0]) == int(identResource):
			return line[1]


def getUserResourceQT(identResource, identUser):
	URS1 = open(userResourceSheet, 'r')
	for i in range(numRow(userResourceSheet)):
		line = URS1.readline().split()
		if int(line[0]) == int(identUser):
			return line[identResource + 1]


def setUserResourceQT(identResource, identUser, newQT):
	URS1 = open(userResourceSheet, 'r')
	row = 0
	for i in range(numRow(userResourceSheet)):
		line = URS1.readline().split()
		if int(line[0]) == int(identUser):
			writeToSheet(userResourceSheet, row, identResource + 1, newQT, numRow(userResourceSheet))
		row = row + 1


def setMarketResourceQT(identResource, newQT):
	MRS1 = open(marketResourceSheet, 'r')
	row = 0
	for i in range(numRow(marketResourceSheet)):
		line = MRS1.readline().split()
		if int(line[0]) == int(identResource):
			writeToSheet(marketResourceSheet, row, 1, newQT, numRow(marketResourceSheet))
		row = row + 1


def main():
	# coding: utf-8


	#Setup Environment
	homeDir = os.makedirs(os.path.dirname(os.path.realpath(argv[1])) +"\\"+"gameDir")
	homeDirPath = os.path.dirname(os.path.realpath(argv[1])) +"\\"+"gameDir" + "\\"


	global userInformationSheet
	userInformationSheet = homeDirPath + "UIS1.bbz"


	global userResourceSheet
	userResourceSheet =	homeDirPath + "URS1.bbz"


	global userConverterSheet
	userConverterSheet = homeDirPath + "UCS1.bbz"
	
	global resourceSheet
	resourceSheet =	homeDirPath + "RS1.bbz"
	
	global converterSheet
	converterSheet = homeDirPath + "CS1.bbz"
	
	global marketConverterSheet
	marketConverterSheet =	homeDirPath + "MCS1.bbz"
	
	global marketResourceSheet
	marketResourceSheet = homeDirPath + "MRS1.bbz"




	#Setup User Information Sheet 1(UIS1)
	playerTable = open(argv[1], 'r')
	iPlayer = int(playerTable.next())
	UIS1 = open(userInformationSheet, 'w+')




	for i in range(iPlayer - 1):
		#Column Format(ID, name,password, balance)
		bucket = playerTable.next()
		UIS1.write(str(i) + " " + bucket[0:len(bucket) - 1] + " " + str(0) + '\n')
	UIS1.write(str(iPlayer - 1) + ' ' + playerTable.next() + ' ' + str(0) + '\n')
	
	playerTable.close()
	UIS1 = open(userInformationSheet, 'w+')
	UCS1 = open(userConverterSheet, 'w+')
	URS1 = open(userResourceSheet, 'w+')












	for i in range(iPlayer):
		playerLine = UIS1.next().split()
		UCS1.write(str(playerLine[0]) + " " + str(0) + '\n')
		#Column Format(player, ID, resource0 quantity-resourceN quantity)
		URS1.write(playerLine[0] + ' ' + str(0) + '\n')




	#Setup Resource Sheet 1(RS1)	
	notResource = "String"
	RS1 = open(resourceSheet, 'w+')
	#Resource Format(ID, name)
	RS1.write(str(0) + " " + notResource + "\n")




	#Setup Converter Sheet 1(CS1)
	notConverter = "String1"
	CS1 = open(converterSheet, 'w+')
	#Column Format(ID, name, resourceInID, numIn, resourceOutID, numOut)








	#Setup Market Resource Sheet 1(MSR1)
	MRS1 = open(marketResourceSheet, 'w+')
	#Column Format(ID, quantity, price)
	MRS1.write(str(0) + " " + str(0) + " " +  str(0))
	#Setup Market Converter Sheet 1(MS1)
	MCS1 = open(marketConverterSheet, 'w+')
	#Column Format(ID, quantity, price)
	MCS1.write(str(0) + " " + str(0) + " " + str(1))

	UIS1.close()
	URS1.close()
	UCS1.close()
	CS1.close()
	RS1.close()
	MCS1.close()
	MRS1.close()

	createNewPlayer("Mom", "dadissad")
	newResource("sadness")

main()