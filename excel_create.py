from xlwt import Workbook
##creating excel sheet to store data 
wb=Workbook()
user_sheet=wb.add_sheet('user_sheet')
user_sheet.write(0,0,'Usr_id')
user_sheet.write(0,1,'User_screen_name')
user_sheet.write(0,2,'#_Following')
user_sheet.write(0,3,'#_Follower')
user_sheet.write(0,4,'#_favourites_count')
user_sheet.write(0,5,'#_tweets')
##user_sheet.write(0,6,'#_retweet_count')
user_sheet.write(0,6,'created_on')
user_sheet.write(0,7,'location')
user_sheet.write(0,8,'description')
user_sheet.write(0,9,'verified_or_not')
user_sheet.write(0,10,'protected')
