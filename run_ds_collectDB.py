from indeed import *
import math

client=IndeedClient('8977558155731952') # my publisher ID
params={
    'q':"data+scientist",
    'userip':"129.59.122.21",
    'useragent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)",
    'limit':25,
    'start':0,
    'fromage':35,
    'sort':"date",
    'jt':"fulltime",
    'psf':"advsrch"
}


search_response=client.search(**params) # response if of type dict
results=dict(search_response)['results'] # results is of type list
nresults=dict(search_response)['totalResults']
nloop=int(math.ceil(nresults/25))

for ii in range(1,nloop+1):
    params['start']=ii*25
    search_response=client.search(**params) # response if of type dict
    resultstemp=dict(search_response)['results'] # results is of type list
    results=results+resultstemp
    # type(results)
    # type(results[1])


import simplejson
f = open('output08022015_5.txt', 'w')
simplejson.dump(results, f)
f.close()
