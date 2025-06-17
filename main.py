# Given DNA sequence
dna = "ATCGATCGAACATCGATCATCGATCGAAATCGATCGAACCGAACGATCGATCGAACATATCGATATCGATCGAACCGATCGAACATCGAACCATCGATCGAACGATCGAAC"

# Initialize a dictionary to store the frequency of each nucleotide
frequency = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

# Iterate over each nucleotide in the DNA sequence and update the frequency
for nucleotide in dna:
    if nucleotide in frequency:
        frequency[nucleotide] += 1
        
# Input validation for DNA sequence
valid_nucleotides = set("ATCG")
if not all(nucleotide in valid_nucleotides for nucleotide in dna):
    raise ValueError("Invalid DNA sequence. Provide sequence containing only A, T, C, and G.")

# Print the frequency of each nucleotide
for nucleotide, count in frequency.items():
    print(f"{nucleotide}: {count}")
    
    
    # Given DNA sequence
dna = "ATCGATCGAACATCGATCATCGATCGAAATCGATCGAACCGAACGATCGATCGAACATATCGATATCGATCGAACCGATCGAACATCGAACCATCGATCGAACGATCGAAC"

# Function to generate the reverse complement of the DNA sequence
def reverse_complement(sequence):
    # Dictionary mapping each nucleotide to its complement
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Generate the reverse complement
    return ''.join(complement[nucleotide] for nucleotide in reversed(sequence))

# Generate the reverse complement of the DNA sequence
reverse_comp = reverse_complement(dna)

# Output the reverse complement
print("Reverse complement of the DNA sequence:", reverse_comp)

# Given DNA sequence
dna = "ATCGATCGAACATCGATCATCGATCGAAATCGATCGAACCGAACGATCGATCGAACATATCGATATCGATCGAACCGATCGAACATCGAACCATCGATCGAACGATCGAAC"

# Function to find the starting indices of a subsequence in the DNA sequence
def find_subsequence(sequence, subsequence):
    start_indices = []
    sub_len = len(subsequence)
    for i in range(len(sequence) - sub_len + 1):
        if sequence[i:i+sub_len] == subsequence:
            start_indices.append(i)
    return start_indices

# Example usage:
# subsequence to search for
subseq = "CGA"
# Call the function with the DNA sequence and the subsequence
indices = find_subsequence(dna, subseq)

# Output the starting indices
print(f"The subsequence '{subseq}' was found at the following indices: {indices}")
