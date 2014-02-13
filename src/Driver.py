import Collect
class Driver():
    def __init__(self):
        print "Reading config.txt file"
        self.readConfigFile()
        source = self.info[0]
        radius = self.info[1]
        print "Collect data from source weather station start..."
        Collect.getSensorData
        print "Collect data finished"
        print "Gathering zipcodes from around source with radius " + str(radius)
        zipcodes = Collect.ZipcodeScraper.getZipCodes(source, radius)
        print zipcodes
        print "Zipcode gathering complete"
        print "Getting weather data for each zipcode..."
        for zipcode in zipcodes:
            Collect.getWeatherData(zipcode)
            
            
    def readConfigFile(self):
        self.info = []
        count = 0
        f = open('../config.txt', 'r')
        for line in f:
            stringArray = line.split()
            self.info.insert(count, stringArray[2])
            count += 1
        f.close()
        
        for line in self.info:
            print line
Driver()