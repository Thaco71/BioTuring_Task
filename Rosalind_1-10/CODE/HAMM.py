with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_1-10/DATA/rosalind_hamm.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    s = lines[0].strip()
    t = lines[1].strip()

if len(s) != len(t):
    print("Two chains are the same length")
else:
    differ = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            differ += 1
    print(differ)
