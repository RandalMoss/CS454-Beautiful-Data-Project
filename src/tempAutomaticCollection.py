import Driver
import time

def executeSomething():
    Driver.Driver().run('C:\Users\yehch_000\Documents\PythonWorkSpace\CS454-Beautiful-Data-Project\config.txt')
    print "The code run at: ", time.asctime(time.localtime(time.time()))   
    time.sleep(10)

while True:
    executeSomething()