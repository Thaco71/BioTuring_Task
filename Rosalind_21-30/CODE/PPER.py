def partial_permutations(n, k):
    result = 1
    for i in range(n, n - k, -1):
        result = (result * i) % 1000000
    return result

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_pper.txt', 'r') as f:
    n, k = map(int, f.read().strip().split())

result = partial_permutations(n, k)

print(result)