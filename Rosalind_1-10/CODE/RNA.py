with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_rna.txt', 'r') as file:
    t = file.read().strip()

u = t.replace('T', 'U')

print(u)