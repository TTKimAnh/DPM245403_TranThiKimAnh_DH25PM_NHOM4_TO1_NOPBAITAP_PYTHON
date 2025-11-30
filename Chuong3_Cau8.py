a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
pt = input("Nhập phép toán (+, -, *, /): ")

if pt == '+':
    result = a + b
elif pt == '-':
    result = a - b
elif pt == '*':
    result = a * b
elif pt == '/':
    if b == 0:
        result = "Lỗi: không thể chia cho 0!"
    else:
        result = a / b
else:
    result = "Không có phép toán này!"

print("Kết quả =", result)