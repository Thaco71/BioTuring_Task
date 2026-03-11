def longest_increasing_subsequence(perm):
    n = len(perm)
    tails = []
    prev = [-1] * n
    pos = []
    
    for i, x in enumerate(perm):
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if perm[tails[mid]] < x:
                left = mid + 1
            else:
                right = mid
        if left == len(tails):
            tails.append(i)
        else:
            tails[left] = i
        if left > 0:
            prev[i] = tails[left - 1]
    lis = []
    if tails:
        k = tails[-1]
        while k != -1:
            lis.append(perm[k])
            k = prev[k]
        lis.reverse()
    
    return lis

def longest_decreasing_subsequence(perm):
    neg_perm = [-x for x in perm]
    neg_lis = longest_increasing_subsequence(neg_perm)
    return [-x for x in neg_lis]

def read_input(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split()
        n = int(data[0])
        perm = list(map(int, data[1:1+n]))
    return n, perm

n, perm = read_input('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_lgis.txt')

lis = longest_increasing_subsequence(perm)

lds = longest_decreasing_subsequence(perm)

print(' '.join(map(str, lis)))
print(' '.join(map(str, lds)))