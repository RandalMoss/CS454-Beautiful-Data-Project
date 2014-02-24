"""
First line of the text file will be where is the data from, city,state, lat, long
After the first line, the rest will be data collected. Everyline will be an update
We will collect data every 2 hours
The other lines will be like, all separated by comma
time of data collected, time when the data is updated in the website, sunrise, sunset,
temp,condition,huminity,pressure,rising,visibility, wind chill,direction,speed
"""
import os
import time
import WebWeatherCollection as wwc

data = {}

def saveDataIntoText(name):
    text_file = open(getFileName(name), "a")
    text_file.write(time.strftime("%c")+","+data['condition']['date']+","+data['astronomy']['sunrise']+","+data['astronomy']['sunset']+","+data["condition"]["temp"]+","+data["condition"]["text"]+","+data["atmosphere"]["humidity"]+","+data["atmosphere"]["pressure"]+","+data["atmosphere"]["rising"]+","+data["atmosphere"]["visibility"]+","+data["wind"]["chill"]+","+data["wind"]["direction"]+","+data["wind"]["speed"]+"\n")
    text_file.close()
    
def readTextFile(name):
    print "TO DO :D"
    
def makeNewTextFile(name):
    nameofData = getFileName(name)
    if(os.path.exists(nameofData)):
#        print "File Already Exist"
        saveDataIntoText(name)
    else:
        open(nameofData,"w")
        makefirstline(name)
        saveDataIntoText(name)
#        print "File Created"

def makefirstline(name):
    text_file = open(getFileName(name), "a")
    text_file.write(data["title"][:14]+","+data["title"][17:-4]+","+data["title"][-2:]+","+data["geo"]["lat"]+","+data["geo"]["long"]+"\n")
    text_file.close()

def getFileName(name):
    workingpath = os.getcwd()[:-3]
    nameofData = workingpath+name+".txt"
    return nameofData

def main(zipcode):
    global data
    data = wwc.getWeatherData(zipcode)
    makeNewTextFile(zipcode)
        
main("91780")