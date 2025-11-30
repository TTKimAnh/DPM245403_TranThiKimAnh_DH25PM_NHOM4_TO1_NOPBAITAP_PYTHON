def nam_nhuan(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def ngay_toida(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 29 if nam_nhuan(year) else 28

# ------ MAIN ------
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

max_day = ngay_toida(month, year)

if day < max_day:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1

print("Ngày kế tiếp là: {}/{}/{}".format(day, month, year))