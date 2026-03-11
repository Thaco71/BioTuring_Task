def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    result = ''
    for base in dna:
        result = complement[base] + result
    return result

def is_reverse_palindrome(dna):
    return dna == reverse_complement(dna)

def find_reverse_palindromes(dna_sequence):
    results = []
    n = len(dna_sequence)
    
    for length in range(4, 13):
        for i in range(n - length + 1):
            substring = dna_sequence[i:i+length]
            if is_reverse_palindrome(substring):
                results.append((i + 1, length))
    
    return results

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_revp.txt', 'r') as f:
    lines = f.readlines()
    dna_sequence = ''
    for line in lines:
        if not line.startswith('>'):
            dna_sequence += line.strip()

palindromes = find_reverse_palindromes(dna_sequence)

for position, length in palindromes:
    print(position, length)