import urllib.request
import json
import time
from datetime import datetime
import csv

def DMS(Decimal):
    d = int(float(Decimal))#we get degrees
    m = int((float(Decimal) - d) * 60)#we get minutes
    s = (float(Decimal) - d - m/60) * 3600.00#we get seconds
    z= round(s, 2) #rounding s 
    if d >= 0:
        return str("N "+ str(abs(d))+ "º "+ str(abs(m))+ "' "+ str(abs(z))+ '" ')# for positive N
    else:
        return str("S "+ str(abs(d))+ "º "+ str(abs(m))+ "' "+ str(abs(z))+ '" ')# for negative S


with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Date and  Time", "Latitute","Longitude"])
    while 1 : #the loop creates a new csv row and updates the values every 5 seconds
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")# get date and time

        req = 'http://api.open-notify.org/iss-now.json'
        response = urllib.request.urlopen(req)
        obj = json.loads(response.read())

        tms=obj['timestamp']# get timestamp
        lat=DMS(obj['iss_position']['latitude'])# get latitude in DMS
        lon=DMS(obj['iss_position']['longitude'])# get longitude in DMS

        writer.writerow([tms,dt,lat,lon]) #create new row
        time.sleep(5)#delay of 5 s

