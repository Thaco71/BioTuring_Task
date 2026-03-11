from itertools import product

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_lexf.txt', 'r') as f:
    lines = f.readlines()

    alphabet = lines[0].strip().split()

    n = int(lines[1].strip())

kmers = [''.join(p) for p in product(alphabet, repeat=n)]

for kmer in kmers:
    print(kmer)