'''
This generates an URL that can be pasted in a browser to obtain json file of elevations of different locations as defined
by a grid of which the N, S, E, W corners are given.

Google Maps Path: https://maps.googleapis.com/maps/api/elevation/json?locations=-33.941033,18.457269|-34.075809,18.296103&key=AIzaSyDkVBeSmR4wP1YpC7weGvIbvJnLsXyTE_Y
'''


import webbrowser
import os
import numpy as np
import matplotlib.pyplot as plt


def CreateGrid_aslist(N,S,W,E,size=19):
    #generate list running N->S for each longitude
    lat = np.around(np.linspace(N, S, size, endpoint=True), decimals=6)
    lng = np.around(np.linspace(W, E, size, endpoint=True), decimals=6)

    listCoord = []
    for col in range(size):
        for row in range(size):
            listCoord.append(str(lat[row])+','+str(lng[col]))

    return listCoord

def genURL(listCoord):
    prefix = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
    suffix = '&key=AIzaSyDkVBeSmR4wP1YpC7weGvIbvJnLsXyTE_Y'
    #from list to single string seperated by |
    locations = '|'.join(listCoord)

    url_maps = prefix + locations + suffix
    chars = len(url_maps)

    return url_maps, chars


def main():
    Gridlist = CreateGrid_aslist(
        -33.773648,
        -34.373648,
        18.127227,
        18.727227
        )

    URL, Chars = genURL(Gridlist)
    print('Characters long: ' + str(Chars))
    print(URL)
    #webbrowser.open(URL)

if __name__ == '__main__':
    main()
