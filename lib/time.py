def converting_time(hour, minute,period):
    #setting the conditions for valid hour, minute, and period parameters. 
    if (hour >= 1 and hour <= 12) and (minute >= 0 and minute <=59):
        if period == "pm" and hour != 12:
            hour += 12
        if period == "am" and hour == 12:
            hour = 0
        #using the zfill method to ensure that the hour and minute have two values. 
        converted_hour = str(hour).zfill(2)
        converted_minute = str(minute).zfill(2)
        #concatenating the new hour and minute to return a string representing 24-hour clock.
        return converted_hour + converted_minute
    else:
        return "invalid input"
    
#example
print(converting_time(6, 7, "pm"))