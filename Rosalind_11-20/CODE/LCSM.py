def read_fasta(file_content):
    sequences = []
    current_seq = []
    
    for line in file_content.strip().split('\n'):
        if line.startswith('>'):
            if current_seq:
                sequences.append(''.join(current_seq))
                current_seq = []
        else:
            current_seq.append(line.strip())
    
    if current_seq:
        sequences.append(''.join(current_seq))
    
    return sequences

def longest_common_substring(sequences):
    if not sequences:
        return ""

    shortest = min(sequences, key=len)
    shortest_len = len(shortest)
    
    result = ""

    for length in range(shortest_len, 0, -1):
        for start in range(shortest_len - length + 1):
            substring = shortest[start:start + length]
            
            found_in_all = True
            for seq in sequences:
                if substring not in seq:
                    found_in_all = False
                    break
            
            if found_in_all:
                return substring
    
    return result

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_lcsm.txt', 'r') as file:
    data = file.read()

sequences = read_fasta(data)

result = longest_common_substring(sequences)

print(result)