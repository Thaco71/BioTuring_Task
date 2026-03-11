with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_iprb.txt', 'r') as file:
    k, m, n = map(int, file.read().split())

total = k + m + n

p_aa_aa = (n / total) * ((n - 1) / (total - 1)) * 1.0
p_aa_Aa = (n / total) * (m / (total - 1)) * 0.5 + (m / total) * (n / (total -1)) * 0.5
p_Aa_Aa = (m / total) * ((m - 1) / (total -1)) * 0.25

p_recessive = p_aa_aa + p_aa_Aa + p_Aa_Aa
p_dominant = 1- p_recessive

print(f"{p_dominant:.5f}")