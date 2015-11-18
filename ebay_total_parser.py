#!/usr/bin/python

#fn = 'out_file_total_1447870175'
fn = 'out_file_total_1447872306'

bad_line_count = 0
zero_count_count = 0 #how many times it says zero results
good_lines = []
times = []
counts = []

with open(fn) as f:
  content = f.readlines()

counter = 0
for line in content:

  counter = counter + 1

  #broken lines
  if 'listing' in line:
    bad_line_count = bad_line_count + 1

  else:
    d = {} 
    pairs = line.replace('\n','').split(':')
    #print pairs
    d['time'] = float(pairs[0]) 
    d['count'] = int(pairs[1])
    good_lines.append(d) #dictionaries of corresonding time/count
    times.append(float(pairs[0])) #times array
    counts.append(int(pairs[1])) #counts array
    if d['count'] == 0:
      zero_count_count = zero_count_count + 1
     
max_time = max(times)
max_count = max(counts) 
min_time = min(times) 
min_count = min(counts) 


print str(counter) + ' total lines'
print str(len(good_lines)) + ' good lines'
print str(bad_line_count) + " bad lines (contain string 'listing' instead of actual number)"
print "files span " + str(max_time - min_time) + " seconds "
print "  " + str((max_time - min_time)/60) + " minutes "
print "max count is " + str(max(counts))
print "min count is " + str(min(counts))
print "count difference is " + str(max_count - min_count)
print "zero count is " + str(zero_count_count)
