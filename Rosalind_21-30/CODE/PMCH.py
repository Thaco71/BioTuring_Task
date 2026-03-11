from math import factorial

def count_perfect_matchings(rna):
    count_A = rna.count('A')
    count_U = rna.count('U')
    count_C = rna.count('C')
    count_G = rna.count('G')

    if count_A != count_U or count_C != count_G:
        return 0
    
    perfect_matchings = factorial(count_A) * factorial(count_C)
    
    return perfect_matchings

def read_fasta(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        rna_sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return rna_sequence

rna_string = read_fasta('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_pmch.txt')

result = count_perfect_matchings(rna_string)

print(result)