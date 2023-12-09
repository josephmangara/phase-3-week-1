def converting_time(hour, minute,period):
    if (hour >= 1 and hour <= 12) and (minute >= 0 and minute <=59):
        if period == "pm" and hour != 12:
            hour += 12
        if period == "am" and hour == 12:
            hour = 0
        converted_hour = str(hour).zfill(2)
        converted_minute = str(minute).zfill(2)

        return converted_hour + converted_minute
    else:
        return "invalid input"
print(converting_time(6, 7, "pm"))