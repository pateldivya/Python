import urllib

def read_text():
    quotes = open("E:\python_programs\trial.txt")
    file = quotes.read()
    print(file)
    quotes.close()
    checkProfanity(file)

def checkProfanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
    print(connection.read())
    connection.close()

read_text()
