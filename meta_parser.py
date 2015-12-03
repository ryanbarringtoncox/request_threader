#!/usr/bin/python
import os, glob, decimal, sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#config
#the_dir = 'aeroplane_out_files_1449159215'
the_dir = ''
graph_title = "Ebay Aeroplane Listings"

if  len(sys.argv) == 1:
  print "Need an input dir"
  print "  ..exiting."
  sys.exit()
else:
  the_dir = sys.argv[1]

os.chdir(the_dir)
first = 0
last = 0
no_number_files = []
files_with_zero_listings = []
graph_data = []

#check for numbers in string
def hasNumbers(inputString):
  return any(char.isdigit() for char in inputString)

listing_count = 0 #files with 'listingscnt' in DOM line
no_number_count = 0 #files with no number in listing
file_counter = 0 #overall file counter

for file in glob.glob('*'):

  timestamp = int(file.split('.')[1]) #get timestamp

  #first time thru
  if file_counter == 0:
    first = timestamp
    last = timestamp

  if timestamp < first:
    first = timestamp

  if timestamp > last:
    last = timestamp

  file_counter = file_counter + 1
  with open(file) as f:
    contents = f.read()
    #print contents
    for line in contents.split('\n'):
      #print line
      if 'listingscnt' in line: #this is the line with listing
        listing_count = listing_count + 1
        if not hasNumbers(line):
          no_number_count = no_number_count + 1
          #print file
          #print "   " + line
          no_number_files.append(file)
        else: #grab timestamp and listing number for graph
          the_time = int(file.split('.')[1])
          # next line may break, specific to DOM on 12/1/2015
          listings_num = int(line.split('"listingscnt"  >')[1].split(' ')[0].replace(',',''))
          #print listings_num
          #if listings_num < 50000: print listings_num
          if listings_num == 0:
            files_with_zero_listings.append(file)
          a = [the_time,listings_num]
          #print a
          graph_data.append(a)

print "found " + str(file_counter) + " files in " + the_dir
print "with " + str(listing_count) + " that have 'listingscnt' in DOM" 
print "spanning " + str(last-first) + " seconds"

print str(no_number_count) + " have no number in listings line"
for f in no_number_files:
  print "  " + f

print str(files_with_zero_listings) + " listings of '0'"
for f in files_with_zero_listings:
  print "  " + f

#print "here's the data for graphing -"
print "Found " + str(len(graph_data)) + " lines to graph"

df = pd.DataFrame(graph_data,columns=['unix time','listings'])

print "Min"
print df.min()

print "Max"
print df.max()

print "Mean"
print df.mean()

df.plot(kind='scatter',x='unix time',y='listings',title=graph_title)
plt.show()
