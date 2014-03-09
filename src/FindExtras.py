# -*- coding: utf-8 -*-

#THIS IS EXTREMELY SLOPPY CODING. I apologise as I am not very familiar with Python
import math
import os

sourceLon = 34.1421
sourceLat = -117.6227
sourceAlt = 1787

#θ = atan2( sin(Δλ).cos(φ2), cos(φ1).sin(φ2) − sin(φ1).cos(φ2).cos(Δλ) )
def calcHeading(newLon,newLat):
    y=math.sin(newLon-sourceLon)*math.cos(newLat)
    x=math.cos(sourceLat)*math.sin(newLat)- math.sin(sourceLat)*math.cos(newLat)*math.cos(newLon-sourceLon)
    heading =math.degrees(math.atan2(y,x))
    return heading
zipfile = open('C:\Users\Tim\Documents\GitHub\CS454-Beautiful-Data-Project\91764.txt')
filetxt = zipfile.readlines()
firstline=str(filetxt[0])
linef=firstline.split(",")
thislat=linef[4].split("\n")

newLon=float(linef[3])
newLat=float(thislat[0])
print(newLon,newLat)
theHeading = calcHeading(newLon,newLat)
print theHeading #output at end of line one of files

def calcDistance(newLon,newLat):
    distance = math.sqrt(((newLat-sourceLat)**2)/((newLon-sourceLon)**2))
    return distance

def calcOceanDistance(newLon,newLat):
    points = open('c:\Users\Tim\Desktop\oceanPoints.txt', "r")
