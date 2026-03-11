def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    result = ''
    for base in reversed(dna):
        result += complement[base]
    return result

def dna_to_mrna(dna):
    return dna.replace('T', 'U')

def translate_until_stop(mrna, start_pos):
    codon_table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }
    
    protein = ''
    for i in range(start_pos, len(mrna) - 2, 3):
        codon = mrna[i:i+3]
        if codon in codon_table:
            aa = codon_table[codon]
            if aa == '_':
                return protein
            protein += aa
        else:
            return ''
    return ''

def find_orfs(dna_sequence):
    proteins = set()

    for sequence in [dna_sequence, reverse_complement(dna_sequence)]:
        mrna = dna_to_mrna(sequence)

        for frame in range(3):
            for i in range(frame, len(mrna) - 2, 3):
                if mrna[i:i+3] == 'AUG':
                    protein = translate_until_stop(mrna, i)
                    if protein:
                        proteins.add(protein)
    
    return proteins

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_orf.txt', 'r') as f:
    lines = f.readlines()
    dna_sequence = ''
    for line in lines:
        if not line.startswith('>'):
            dna_sequence += line.strip()

proteins = find_orfs(dna_sequence)
for protein in proteins:
    print(protein)