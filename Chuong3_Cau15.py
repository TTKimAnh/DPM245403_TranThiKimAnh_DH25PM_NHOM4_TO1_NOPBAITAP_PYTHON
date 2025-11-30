def in_ket_qua_range(ten_cau, ham_range):
    """Hàm in ra kết quả của range() dưới dạng danh sách (list)."""
    print(f"({ten_cau}) {ham_range}: {list(ham_range)}")

print("--- Kết quả các lệnh range() ---")

# (a) range(5)
in_ket_qua_range('a', range(5))

# (b) range(5, 10)
in_ket_qua_range('b', range(5, 10))

# (c) range(5, 20, 3)
in_ket_qua_range('c', range(5, 20, 3))

# (d) range(20, 5, -1)
in_ket_qua_range('d', range(20, 5, -1))

# (e) range(20, 5, -3)
in_ket_qua_range('e', range(20, 5, -3))

# (f) range(10, 5) -> Step dương mặc định, Start > Stop -> Chuỗi rỗng
in_ket_qua_range('f', range(10, 5))

# (g) range(0) -> Chuỗi rỗng
in_ket_qua_range('g', range(0))

# (h) range(10, 101, 10)
in_ket_qua_range('h', range(10, 101, 10))

# (i) range(10, -1, -1)
in_ket_qua_range('i', range(10, -1, -1))

# (j) range(-3, 4)
in_ket_qua_range('j', range(-3, 4))

# (k) range(0, 10, 1)
in_ket_qua_range('k', range(0, 10, 1))