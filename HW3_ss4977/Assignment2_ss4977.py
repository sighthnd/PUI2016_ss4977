#!/usr/bin/python
# When trying to log in to finish this, I got the following:
#
# /usr/bin/xauth:  error in locking authority file /home/cusp/ss4977/.Xauthority
# Warning: No xauth data; using fake authentication data for X11 forwarding.
#
# Cannot run Jupyter until that is fixed, edits have been done on github.
# Being unable to run Jupyter, I'm trying a python script outside,
# which unfortunately will not be able to show graphics, but can at least
# test most of what needs to be done.
from __future__ import print_function
import os
import sys
import numpy as np
import pandas as pd
import datetime
#import pylab as pl
#%pylab inline

puidata = os.getenv("PUIDATA")
sitename = "http://s3.amazonaws.com/tripdata"
bikemon = "201508" # Would like this to be settable during runtime
# Define corners of Midtown
nwcorn = (40.7693944, -73.9870549) # W 59th & 8th
swcorn = (40.7544542, -73.99989933)# W 36th & 8th
secorn = (40.7475701, -73.9742955) # E 36th & 2nd
necorn = (40.7591923, -73.9665707) # E 59th & 2nd
boundary = (nwcorn, swcorn, secorn, necorn)

def getBikeDataCSV(mon):
    # Based loosely on Federica's code
    basename = mon + "-citibike-tripdata"
    zipname = basename + ".zip"
    os.chdir(puidata) # Now all file operations without an absolute path will take place in puidata
    fullfile = puidata + "/" + zipname
    # Check if the file is present
    print("Checking presence of " + zipname)
    print(os.getenv("PWD"))
    if os.path.isfile(basename + ".csv"):
        print("Found file " + basename + ".csv")
        if os.path.isfile(mon + "-citibike-tripdata.csv"):
            if os.system("mv " + mon + "-citibike-tripdata.csv " + puidata):
                print("Could not move file to " + puidata)
                return
    else:
        print("Downloading file " + zipname)
        if not os.path.isfile(fullfile):
            os.system("curl -O " + sitename + "/" + zipname)
            if os.path.isfile(fullfile):
                print("Got " + zipname + "\n")
                os.system("unzip -q " + fullfile)
            else:
                print("Failed\n")
                return

def in_rect(ptlat, ptlon, contour):
    # ptlat - scalar latitude of the coordinate being tested
    # ptlon - scalar longitude of the coordinate being tested
    # contour - tuple of coordinates bounding polygon
    # First look for two pairs of points in contour where
    # which ptlat is between
    bet_segs = []
    eq_pt = []
    try:
        for corner in range(0, len(contour)):
            if between(ptlat, contour[corner][0], contour[(corner + 1) % len(contour)][0]):
                bet_segs.append(corner)
            elif ptlat == contour[corner][0]:
                eq_pt.append(corner)
    except ValueError:
        return False
    # If there were no segments, return False
    if len(bet_segs) <= 1 and len(eq_pt) == 0:
        return False
    # If there is one equal to a vertex and none inside segment,
    # return whether it is on the vertex
    if len(eq_pt) == 1 and len(bet_segs) == 0:
        return ptlon == contour[eq_pt[0]][1]
    # If there are two equal to a vertex and none inside segment,
    # return whether it is on the line connecting those vertices, including ends
    if len(eq_pt) == 2 and len(bet_segs) == 0:
        return between(ptlon, contour[eq_pt[0]][1], contour[eq_pt[1]][1]
                      ) or ptlon == contour[eq_pt[0]][1] or ptlon == contour[eq_pt[1]][1]
    # If there are two or more segments, find the longitude-intercepts
    # for each of those segments with the latitude and return whether or
    # not the point is on a longitude in between
    if len(bet_segs) >= 2:
        xint_list = []
        # Find the longitude on each segment in the list intersecting the latitude
        for ver in bet_segs:
            xint = x_intercept(ptlat, ptlon, (contour[ver], contour[(ver+1) % len(contour)]))
            xint_list.append(xint)
        lessthan_lon = 0
        # If the number of segments with an x-intercept greater than the points x-coordinate
        # is odd, the point is in the polygon
        for xi in xint_list:
            if xi == ptlon:
                # On the segment
                return True
            if xi < ptlon:
                lessthan_lon += 1
        return (lessthan_lon % 2) == 1

def x_intercept(ptlat, ptlon, seg_ends):
    # Return the x-coordinate of the segment defined by seg_ends that has a y-coordinate of ptlat
    if seg_ends[0][0] == seg_ends[1][0]:
        if ptlat == seg_ends[0][0]:
            if between(ptlon, seg_ends[0][1], seg_ends[1][1]):
                return ptlon
            else:
                return Null
        else:
            return Null
    if seg_ends[0][1] == seg_ends[1][1]:
        return seg_ends[0][1]
    y_frac = (ptlat - seg_ends[0][0]) / (seg_ends[1][1] - seg_ends[0][1])
    x_int = seg_ends[0][1] + y_frac * (seg_ends[1][1] - seg_ends[0][1])
    return x_int

