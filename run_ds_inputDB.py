import json
from collections import Counter
f=open('/Users/Jie/Dropbox/Insight/output08022015_5.txt','r')
result=json.load(f)
f.close()

#nloop1=len(result)
#jk=[]
#for ii in range(nloop1):
#    sample=result[ii]
#    jk.append(sample['jobkey'])
#count=Counter(jk)
def toTimeStamp(date):
    toMonth={u'Jan':u'01',u'Feb':u'02',u'Mar':u'03',u'Apr':u'04',u'May':u'05',
           u'Jun':u'06',u'Jul':u'07',u'Aug':u'08',u'Sep':u'09',u'Oct':u'10',
           u'Nov':u'11',u'Dec':u'12'}
    day=date[5:7]
    month=toMonth[date[8:11]]
    year=date[12:16]
    time=date[17:25]
    timeStamp=year+u'-'+month+u'-'+day+u' '+time
    return timeStamp
    
import MySQLdb
con = MySQLdb.connect('localhost', 'Jie', 'Jie315', 'Indeeddb')
cur = con.cursor()
l=0
with con:
    #cur.execute("CREATE TABLE Indeedds(jobkey VARCHAR(20) NOT NULL PRIMARY KEY,"
    #"date TIMESTAMP, jobtitle VARCHAR(50),company VARCHAR(30), city VARCHAR(30),"
    #"state VARCHAR(2),country VARCHAR(15))")
    for ii in range(0,len(result)):
        sample=result[ii]
        try:
            cur.execute("INSERT INTO Indeedds(jobkey,date,jobtitle,company,city,state,country)"
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)",(sample['jobkey'],toTimeStamp(sample['date']),sample['jobtitle'],sample['company'],sample['city'],sample['state'],sample['country']))
        except MySQLdb.IntegrityError:
            l=l+1
        con.commit()
con.close()
