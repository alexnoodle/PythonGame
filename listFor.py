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

class packet():
	''' Initializes every array for all the users information and game information
		Also includes values for the number of columns and rows for the arrays. The arrays are one dimensional
		but with the values they can be treated as two dimensional
	'''
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

		
#This changes one value in any array you choose
def writeToSheet(sheet, row, col, content, numRow):
	sheet[(row * numRow) + col] = content

#This returns one value from the chosen location
def readFromsheet(sheet, row, column, numRow):
	return sheet[(row * numRow) + column]

#This alters all of the user sheets to include the new user and his information
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

#Will have logic to collect votes from players and then implement the desired change or not
def vote():
	print("TODO1")
	return True

#Will have logic to calculate the price for a resource based on the amount of resource there is in the market
def calcPrice():
	print("TODO2")

#Will calculate the initial price of a new resource
def calcPrice0():
	print("TODO3")

#Will create the new resource in resource sheets and in the market
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
	#Puts a new converters information in the converter sheet and on the market
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

#Checks to see whether the user has enough of their resource to sell it and if so it removes the resource from the player,
#places it in the market, and gives the user money.
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

#Checks to see if the user has enough money, if so it removes the resource from the market, places it in the users sheet,
# and removes the money from the user.
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

def main():
	# coding: utf-8
	#Setup Environment
	pkt = packet()
	print(type(pkt.userConverterSheet))
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
	print(type(pkt.userConverterSheet))
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

#playerTable = open(argv[1], 'r')
#print(type(playerTable))
#iPlayer = int(playerTable.next())


main()


