from bs4 import BeautifulSoup
from excel_create import *
from authh import *
from userr_info import *
from sorting_algo import *
import time 

## checking for rate limit status
'''
data = api.rate_limit_status()
print(data['resources']['statuses']['/statuses/home_timeline'])
print(data['resources']['users']['/users/lookup'])
'''


## Get the User object for twitter...
user = api.get_user('NanduMayur')
user_id=user.id
##user = api.get_user(user_id)
##print(user)
i=1
j=0
total_id_1=[]
while i<102:
    user_info(user_id,i)
    total_id=follower_following_id(user_id)
    total_id_1=total_id_1+total_id
    total_id_1=remove_duplicate(total_id_1)
    i=i+1
    user_id=total_id_1[j]
    j+1
    time.sleep(5)
    
##while true:
##    user_new=api.get_user(total_id[0])
##    user_info(user_new)

wb.save('user_db.xls')


