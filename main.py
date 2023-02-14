def add_time(time,duration,day = ""):
    time = time.strip('"')
    day = day.strip('"')
    time = time.split()
    AMorPM = time[1]
    Atime = time[0]
    Atime = Atime.split(':')
    time_hrs = int(Atime[0])
    time_mins = int(Atime[1])
    if AMorPM == "PM":
        time_hrs = time_hrs + 12
    duration = duration.strip('"')
    duration = duration.split(':')
    duration_hrs = int(duration[0])
    duration_mins = int(duration[1])
    time_hrs_in_mins = time_hrs*60
    duration_hrs_in_mins = duration_hrs*60
    Total_time_mins = time_hrs_in_mins + duration_hrs_in_mins + time_mins + duration_mins
    Total_time_mins_in_hrs = int(Total_time_mins) // 60 
    Total_time_mins_in_mins = int(Total_time_mins) % 60
    Total_time_mins_in_crcthrs = int(Total_time_mins_in_hrs) % 24
    if Total_time_mins_in_crcthrs >= 12 :
        AM_PM = "PM"
        Total_time_mins_in_crcthrs = Total_time_mins_in_crcthrs - 12
    else:
        AM_PM = "AM"
    Cday = ""
    No_of_days = Total_time_mins_in_hrs // 24
    if Total_time_mins_in_hrs >= 24:
        No_of_days = Total_time_mins_in_hrs // 24
        if No_of_days == 1:
            Cday = "(next day)"
        elif No_of_days >1:
            Cday = "(" + str(No_of_days) + " days later)"
    Total_time_mins_in_hrs = str(Total_time_mins_in_hrs)
    Total_time_mins_in_mins = str(Total_time_mins_in_mins)
    Total_time_mins_in_crcthrs = str(Total_time_mins_in_crcthrs)
    days_in_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday",""]
    if day == "" and int(Total_time_mins_in_mins) > 10:
        if int(Total_time_mins_in_crcthrs) == 0:
            Total_time_mins_in_crcthrs = "12"
        Final_Output = Total_time_mins_in_crcthrs + ":" + Total_time_mins_in_mins + " " + AM_PM + " " + Cday
        print(Final_Output)  
    elif day == "" and int(Total_time_mins_in_mins) < 10:
        if int(Total_time_mins_in_crcthrs) == 0:
            Total_time_mins_in_crcthrs = "12"
        Final_Output = Total_time_mins_in_crcthrs + ":0" + Total_time_mins_in_mins + " " + AM_PM + " " + Cday
        print(Final_Output)
    elif day != "" and int(Total_time_mins_in_mins) > 10:
        n = days_in_week.index(day)
        n = (n + No_of_days) % 7
        day = days_in_week[n]
        if int(Total_time_mins_in_crcthrs) == 0:
            Total_time_mins_in_crcthrs = "12"
        Final_Output = Total_time_mins_in_crcthrs + ":" + Total_time_mins_in_mins + " " + AM_PM + ", " + day + " " + Cday
        print(Final_Output)  
    elif day != "" and int(Total_time_mins_in_mins) < 10:
        n = days_in_week.index(day)
        n = (n + No_of_days) % 7
        day = days_in_week[n]
        if int(Total_time_mins_in_crcthrs) == 0:
            Total_time_mins_in_crcthrs = "12"
        Final_Output = Total_time_mins_in_crcthrs + ":0" + Total_time_mins_in_mins + " " + AM_PM + ", " + day + " " + Cday
        print(Final_Output)   
add_time("12:37 AM","340:39","Monday")
