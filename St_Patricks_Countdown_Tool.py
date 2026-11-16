import datetime

today = datetime.date.today()
current_time = datetime.datetime.now()

current_year = datetime.date.today().year

saint_patricks_time = datetime.datetime(current_year, 3, 17,0,0,0)

if current_time > saint_patricks_time:
    saint_patricks_time = datetime.datetime(current_year+1, 3, 17,0,0,0)


time_till_st_patricks = saint_patricks_time - current_time

total_seconds_till_st_patricks = time_till_st_patricks.total_seconds()

days_till_st_patricks = int(total_seconds_till_st_patricks // 86400)

hours_till_st_patricks = int(total_seconds_till_st_patricks // 3600)
hours_till_st_patricks = hours_till_st_patricks % 24

minutes_till_st_patricks = int(total_seconds_till_st_patricks // 60)
minutes_till_st_patricks = minutes_till_st_patricks % 60

seconds_till_st_patricks = int(total_seconds_till_st_patricks % 60)

if days_till_st_patricks == 0:
    print("Happy St. Patrick's Day!")
else:
    print(str(days_till_st_patricks) + " days " + str(hours_till_st_patricks) + 
        " hours " + str(minutes_till_st_patricks) + " minutes " + str(seconds_till_st_patricks) + " seconds until St. Patrick's Day!")