def between (compare, st, en):
    if st < compare and compare < en:
        return True
    if en < compare and compare < st:
        return True
    return False

getBikeDataCSV(bikemon)
bamboo = pd.read_csv(puidata + "/" + bikemon + "-citibike-tripdata.csv")
# Remove the unneeded fields
bamboo = bamboo.drop(["tripduration", "bikeid", "usertype", "birth year", "gender"], axis=1)
# Create the fields that will hold the calculated values whether the start and end are in Midtown
bamboo["st_in"] = pd.Series(np.zeros(len(bamboo["starttime"])))
bamboo["en_in"] = pd.Series(np.zeros(len(bamboo["starttime"])))
print("Selecting by location")
# Previously, there was a bug in the in_rect() subroutine that prevented getting accurate assessments
# of what was in Midtown. It was fixed offline, but could not test it with pandas due to Xauth problem on gw
bamboo.loc[in_rect(bamboo["end station latitude"], bamboo["end station longitude"],
                   boundary), "en_in"] = 1
bamboo.loc[in_rect(bamboo["start station latitude"], bamboo["start station longitude"],
                   boundary), "st_in"] = 1
print("Identified points in and out of Midtown")
print(bamboo.shape)
print(bamboo.head(5))
"""
print(bamboo["start station name"][0])
print(bamboo["start station latitude"][0])
print(bamboo["start station longitude"][0])
chk = in_rect(bamboo["start station latitude"][0], bamboo["start station longitude"][0], boundary)
if chk:
    print("In")
else:
    print("Out")
print(bamboo["st_in"])
if not chk:
    bamboo["st_in"][0] = 0
"""
# Hmm, the update of st_in and en_in did not seem to work, will try doing
# things manually
station_conds = {}
for row in range(0, len(bamboo["st_in"])):
    name = bamboo["start station name"][row]
    if name in station_conds.keys():
        bamboo["st_in"][row] = station_conds[name]
    else:
        lat = bamboo["start station latitude"][row]
        lon = bamboo["start station longitude"][row]
        if in_rect(lat, lon, boundary):
            bamboo["st_in"][row] = 1
            station_conds[name] = 1
        else:
            bamboo["st_in"][row] = 0
            station_conds[name] = 0
    name = bamboo["end station name"][row]
    if name in station_conds.keys():
        bamboo["en_in"][row] = station_conds[name]
    else:
        lat = bamboo["end station latitude"][row]
        lon = bamboo["end station longitude"][row]
        if in_rect(lat, lon, boundary):
            bamboo["en_in"][row] = 1
            station_conds[name] = 1
        else:
            bamboo["en_in"][row] = 0
            station_conds[name] = 0
# Remove all entries where both ends either are both in Midtown or both not in Midtown
dFrame = bamboo[bamboo["st_in"] != bamboo["en_in"]]
print(dFrame.head(5))
print("Reduced dataset")
# Identify which entries are on days of the week and hours of interest
dFrame["st_date"] = pd.to_datetime(dFrame["starttime"])
dFrame["en_date"] = pd.to_datetime(dFrame["stoptime"])
for nkey in "weekday", "day", "sttime", "etime":
    dFrame[nkey] = pd.Series(np.zeros(len(dFrame["st_date"])))
"""
pd.Series.dt is not working, will have to workaround manually
dFrame["weekday"] = dFrame["st_date"].dt.weekday
dFrame["day"] = dFrame["st_date"].dt.day
dFrame["sttime"] = dFrame["st_date"].dt.hour
dFrame["etime"] = dFrame["en_date"].dt.hour
"""
print(type(dFrame["st_date"][0]))
#print(dFrame["st_date"][0].weekday) # Not working
for row in range(0, len(dFrame["sttime"])):
    # dFrame["weekday"][row] = dFrame["st_date"][row].weekday
    # Not working, urrrgghh
    dFrame["day"][row] = dFrame["st_date"][row].day
    dFrame["sttime"][row] = dFrame["st_date"][row].hour
    dFrame["etime"][row] = dFrame["en_date"][row].hour
print(dFrame.shape)
print(dFrame.head(5))
shoots = dFrame.loc[(dFrame["weekday"] < 5) &
                    (((dFrame["sttime"] >= 7) & (dFrame["sttime"] < 10) |
                     ((dFrame["etime"] >= 7) & (dFrame["etime"] < 10))))]
shoots.head(10)
dFrame.head(10)
# Calculate aggregated statistics. Will test when X is working from gw
enter = shoots[shoots["en_in"] == 1]
leave = shoots[shoots["st_in"] == 1]
enter_stats = enter.groupby(['day', 'sttime']).agg({'en_in': [np.size]})
leave_stats = leave.groupby(['day', 'sttime']).agg({'st_in': [np.size]})
print(enter.shape)
print(leave.shape)
