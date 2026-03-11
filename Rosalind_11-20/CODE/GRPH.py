def read_fasta(file_content):
    sequences = {}
    current_id = ""
    current_seq = []
    
    for line in file_content.strip().split('\n'):
        if line.startswith('>'):
            if current_id:
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:].strip()
            current_seq = []
        else:
            current_seq.append(line.strip())
    
    if current_id:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences

def build_overlap_graph(sequences, k=3):
    adjacency_list = []

    ids = list(sequences.keys())

    for i in range(len(ids)):
        for j in range(len(ids)):
            if i != j:
                s_id = ids[i]
                t_id = ids[j]
                s_seq = sequences[s_id]
                t_seq = sequences[t_id]
                
                if len(s_seq) >= k and len(t_seq) >= k:
                    if s_seq[-k:] == t_seq[:k]:
                        adjacency_list.append((s_id, t_id))
    
    return adjacency_list

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_grph.txt', 'r') as file:
    data = file.read()

sequences = read_fasta(data)

adjacency_list = build_overlap_graph(sequences, k=3)

for s, t in adjacency_list:
    print(f"{s} {t}")