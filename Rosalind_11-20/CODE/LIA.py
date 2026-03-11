import math

def combination(n, k):
    """Tính tổ hợp C(n, k)"""
    return math.comb(n, k)

def probability_at_least_N(k, N):

    total = 2 ** k  # Tổng số cá thể ở thế hệ thứ k
    p = 1/4  # Xác suất một cá thể có kiểu gen Aa Bb

    if N > total:
        return 0.0
    
    probability = 0.0
    for i in range(N, total + 1):
        # C(total, i) * p^i * (1-p)^(total-i)
        prob_i = combination(total, i) * (p ** i) * ((1 - p) ** (total - i))
        probability += prob_i
    
    return probability

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_lia.txt', 'r') as file:
    k, N = map(int, file.read().strip().split())

result = probability_at_least_N(k, N)

print(round(result, 3))