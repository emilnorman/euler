y = 1900
m = 0 # January
# weekdays : 0 - 6 (sunday)
wd = 0 # Start om monday
sundays = 0

# 0 jan 31
# 1 feb 28/29
# 2 mar 31
# 3 apr 30 
# 4 may 31
# 5 jun 30
# 6 jul 31
# 7 aug 31
# 8 sep 30 
# 9 okt 31
# 10 nov 30 
# 11 dec 31

while y < 2001:
    if (y > 1900 and wd == 6):
        sundays += 1

        # 31 days
    if m == 0 or m == 2 or m == 4 or m == 6 or m ==7 or m == 9 or m ==11:
        wd = (31 + wd) % 7

    # 28/29 days
    elif m == 1:
        febDays = 0
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    febDays = 29
                else:
                    febDays = 28
            else:
                febDays = 29
        else: 
            febDays = 28

        wd = (febDays + wd) % 7

    # 30 days
    else:
        wd = (30 + wd) % 7

    # Increase month/year
    if m == 11:
        y += 1
        m = 0
    else:
        m += 1

print(sundays)
