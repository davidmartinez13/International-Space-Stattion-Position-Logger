# International-Space-Stattion-Position-Logger
Wrote a program that stores the location of the ISS in a CSV file in real time. 
It creates a CSV file, if it does not exists already. If the file exists, the program should append new information at the end of the file.
It contains: timestmap, datetime, latitude, longitude
If the program crashes/stop, the csv file should reamain uncorrupted.
The output file should be a valid CSV (every line is one log, first line is header).
The sampling frequency should be around 5s.
