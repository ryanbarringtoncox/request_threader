#!/usr/bin/python
import urllib2, time

result_list = []

# url to request
url = 'http://www.ebay.com/sch/i.html?_odkw=aeroplane&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR12.TRC2.A0.H0.TRS0&_nkw=aeroplane&_sacat=0' 

def request(url):
  '''request url and return DOM on success.  else do nothing.'''
  try:
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page
  except:
    pass

def parse_it(the_page,element_string):
  '''parse page for element with element_string - can only appear once!'''
  for line in the_page.split('\n'): #loop through lines of DOM
    if element_string in line:
      d = {}
      d['time']=time.time()
      d['result'] = line.split('>')[1].split(' ')[0].replace(',', '')
      return d

#for x in range(0, 100):
while len(result_list) < 10:
  try:
    the_page = request(url)
    d = parse_it(the_page,'listingscnt')
    print d
    result_list.append(d) 
  except:
    pass  

for x in result_list:
  print str(x['time']) + ':' + x['result']
#print "done and result_list length is"
#print len(result_list)
#print result_list
