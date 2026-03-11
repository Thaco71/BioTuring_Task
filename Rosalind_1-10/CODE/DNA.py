with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/rosalind_dna.txt', 'r') as file:
    dna_str = file.read().strip()

count_A = dna_str.count('A')
count_C = dna_str.count('C')
count_G = dna_str.count('G')
count_T = dna_str.count('T')

print(count_A, count_C, count_G, count_T)