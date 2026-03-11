def find_subsequence_indices(s, t):
    indices = []
    pos = 0

    for char in t:
        found_pos = s.find(char, pos)
        if found_pos != -1:
            indices.append(found_pos + 1)  
            pos = found_pos + 1  
        else:
            return []
    
    return indices

def read_fasta(filename):
    sequences = []
    with open(filename, 'r') as f:
        current_seq = []
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

sequences = read_fasta('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_sseq.txt')
s = sequences[0]
t = sequences[1]

result = find_subsequence_indices(s, t)

print(' '.join(map(str, result)))