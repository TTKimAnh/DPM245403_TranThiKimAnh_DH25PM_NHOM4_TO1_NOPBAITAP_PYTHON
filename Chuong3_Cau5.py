cases = [
    ("(a)", 3, 5, 7),
    ("(b)", 3, 7, 5),
    ("(c)", 5, 3, 7),
    ("(d)", 5, 7, 3),
    ("(e)", 7, 3, 5),
    ("(f)", 7, 5, 3)
]

for label, i, j, k in cases:
    # Lưu lại giá trị gốc để xử lý riêng từng case
    ii, jj, kk = i, j, k
    
    if ii < jj:
        if jj < kk:
            ii = jj
        else:
            jj = kk
    else:
        if jj > kk:
            jj = ii
        else:
            ii = kk

    print(label, "→ i =", ii, ", j =", jj, ", k =", kk)