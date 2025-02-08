# 
# Earth quake last 24 hours
#

import urllib.request 
import json
import datetime

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
 
    print(theJSON["metadata"]["title"])
    count  = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    print("Richter scale | time    | Place ")
    for i in theJSON["features"]:
        magnitude = i["properties"]["mag"] + 0.00 
        epoch = i["properties"]["time"]
        epoch_date_time = datetime.datetime.fromtimestamp(epoch/1000)  
        print('{0:.2f}'.format(magnitude), epoch_date_time, i["properties"]["place"])
 
def main():
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    # print ("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    printResults(data)

if __name__ == "__main__":
    main()
