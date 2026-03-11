with open('/home/thanhcong/Downloads/BioTuring_Task/Rosalind_11-20/DATA/rosalind_iev.txt', 'r') as file:
    couples = list(map(int, file.read().strip().split()))

probabilities = [
    1.0,    # AA-AA: 100% con trội
    1.0,    # AA-Aa: 100% con trội
    1.0,    # AA-aa: 100% con trội
    0.75,   # Aa-Aa: 75% con trội
    0.5,    # Aa-aa: 50% con trội
    0.0     # aa-aa: 0% con trội
]

expected_offspring = 0
for i in range(6):
    expected_offspring += couples[i] * probabilities[i] * 2

print(expected_offspring)