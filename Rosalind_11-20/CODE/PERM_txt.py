from itertools import permutations

# Đọc dữ liệu từ file input
with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_perm.txt', 'r') as f:
    n = int(f.readline().strip())

# Tạo list các số từ 1 đến n
numbers = list(range(1, n + 1))

# Tạo tất cả các hoán vị
perms = list(permutations(numbers))

# Ghi kết quả ra file output
with open('output_PERM.txt', 'w') as f:
    # Ghi tổng số hoán vị
    f.write(str(len(perms)) + '\n')
    
    # Ghi từng hoán vị
    for perm in perms:
        f.write(' '.join(map(str, perm)) + '\n')

print(f"Đã ghi kết quả vào file output.txt với {len(perms)} hoán vị")