#!/usr/bin/python
import os, glob, decimal

#the_dir = 'aeroplaneout_files_1448472525'
#the_dir = 'aeroplaneout_files_1448472822'
#the_dir = 'gunout_files_1448473078'
#the_dir = 'gunout_files_1448473351'
the_dir = 'staplerout_files_1448477783'
os.chdir(the_dir)
first = 0
last = 0
no_number_files = []

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

  if timestamp < first:
    first = timestamp

  if timestamp > first:
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

print "found " + str(file_counter) + " files in " + the_dir
print "with " + str(listing_count) + " that have 'listingscnt' in DOM" 
print "spanning " + str(last-first) + " seconds"
print str(no_number_count) + " have no number in listings line"
for f in no_number_files:
  print "  " + f
#print "No-number count is " + str(float(no_number_count/file_counter)*100) + '%'
