#!/usr/bin/python
# hits ebay with given search_word and writes html DOM locally
# prints files of the format [randint].[timestamp].html in folder [ebay_search_word]_files_[timestamp] in working dir
import urllib2, time, Queue, threading, os
from random import randint

num_threads = 50
hits_per_thread = 100
#search_word = 'aeroplane'
#search_word = 'gun'
search_word = 'stapler'
url = 'http://www.ebay.com/sch/i.html?_odkw='+search_word+'&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR12.TRC2.A0.H0.TRS0&_nkw='+search_word+'&_sacat=0' 

def request(url):
  '''request url and return DOM on success.  else do nothing.'''
  try:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page
  except:
    print "excepting request..."

def write_lines(out_files_dir,hits_per_thread):
  '''write DOM to local file.'''
  counter = 0
  while counter < hits_per_thread:
    try:
      #files named with random int preceding so they won't clobber one another
      fn = str(randint(0,1000000))+'.'+str(time.time())+'.html'
      f = open(fn, 'w')
      print "opening file " + fn
      the_page = request(url)
      f.write(the_page)
      counter = counter + 1
    except:
      print "  excepting write_lines, tryin again..."

if __name__ == '__main__':

  start_time = time.time() #starting timestamp for dir names

  #make timestamped dir for outfiles from this run, cd in...
  out_files_dir = search_word+'_out_files_' + str(start_time).split('.')[0]
  os.mkdir(out_files_dir)
  os.chdir(os.getcwd()+'/'+out_files_dir)

  #thread it
  for i in range(1,num_threads+1):
    t = threading.Thread(target=write_lines, args=(out_files_dir,hits_per_thread))
    t.start()
