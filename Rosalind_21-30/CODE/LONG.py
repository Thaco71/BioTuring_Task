def read_fasta(filename):
    sequences = []
    current_seq = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_seq:
                    sequences.append(''.join(current_seq))
                    current_seq = []
            else:
                current_seq.append(line)
        
        if current_seq:
            sequences.append(''.join(current_seq))
    
    return sequences

def overlap_length(s1, s2, min_length=1):
    max_overlap = min(len(s1), len(s2))
    
    # Tìm overlap dài nhất
    for i in range(max_overlap, min_length - 1, -1):
        if s1[-i:] == s2[:i]:
            return i
    return 0

def find_shortest_superstring(sequences):
    seqs = sequences.copy()
    
    while len(seqs) > 1:
        max_overlap = -1
        best_i, best_j = -1, -1
        best_merged = ""

        for i in range(len(seqs)):
            for j in range(len(seqs)):
                if i == j:
                    continue
                
                overlap = overlap_length(seqs[i], seqs[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                    best_i, best_j = i, j
                    best_merged = seqs[i] + seqs[j][overlap:]

        if best_i != -1 and best_j != -1:
            seq1 = seqs.pop(max(best_i, best_j))
            seq2 = seqs.pop(min(best_i, best_j))
            seqs.append(best_merged)
    
    return seqs[0]

sequences = read_fasta('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_long.txt')

result = find_shortest_superstring(sequences)

print(result)