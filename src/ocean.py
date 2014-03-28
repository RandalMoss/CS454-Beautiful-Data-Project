import os
import time
pointOrigin=[34.1,-117.2]


def main(pointOrigin):
    coast=open('../OceanPoints.txt')
    coastline=coast.readlines()
    shoreMatrix=range(len(coastline))
    for lines in range(0, len(coastline)):
        shoreMatrix[lines]=coastline[lines].rstrip().split(',')
    for i in range(0,len(coastline)):
        oceanLon=shoreMatrix[i][1]
        oceanLat=shoreMatrix[i][2]
        pointOcean=[float(oceanLon),float(oceanLat)]
        cdist = (pointOrigin[1]*pointOcean[0])
        shoreMatrix[i][0]=cdist

        print pointOcean
        print '^ pointOcean'
    print shoreMatrix





        
        # SORTING ALGORITHM
        # SORTING ALGORITHM
        #sortedMatrix=[[1,34.0,-116.0],[2,34.5,-116.2],[1,35.9,-118.1]]
        #pointClosest=[sortedMatrix[0][1],sortedMatrix[0][2]]
        #pointN1=[sortedMatrix[1][1],sortedMatrix[1][2]]
        #pointN2=[sortedMatrix[2][1],sortedMatrix[2][2]]
        #vCO=createVectors(pointClosest,pointOrigin)
        #vCN1=createVectors(pointClosest,pointN1)
        #vCN2=createVectors(pointClosest,pointN2)
        #theta1=calcAngle(vCO,vCN1)
        #theta2=calcAngle(vCO,vCN2)
        #if(theta1>=90 and theta2>=90):
            #pointIntersect=pointClosest
        #elif(theta1>theta2):
            #use ASA law of sines
            #print 'else if'
        #else:
            #print 'else'
            #use ASA law of sines
        #return pointIntersect
main(pointOrigin)

