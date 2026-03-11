from itertools import permutations

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_perm.txt', 'r') as f:
    n = int(f.readline().strip())

numbers = list(range(1, n + 1))

perms = list(permutations(numbers))

print(len(perms))

for perm in perms:
    print(' '.join(map(str, perm)))