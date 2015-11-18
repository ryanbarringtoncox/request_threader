#!/usr/bin/python
import urllib2, time, Queue, threading

num_threads = 5 
lines_per_file = 5
url = 'http://www.ebay.com/sch/i.html?_odkw=aeroplane&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR12.TRC2.A0.H0.TRS0&_nkw=aeroplane&_sacat=0' 

def request(url):
  '''request url and return DOM on success.  else do nothing.'''
  try:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page
  except:
    print "excepting request..."
    pass

def parse_it(the_page,element_string):
  '''parse page for element with element_string - can only appear once!'''
  for line in the_page.split('\n'): #loop through lines of DOM
    if element_string in line:
      d = {}
      d['time']=time.time()
      d['result'] = line.split('>')[1].split(' ')[0].replace(',', '')
      return d

def write_lines(i):
  fn = 'out_file'+str(i)
  f = open(fn, 'w')
  print "opening file " + fn
  counter = 0
  while counter < lines_per_file:
    try:
      the_page = request(url)
      d = parse_it(the_page,'listingscnt')
      f.write(str(d['time']) + ':' + d['result']+'\n')
      counter = counter + 1
    except:
      print "excepting write_lines..."
      pass  

if __name__ == '__main__':
  threads = []
  for i in range(1,num_threads+1):
    #t = threading.Thread(target=write_lines, args = (i))
    t = threading.Thread(target=write_lines, args=(i,))
    #t.daemon = True
    threads.append(t) # do i need this?
    t.start()
