#!/usr/bin/python
import urllib2, time, Queue, threading, os

num_threads = 50 
lines_per_file = 100 
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

def parse_it(the_page,element_string):
  '''parse page for element with element_string - can only appear once!'''
  for line in the_page.split('\n'): #loop through lines of DOM
    if element_string in line:
      d = {}
      d['time']=time.time()
      d['result'] = line.split('>')[1].split(' ')[0].replace(',', '')
      try:
        int(d['result'])
      except:
        print "Something went wrong parsing this line:"
        print line
      return d

def write_lines(i,out_files_dir):
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
      print "  excepting write_lines..."

if __name__ == '__main__':

  start_time = time.time()

  #make dir for outfiles
  out_files_dir = 'out_files_' + str(start_time).split('.')[0]
  os.mkdir(out_files_dir)
  os.chdir(os.getcwd()+'/'+out_files_dir)

  for i in range(1,num_threads+1):
    #t = threading.Thread(target=write_lines, args = (i))
    t = threading.Thread(target=write_lines, args=(i,out_files_dir))
    t.start()
