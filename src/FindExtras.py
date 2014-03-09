# -*- coding: utf-8 -*-

# created by Timothy Schellin
# suprisingly I did not use anyone elses source code...
# however I fear I might have reinvented the wheel for a few methods
# Lots of fun math here, and copius documentation!

import math
import os

sourceAlt = 1787

sourceLon = 34.1421
sourceLat = -117.6227

pointOrigin=[sourceLon,sourceLat]

# a method will need to be created to find the closest points using the calcDistance method
pointClose=[1,1]
pointN1=[4,2]
pointN2=[1,3]

#   formula for heading: θ = atan2( sin(Δλ).cos(φ2), cos(φ1).sin(φ2) − sin(φ1).cos(φ2).cos(Δλ) )
def calcHeading(newLon,newLat):
    y=math.sin(newLon-sourceLon)*math.cos(newLat)
    x=math.cos(sourceLat)*math.sin(newLat)- math.sin(sourceLat)*math.cos(newLat)*math.cos(newLon-sourceLon)
    heading =math.degrees(math.atan2(y,x))
    return heading

#   distance formula: √([x2-x1]²+[y2-y1]²)
def calcDistance(point1,point2):
    try:
        distance = (math.sqrt(((point2[0]-point1[0])**2)/((point2[1]-point1[1])**2)))*57.296
        return distance
    except:
        print("method calcDistance says: arguments must be passed in an array/list or tuple")

#   a formula too long to type
def calcOceanDistance(newLon,newLat):
    #not finished
    cod = 'not finished'
    points = open('c:\Users\Tim\Desktop\oceanPoints.txt', "r") #a text file I created that lists points along the Pacific ocean coast in lat/lon
    pointsln = points.readlines()
    distanceArray = []
    for line in points:
        count=0
        pointsln[count]
    #after finding angles

#   vector=< x2-x1, y2-y1 >
def createVectors(point1,point2):
    try:
        vector = [point2[0]-point1[0],point2[1]-point1[1]]
        return vector
    except:
        print("method createVectors says: arguments must be passed in an array/list or tuple")
    
#   finds the dot product of two vectors: a · b = ax × bx + ay × by
def calcDotProduct(vector1,vector2):
    try:
        dotProduct = (vector1[0]*vector2[0]+vector1[1]*vector2[1])
        return dotProduct
    except:
        print("method calcDotProduct says: arguments must be passed in an array/list or tuple")


def findAltitude():
    altitude = "altitude method not created yet"
    return altitude

#   this method is suppose to append the extra values into the first line of zipcode.txt files
def addExtras():
    empty = ""
    return empty

#Below here is the main part of the module

zipfile = open('C:\Users\Tim\Documents\GitHub\CS454-Beautiful-Data-Project\91764.txt')
filetxt = zipfile.readlines()
firstline=str(filetxt[0])
linef=firstline.split(",")
thislat=linef[4].split("\n")

#establish newLon and newLat
newLon=float(linef[3])
newLat=float(thislat[0])
newPoint=[newLat,newLon]
print newPoint

#method calls
theHeading = calcHeading(newLon,newLat)
print str(theHeading)+(" degrees relative to true north")
theDistance = calcDistance(pointOrigin,newPoint)
print str(theDistance)+(" miles")
theAltitude = findAltitude()
print theAltitude



vector_Pc_to_Po=createVectors(pointClose,pointOrigin)
print vector_Pc_to_Po
vector_P1_to_Pc=createVectors(pointN1,pointClose)
print vector_P1_to_Pc
dotProduct1=calcDotProduct(vector_Pc_to_Po,vector_P1_to_Pc)
print dotProduct1
