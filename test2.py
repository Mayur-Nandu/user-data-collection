import tweepy
from authh import *
from xlwt import Workbook
from userr_info import *


##user_str=str(userr)
##parsed = json.loads(user_str)
##print (json.dumps(parsed, indent=4, sort_keys=True))

def requesting_user_info(query,i):
        pg=1
        #assuming 800requests
        while pg!=40: 
            userr=api.search_users(q=query ,per_page=20,page=pg)
            for user in userr:
                user_info(user.id,i)
                i=i+1
            pg=pg+1
        return i

list_of_query=['abc','xyz','free','discount','likes']
next_row=1

for keyword in list_of_query:
    next_row=requesting_user_info(keyword ,next_row)
'''
i=1
pg=0
query='free'
for j in range(3):
     userr=api.search_users(q=query ,per_page=20,page=pg)
     for user in userr:
         user_info(user.id,i)
         i=i+1
     j=j+1
     pg=pg+1
'''
     
wb.save('user_db2.xls')
