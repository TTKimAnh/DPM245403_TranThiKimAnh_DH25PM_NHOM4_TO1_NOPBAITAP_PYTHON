def doc_so(n):
    chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    if n < 10:
        return chu_so[n]

    if n < 20:
        if n == 10:
            return "mười"
        elif n == 15:
            return "mười lăm"
        else:
            return "mười " + chu_so[n % 10]

    # số >= 20
    chuc = n // 10
    don_vi = n % 10

    # đọc hàng chục
    result = chu_so[chuc] + " mươi"

    # hàng đơn vị
    if don_vi == 0:
        return result
    elif don_vi == 1:
        return result + " mốt"
    elif don_vi == 4:
        return result + " tư"
    elif don_vi == 5:
        return result + " lăm"
    else:
        return result + " " + chu_so[don_vi]

# ----- TEST -----
n = int(input("Nhập n (0-99): "))
print(doc_so(n))