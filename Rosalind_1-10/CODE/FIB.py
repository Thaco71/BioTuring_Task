with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_fib.txt', 'r') as file:
    n, k = map(int, file.read().split())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    F1, F2 = 1, 1
    for i in range(3, n + 1):
        F_current = F2 + k*F1
        F1, F2 = F2, F_current

print(F2)