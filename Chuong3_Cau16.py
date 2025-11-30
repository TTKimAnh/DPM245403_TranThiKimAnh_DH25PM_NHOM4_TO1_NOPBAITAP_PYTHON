dem_sao = 0 
for a in range(20, 100, 5):
    print('*', end='')
    dem_sao += 1 # Đếm số lần lặp
print() # Lệnh xuống dòng
print(f"Tổng số dấu '*' được in ra là: {dem_sao}")