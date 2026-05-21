branch_count = int(input("Nhập so lượng chi nhánh: "))
month_count = 3

revenue = {}

for month in range(1, month_count + 1):
    for branch in range(1, branch_count + 1):
        revenue[(branch, month)] = int(input(f"Nhập doanh thu Chi nhánh {branch}, tháng {month}: "))

for month in range(1, month_count + 1):
    for branch in range(1, branch_count + 1):
        print(f"Chi nhánh {branch}, tháng {month}: {revenue[(branch, month)]} triệu đồng")

# Bài 1 bị một lỗi sai locgic khi dùng vòng lặp lồng nhau doanh thu chi nhánh nằm trong tháng chính vì thế mà khi nhập bị lỗi sai không theo như mong muốn
