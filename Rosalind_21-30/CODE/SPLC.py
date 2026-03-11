def read_fasta(filename):
    sequences = {}
    current_id = ""
    current_seq = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)

        if current_id:
            sequences[current_id] = ''.join(current_seq)
    
    return sequences

def dna_to_rna(dna):
    return dna.replace('T', 'U')

def translate_rna_to_protein(rna):
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
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i+3]
        if codon in codon_table:
            aa = codon_table[codon]
            if aa == '_':  
                break
            protein += aa
        else:
            break
    return protein

sequences = read_fasta('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_splc.txt')

dna_strings = list(sequences.values())
dna_original = dna_strings[0]  
introns = dna_strings[1:]      

exons_dna = dna_original
for intron in introns:
    exons_dna = exons_dna.replace(intron, '')

exons_rna = dna_to_rna(exons_dna)

protein = translate_rna_to_protein(exons_rna)

print(protein)