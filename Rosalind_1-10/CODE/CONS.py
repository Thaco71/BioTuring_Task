def read_fasta(file_content):
    sequences = []
    current_seq = ""
    
    for line in file_content.strip().split('\n'):
        if line.startswith('>'):
            if current_seq:
                sequences.append(current_seq)
                current_seq = ""
        else:
            current_seq += line.strip()
    
    if current_seq:
        sequences.append(current_seq)
    
    return sequences

def build_profile(sequences):
    n = len(sequences[0])
    profile = {
        'A': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
        'T': [0] * n
    }
    
    for seq in sequences:
        for i, nucleotide in enumerate(seq):
            profile[nucleotide][i] += 1
    
    return profile

def get_consensus(profile, n):
    consensus = []
    nucleotides = ['A', 'C', 'G', 'T']
    
    for i in range(n):
        max_count = -1
        max_nuc = ''
        for nuc in nucleotides:
            if profile[nuc][i] > max_count:
                max_count = profile[nuc][i]
                max_nuc = nuc
        consensus.append(max_nuc)
    
    return ''.join(consensus)

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_cons.txt', 'r') as file:
    data = file.read()

sequences = read_fasta(data)

n = len(sequences[0])
profile = build_profile(sequences)

consensus = get_consensus(profile, n)

print(consensus)
print(f"A: {' '.join(map(str, profile['A']))}")
print(f"C: {' '.join(map(str, profile['C']))}")
print(f"G: {' '.join(map(str, profile['G']))}")
print(f"T: {' '.join(map(str, profile['T']))}")