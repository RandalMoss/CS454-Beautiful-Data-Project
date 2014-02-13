import ZipcodeScraper
import WebWeatherCollection as wwc

def getSensorData():
    f = open('../Jan14log.txt', 'r')
    for line in f:
        print(line)
    f.close()
    
def getZipCodesAroundRadius(source, radius):
    ZipcodeScraper.getZipCodes(source, radius)
    
def getWeatherData(zipcode):
    wwc.getWeatherData(zipcode)