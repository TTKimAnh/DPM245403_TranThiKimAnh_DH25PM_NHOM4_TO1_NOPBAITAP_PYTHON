month = int(input("Nhập tháng (1-12): "))

if month < 1 or month > 12:
    print("Tháng không hợp lệ!")
else:
    if month <= 3:
        print("Tháng", month, "thuộc Quý 1")
    elif month <= 6:
        print("Tháng", month, "thuộc Quý 2")
    elif month <= 9:
        print("Tháng", month, "thuộc Quý 3")
    else:
        print("Tháng", month, "thuộc Quý 4")