'''
Google Maps Path: https://maps.googleapis.com/maps/api/elevation/json?path=-33.941033,18.457269|-34.075809,18.296103&samples=300&key=AIzaSyDkVBeSmR4wP1YpC7weGvIbvJnLsXyTE_Y

'''

import json
import os
import matplotlib.pyplot as plt


def getElev(Path):
    File = json.loads(open(Path).read())
    # Create a dictionary for each results[] object
    elevationArray = []
    for resultset in File['results']:
        elevationArray.append(resultset['elevation'])

    return elevationArray
    
def plotElev(Elevs):
    plt.figure(1,figsize=(16,10))
    plt.subplot(111)
    plt.plot(Elevs)
    plt.show()


def main():
    Path = r'H:\11. Python Stuff\Playroom\GoogleMaps\TableMountandsea.json'
    Elevs = getElev(Path)
    plotElev(Elevs)


if __name__ == '__main__':
    main()
