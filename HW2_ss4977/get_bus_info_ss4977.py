#!/usr/bin/python
## Python 3 print function
from __future__ import print_function
import os
import os.path
import sys
import re
import urllib2
# Prepare to convert the response from the MTA server to a dictionary
import json

mtakey = sys.argv[1]
busroute = sys.argv[2]
outfile = sys.argv[3]
if re.match(r"[\d\-a-f]{20,}", mtakey):
    # Argument is given in form of MTA API key
    pass
else:
    # Argument is a file name which contains the key
    if os.path.isfile(mtakey):
        # Check that the file exists, otherwise report its absence and exit
        if os.access(mtakey, os.R_OK):
            # Similarly if the file exists but is not readable
            fh = open(mtakey, "r")
            fstr = fh.readline()
            fstr = re.sub(r'[\r\n]+', "", fstr)
            if re.match(r"[\d\-a-f]{20,}$", fstr):
                mtakey = fstr
            else:
                print(mtakey + " does not contain a valid key\n")
                sys.exit()
        else:
            print("Could not open file " + mtakey + "\n")
            sys.exit()
    else:
        print(mtakey + " is not an API key and is not a file\n")
        sys.exit()

site = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
daturl = site + "?key=" + mtakey + "&LineRef=" + busroute

site = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
daturl = site + "?key=" + mtakey + "&LineRef=" + busroute

# Get the data from the server
try:
    fh = urllib2.urlopen(daturl)
    # If this works, just read what it returns
    datstr = fh.readline()
except urllib2.URLError:
    # A possible source of an error is trying to use a proxy
    # This routine from https://www.decalage.info/en/python/urllib2noproxy
    # bypasses the proxy
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(daturl)
    r = opener.open(req)
    datstr = r.read()
# Converts response from the server into dictionary
datstruct = json.loads(datstr)
# Traverse the data structure to the list of active buses
substruct = datstruct["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"]
vehlist = substruct[0]["VehicleActivity"]
dests = {}

fh = open(outfile, "w")
fh.write("Latitude,Longitude,Stop Name,Stop Status\n")
com = ','
for i in range(len(vehlist)):
    vehdat = vehlist[i]["MonitoredVehicleJourney"]
    lat = vehdat["VehicleLocation"]["Latitude"]
    lon = vehdat["VehicleLocation"]["Longitude"]
    posdat = vehdat["OnwardCalls"]
    stName = "N/A"
    stDist = "N/A"
    if "OnwardCall" in posdat.keys():
        stName = posdat["OnwardCall"]["StopPointName"]
        stDist = posdat["OnwardCall"]["Extensions"]["Distances"]["PresentableDistance"]
    fh.write(com.join([str(lat), str(lon), stName, stDist]))
    fh.write("\n")

