with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_subs.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    s = lines[0]
    t = lines[1]

locations = []
len_s = len(s)
len_t = len(t)

for i in range(len_s - len_t + 1):
    if s[i:i+len_t] == t:
        locations.append(i + 1)

print(' '.join(map(str, locations)))