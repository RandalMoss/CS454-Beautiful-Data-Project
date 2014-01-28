class Collect():
    def __init__(self):
        f = open('../Jan14log.txt', 'r')
        for line in f:
            print(line)
        f.close()