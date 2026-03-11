def mortal_fibonacci(n, m):
    rabbits = [0] * (m + 1)
    rabbits[1] = 1
    
    for month in range(2, n + 1):
        new_borns = sum(rabbits[2:])
        
        for age in range(m, 1, -1):
            rabbits[age] = rabbits[age - 1]
        
        rabbits[1] = new_borns
    
    return sum(rabbits)

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_fibd.txt', 'r') as file:
    n, m = map(int, file.read().strip().split())

result = mortal_fibonacci(n, m)
print(result)