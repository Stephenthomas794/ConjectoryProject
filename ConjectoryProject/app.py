"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#Libaries 
from flask import Flask
import requests 

#Create App
app = Flask(__name__)

#Variables
#htmlString = "www.whateverurlyouwant.com/A100706#A002275"
#matchString = "A002275"
sequence1 = "http://www.oeis.org/A100706"
sequence2 = "http://www.oeis.org/A002275"

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#Routing to Main Page
@app.route('/')
def SidMethod():
    r = requests.get("http://oeis.org/A100706")
    #searchURLString(htmlString,matchString)
    if (crossURLSequenceMatch(sequence1, sequence2)):
        return "True"
    return "False"

def searchURLString(htmlString,matchString):
    #Length of the Strings sent
    sizeHtml = len(htmlString)
    sizeMatch = len(matchString)
    #Total to search to avoid the last few letters, and avoid extra searching
    totalToSearch = (sizeHtml - sizeMatch) + 1
    #Main counter for the htmlString 
    counter = 0
    #Counter for the matchString
    counterTwo = 0
    #Continue to loop and incrase counter by one till **almost the entire htmlString is done
    while (counter <= totalToSearch):
        for letter in htmlString:
            if (letter == matchString[counterTwo]):
                counterTwo = counterTwo + 1
                #size and every letter of the matchString has been found in htmlString
                if (counterTwo == sizeMatch):
                    return True
                    break
            #counter for matchString gets reset
            elif (letter != matchString[counterTwo]):
                counterTwo = 0
            counter = counter + 1
    return False

def crossURLSequenceMatch(sequence1, sequence2):
    #Make Request to both webpages
    one = requests.get(sequence1)
    two = requests.get(sequence2)
    #Convert both webpages to text
    oneText = one.text
    twoText = two.text
    #Break the URL for the SubStrings we are cross referencing for
    searchOne = sequence1[20:]
    searchTwo = sequence2[20:]
    #Cross reference
    if (searchURLString(oneText,searchTwo)):
        return True
    elif (searchURLString(twoText,searchOne)):
        return True
    else:
        return False
    return False

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
