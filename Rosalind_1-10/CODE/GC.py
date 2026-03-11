def calculate_gc_content(dna_string):
    if len(dna_string) == 0:
        return 0.0
    gc_count = dna_string.count('C') + dna_string.count('G')
    return (gc_count / len(dna_string)) * 100

def read_fasta(file_content):
    sequences = {}
    current_id = ""
    current_seq = []
    
    lines = file_content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if current_id and current_seq:
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:]
            current_seq = []
        else:
            if line:
                current_seq.append(line)
    
    if current_id and current_seq:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_gc.txt', 'r') as file:
    fasta_data = file.read()

sequences = read_fasta(fasta_data)

max_gc_id = None
max_gc_content = -1.0

for seq_id, dna_string in sequences.items():
    gc_content = calculate_gc_content(dna_string)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_id = seq_id

print(max_gc_id)
print(f"{max_gc_content:.6f}")