from sys import argv
import os
import shutil

def createNewPlayer(username, password, userInformationSheet, userResourceSheet, userConverterSheet):
    newID = readFromsheet
    UIS1 = open(userInformationSheet, 'r+')
    lastLine = []
    if numRow(userInformationSheet)!= 0:

        for i in range(numRow(userInformationSheet)):
            lastLine = UIS1.next().split()
        newID = int(lastLine[0])+1
        UIS1.write(str(newID) + " " + username + " " + password + " " + '0' + "\n")
        UIS1.close()

    else:

        newID = 0
        UIS1.write(str(newID) + " " + username + " " + password + " " + '0'+ "\n")
        UIS1.close()

 #   RS1 = open(resourceSheet, 'r')
  #  print(RS1)
    URS1 = open(userResourceSheet, 'a')
    newLine = str(newID) + " "
   # print(resourceSheet)
    #print(numRow(resourceSheet))
    newLine += '1' + " "
    for i in range(numRow(resourceSheet)-1):
        newLine += '0' + " "
    newLine += "\n"
    URS1.write(newLine)
    URS1.close()


    UCS1 = open(userConverterSheet, 'a')
    newLine = str(newID) + " "
    if int(numRow(converterSheet)) == 0:
        UCS1.write(newLine + '1' + " " +"\n")
    else:
        newLine += '1' + " "
        for i in range(numRow(converterSheet)-1):
            newLine += '0' + " "


        UCS1.write(newLine + "\n")
    UCS1.close()

def readFromsheet(sheet, row):
#pass in full path to sheet
    line = []
    dockSheet = open(sheet, 'r')
    for i in range(int(row)):
        line = dockSheet.next().split()

    return line

def numRow(sheet):
    numRow = 0;
    file = open(sheet, 'r+')
    while(True):
        try:

            waste = file.next()
            numRow = numRow + 1
            #print(numRow)


        except StopIteration:
            return numRow

def numCol(sheet):
    numCol = 0
    file = open(sheet, 'r')
    try:
        return len(file.next().split())
    except StopIteration:
        return 0
def cleanUp():
      shutil.rmtree(os.path.dirname(os.path.realpath(argv[0]))+ "\\static")
def main():
    # coding: utf-8

    #Setup Environmentj
    homeDir = os.makedirs(os.path.dirname(os.path.realpath(argv[0]))+ "\\static" +"\\"+"gameDir")
    homeDirPath = os.path.dirname(os.path.realpath(argv[0]))+ "\\static" +"\\"+"gameDir" + "\\"


    global userInformationSheet
    userInformationSheet = homeDirPath + "UIS1.bbz"


    global userResourceSheet
    userResourceSheet =    homeDirPath + "URS1.bbz"


    global userConverterSheet
    userConverterSheet = homeDirPath + "UCS1.bbz"

    global resourceSheet
    resourceSheet =    homeDirPath + "RS1.bbz"

    global converterSheet
    converterSheet = homeDirPath + "CS1.bbz"

    global marketConverterSheet
    marketConverterSheet =    homeDirPath + "MCS1.bbz"

    global marketResourceSheet
    marketResourceSheet = homeDirPath + "MRS1.bbz"

    #Setup Resource Sheet 1(RS1)S
    RS1 = open(resourceSheet, 'w+')
    UIS1 = open(userInformationSheet, 'w+')
    UCS1 = open(userConverterSheet, 'w+')
    URS1 = open(userResourceSheet, 'w+')
    UIS1.close()
    UCS1.close()
    URS1.close()
    #Resource Format(ID, name)
    RS1.write(str(0) + " " + "notResource0" + "\n")
    RS1.write(str(1) + " " + "notResource1" + "\n")
    RS1.write(str(2) + " " + "notResource2" + "\n")
    RS1.write(str(3) + " " + "notResource3" + "\n")
    RS1.write(str(4) + " " + "notResource4" + "\n")
    RS1.close()
       #Setup Converter Sheet 1(CS1)
    notConverter = "String1"
    CS1 = open(converterSheet, 'w+')
    #Column Format(ID, name, resourceInID, numIn, resourceOutID, numOut)
    CS1.write("0 default 0 1 0 2")



    createNewPlayer("username1", "password", userInformationSheet, userResourceSheet, userConverterSheet)
    createNewPlayer("username2", "password", userInformationSheet, userResourceSheet, userConverterSheet)


    #Setup User Information Sheet 1(UIS1)





    #Setup Converter Sheet 1(CS1)
    notConverter = "String1"
    CS1 = open(converterSheet, 'w+')
    #Column Format(ID, name, resourceInID, numIn, resourceOutID, numOut)
    CS1.write("0 default 0 1 0 2")











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

    psow = open(homeDirPath + "liveStatus.txt", 'w')
    psow.write("1")
    os.makedirs(homeDirPath + "\\queue")
    os.makedirs(homeDirPath + "\\queue\\buffer")

    globalVars  = open(str(homeDirPath) + "globals.txt", 'w')
    globalVars.write(str(homeDirPath) + "\n")
    globalVars.write(userInformationSheet + "\n")
    globalVars.write(userResourceSheet + "\n")
    globalVars.write(userConverterSheet + "\n")
    globalVars.write(converterSheet + "\n")
    globalVars.write(resourceSheet + "\n")
    globalVars.write(marketConverterSheet + "\n")
    globalVars.write(marketResourceSheet + "\n")
    globalVars.write(homeDirPath + "queue" + "\n")
    globalVars.write(homeDirPath + "liveStatus.txt" + "\n")

cleanUp()
main()