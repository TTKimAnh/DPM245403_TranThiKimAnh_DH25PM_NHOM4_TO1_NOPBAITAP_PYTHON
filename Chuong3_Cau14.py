# Mã nguồn Python cho Bài toán đếm dấu '*' (Câu 14)

a = 0
dem_sao = 0 # Biến đếm số lượng dấu '*'

# Vòng lặp ngoài
while a < 100:
    b = 0
    
    # Vòng lặp trong
    while b < 40:
        
        # Điều kiện in: Tổng (a + b) là số chẵn
        if (a + b) % 2 == 0:
            # print('*', end='') # Dòng này sẽ in dấu '*' thực tế
            dem_sao += 1         # Chỉ đếm số lần thỏa mãn điều kiện
        
        b += 1
    
    # print() # Dòng này sẽ in ký tự xuống dòng (theo mã gốc)
    a += 1

print(f"Tổng số dấu '*' được in ra là: {dem_sao}") 
# Kết quả sẽ là 2000