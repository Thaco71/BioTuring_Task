with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_revc.txt', 'r') as file:
    DNA = file.read().strip()

complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

rcDNA = ''.join(complement[base] for base in reversed(DNA))

print(rcDNA)
