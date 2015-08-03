
from BeautifulSoup import BeautifulSoup
import pickle
#import MySQLdb as mdb
#con=mdb.connect('localhost','Jie','Jie315','Indeeddb')
#with con:
#    cur=con.cursor()
#   cur.execute("SELECT state,COUNT(*) FROM Indeedds WHERE date>'2015-06-30 00:00:00' AND date<'2015-08-01 00:00:00' GROUP BY state;")
#    rows=cur.fetchall()
#jobn={}
#for row in rows:
#    jobn[row[0]]=row[1]
#file = open('jobnJuly2015.txt', 'w')
#pickle.dump(jobn, file)
#file.close()

file = open('jobnJuly2015.txt')
jobn = pickle.load(file)
file.close()

nmax=max(jobn.values())
thresh=[pow(2,7),pow(2,6),pow(2,5),pow(2,4),0]
path_style = 'font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'

# load the svg map;
svg = open('states_with_names.svg', 'r').read()
soup = BeautifulSoup(svg,selfClosingTags=['defs','sodipodi:namedview','path','rect'])
paths = soup.findAll('path')
# Map colors http://colorbrewer2.org/
colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

for path in paths:
     if len(path['id'])==2:
        if path['id'] in jobn.keys():
            njob=jobn[path['id']]
            if njob > thresh[0]:
              color_class = 5
            elif njob > thresh[1]:
              color_class = 4
            elif njob > thresh[2]:
              color_class = 3
            elif njob > thresh[3]:
              color_class = 2
            elif njob > thresh[4]:
              color_class = 1
            else:
              color_class = 0
        else:
           jobn[path['id']]=0
           color_class=0
        color = colors[color_class]
        path['style'] = path_style+color
print soup

            
               
