from itertools import product, permutations

def generate_signed_permutations(n):
    signed_perms = []

    base_permutations = list(permutations(range(1, n + 1)))

    for perm in base_permutations:
        for sign in product([-1, 1], repeat=n):
            signed_perm = [perm[i] * sign[i] for i in range(n)]
            signed_perms.append(signed_perm)
    
    return signed_perms

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_sign.txt', 'r') as f:
    n = int(f.read().strip())

signed_perms = generate_signed_permutations(n)

print(len(signed_perms))

for perm in signed_perms:
    print(' '.join(map(str, perm)))