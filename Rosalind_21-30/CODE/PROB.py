import math

def calculate_log_probability(dna_string, gc_content):
    log_prob = 0.0

    prob_G = gc_content / 2
    prob_C = gc_content / 2
    prob_A = (1 - gc_content) / 2
    prob_T = (1 - gc_content) / 2

    for nucleotide in dna_string:
        if nucleotide == 'A':
            log_prob += math.log10(prob_A)
        elif nucleotide == 'C':
            log_prob += math.log10(prob_C)
        elif nucleotide == 'G':
            log_prob += math.log10(prob_G)
        elif nucleotide == 'T':
            log_prob += math.log10(prob_T)
    
    return log_prob

with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_21-30/DATA/rosalind_prob.txt', 'r') as f:
    lines = f.readlines()

    dna_string = lines[0].strip()

    gc_contents = list(map(float, lines[1].strip().split()))

results = []
for gc in gc_contents:
    log_prob = calculate_log_probability(dna_string, gc)
    results.append(log_prob)

print(' '.join(f'{x:.3f}' for x in results))