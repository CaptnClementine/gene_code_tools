![image](https://github.com/CaptnClementine/gene_code_tools/assets/131146976/68f2999b-5b6e-4668-9865-fae0d4e0b778)
# gene_code_tools 


`gene_code_tools` is a collection of Python functions for working with DNA, RNA, and protein sequences. It provides utility functions to check and manipulate sequences based on various criteria.

In the main file **gene_code_main_operations** you can find 3 most important functions**:**

- [ ]  filter_dna
    - Filter a dictionary of FASTQ sequences based on various criteria.
- [ ]  run_amino_analyzer
    - Perform basic protein analytics.
- [ ]  run_dna_rna_tools
    - Conduct fundamental analytics on RNA and DNA sequences.

| Function | Description | Returns | Arguments |
| --- | --- | --- | --- |
| filter_dna | Filter FASTQ sequences based on criteria like GC content, length, and quality. | Filtered sequences (dict) | seqs (dict), gc_bounds (tuple or int), length_bounds (tuple or int, optional), quality_threshold (int, optional) |
| run_amino_analyzer | Perform various protein sequence operations. | Result of specified operation(s) | seq (str), args (Union[str, Tuple[str, ...]]) |
| run_dna_rna_tools | Perform DNA and RNA sequence operations. | Result of specified operation(s) | seq (str), args (Union[str, Tuple[str, ...]]) |

Here's more detailed information and examples for each function:

## function filter_dna

### Features

- [ ]  Check if a sequence consists only of DNA characters.
- [ ]  Calculate the GC content percentage of a DNA sequence.
- [ ]  Check if a DNA sequence falls within specified GC content bounds.
- [ ]  Check if a DNA sequence falls within specified length bounds.
- [ ]  Check if the average quality score of a sequence exceeds a threshold.

### Usage

Here's an example of how to use the functions provided by `gene_code_tools`:

```python
from gene_code_utils.filter_dna_utils import filter_dna

# Create a dictionary of FASTQ sequences
seqs = {
    'sequence1': ('AGCTAGCTAGCT', '!@#$!@#$!@#$'),
    'sequence2': ('TATATATATATA', 'abcdefghi'),
    # Add more sequences as needed
}

# Specify your filtering criteria
gc_bounds = (20, 80)  # GC content bounds
length_bounds = (50, 100)  # Sequence length bounds
quality_threshold = 30  # Quality threshold

# Filter the sequences based on the criteria
filtered_seqs = filter_dna(seqs, gc_bounds, length_bounds, quality_threshold)

# Use the filtered sequences as needed
print(filtered_seqs)
```

### Common Errors

When using Gene Code Tools, you might encounter common errors such as invalid input values or incorrect sequence formats. Here are some typical errors and how to handle them:

1. **Invalid gc_bounds or length_bounds**: Ensure that the bounds provided are valid tuples with two non-negative values or a single non-negative integer. For example, `gc_bounds=(20, 80)` is valid, and `gc_bounds=44.4` sets an upper GC content limit of 44.4%. All bounds inclusive
2. **Invalid quality_threshold**: The `quality_threshold` should be an integer between 0 and 42 (inclusive).
3. **Invalid sequence characters**: When working with DNA sequences, make sure that the input sequences contain only valid DNA characters (A, T, G, C, a, t, g, c).

### Specified Variables and Parameters

Gene Code Tools provides the following specified variables and parameters:

- `seqs` (dict): A dictionary containing FASTQ sequences.
- `gc_bounds` (tuple or int): GC content filtering bounds.
- `length_bounds` (tuple or int, optional): Length filtering bounds.
- `quality_threshold` (int, optional): Quality threshold for filtering sequences.

### Examples

Here are some examples of how to use Gene Code Tools:

```python
# Example 1: Filtering DNA sequences
filtered_seqs = filter_dna(seqs, gc_bounds=(20, 80), length_bounds=50, quality_threshold=30)

# Example 2: Using a single upper bound for GC content
filtered_seqs = filter_dna(seqs, gc_bounds=44.4, length_bounds=(10, 100))

# Example 3: Using a single upper bound for sequence length
filtered_seqs = filter_dna(seqs, gc_bounds=(20, 80), length_bounds=1000)

# Example 4: Filtering without specifying bounds
filtered_seqs = filter_dna(seqs)
```

## function run_amino_analyzer

### **Features**

- [ ]  Transcribe DNA sequences into RNA.
- [ ]  Reverse transcribe RNA sequences into DNA.
- [ ]  Check for the presence of a start codon in RNA sequences.
- [ ]  Reverse sequences.
- [ ]  Find the complement of DNA or RNA sequences.
- [ ]  Find the reverse complement of DNA or RNA sequences.
- [ ]  Check if a sequence is a palindrome.
- [ ]  Determine the type of RNA or DNA sequences (DNA, RNA, or mixed).

### **Usage**

### **Main Function: `run_dna_rna_tools`**

The **`run_dna_rna_tools`** function is the main entry point for performing various DNA and RNA sequence operations. It takes a sequence and an optional set of additional arguments to specify the operation to perform.

```python
pythonCopy code
from gene_code_utils import run_dna_rna_tools

# Example 1: Transcribe DNA to RNA
result = run_dna_rna_tools("ATGC", "transcribe")
print(result)  # Output: "AUGC"

# Example 2: Reverse RNA sequence
result = run_dna_rna_tools("AUGC", "reverse")
print(result)  # Output: "CGUA"

```

### Arguments

- **`seq (str)`**: The input DNA or RNA sequence.
- **`args (Union[str, Tuple[str, ...]])`**: Additional sequences or options. If the last argument is a string, it specifies the operation to perform.

### Supported Operations

- **`transcribe`**: Transcribe a DNA sequence into RNA.
- **`reverse_transcription`**: Reverse transcribe an RNA sequence into DNA.
- **`has_start_codon`**: Check if an RNA sequence has a start codon.
- **`reverse`**: Reverse a sequence.
- **`complement`**: Find the complement of a DNA or RNA sequence.
- **`reverse_complement`**: Find the reverse complement of a DNA or RNA sequence.
- **`is_palindrome`**: Check if a sequence is a palindrome.

### **Gene Code Utilities (`gene_code_utils.py`)**

The **`gene_code_utils.py`** module contains the core functions used by the main function. It includes the following functions:

- **`is_dna(seq: str) -> bool`**: Check if a sequence is DNA.
- **`is_rna(seq: str) -> bool`**: Check if a sequence is RNA.
- **`transcribe(seq: str) -> str`**: Transcribe a DNA sequence into RNA.
- **`reverse(seq: str) -> str`**: Reverse a sequence.
- **`complement(seq: str) -> str`**: Find the complement of a DNA or RNA sequence.
- **`reverse_complement(seq: str) -> str`**: Find the reverse complement of a DNA or RNA sequence.
- **`reverse_transcription(seq: str) -> str`**: Perform reverse transcription on an RNA sequence.
- **`is_palindrome(seq: str) -> bool`**: Check if a sequence is a palindrome.
- **`has_start_codon(seq: str) -> Union[bool, str]`**: Check if an RNA sequence has a start codon.
- **`type_rna_or_dna(seqs: List[str]) -> str`**: Determine the type of RNA or DNA from a list of sequences.

You can use these functions directly if needed.

### **Common Errors**

- **Invalid Procedure**: If you specify an invalid operation, you will receive a "Invalid procedure. Check your sequences and try again." error.
- **Sequence Type Mismatch**: If you try to perform an operation on the wrong sequence type (e.g., transcribing a DNA sequence), you will receive a type-specific error message.
- **Unsupported Sequences**: If your sequences contain characters other than A, T, G, C, U, a, t, g, c, u, you will receive a "Input sequence must be DNA or RNA." error.

### **Specified Variables and Parameters**

- **`seq (str)`**: The input DNA or RNA sequence.
- **`args (Union[str, Tuple[str, ...]])`**: Additional sequences or options.
- **`procedure (str)`**: The specified operation to perform.
- **`seqs (List[str])`**: List of sequences to operate on.
- **`dna_or_rna (str)`**: Indicates whether the sequences are DNA, RNA, or mixed.
- **`new_RNA (List[str])`**: List to store the results of operations.

### **Example**

```python
pythonCopy code
from gene_code_utils import run_dna_rna_tools

# Transcribe DNA to RNA and find the reverse complement
result = run_dna_rna_tools("ATGC", "transcribe", "reverse_complement")
print(result)  # Output: "GCAT"

```

## function run_dna_rna_tools

**Features**

- [ ]  Transcribe DNA sequences into RNA.
- [ ]  Reverse transcribe RNA sequences into DNA.
- [ ]  Check for the presence of a start codon in RNA sequences.
- [ ]  Reverse sequences.
- [ ]  Find the complement of DNA or RNA sequences.
- [ ]  Find the reverse complement of DNA or RNA sequences.
- [ ]  Check if a sequence is a palindrome.
- [ ]  Determine the type of RNA or DNA sequences (DNA, RNA, or mixed).

## **Usage**

### **Main Function: `run_dna_rna_tools`**

The **`run_dna_rna_tools`** function is the main entry point for performing various DNA and RNA sequence operations. It takes a sequence and an optional set of additional arguments to specify the operation to perform.

```python
pythonCopy code
from dna_rna_tools_utils import run_dna_rna_tools

# Example 1: Transcribe DNA to RNA
result = run_dna_rna_tools("ATGC", "transcribe")
print(result)  # Output: "AUGC"

# Example 2: Reverse RNA sequence
result = run_dna_rna_tools("AUGC", "reverse")
print(result)  # Output: "CGUA"

```

### Arguments

- **`seq (str)`**: The input DNA or RNA sequence.
- **`args (Union[str, Tuple[str, ...]])`**: Additional sequences or options. If the last argument is a string, it specifies the operation to perform.

### Supported Operations

- **`transcribe`**: Transcribe a DNA sequence into RNA.
- **`reverse_transcription`**: Reverse transcribe an RNA sequence into DNA.
- **`has_start_codon`**: Check if an RNA sequence has a start codon.
- **`reverse`**: Reverse a sequence.
- **`complement`**: Find the complement of a DNA or RNA sequence.
- **`reverse_complement`**: Find the reverse complement of a DNA or RNA sequence.
- **`is_palindrome`**: Check if a sequence is a palindrome.

### **Gene Code Utilities (`dna_rna_tools_utils.py`)**

The **`dna_rna_tools_utils.py`** module contains the core functions used by the main function. It includes the following functions:

- **`is_dna(seq: str) -> bool`**: Check if a sequence is DNA.
- **`is_rna(seq: str) -> bool`**: Check if a sequence is RNA.
- **`transcribe(seq: str) -> str`**: Transcribe a DNA sequence into RNA.
- **`reverse(seq: str) -> str`**: Reverse a sequence.
- **`complement(seq: str) -> str`**: Find the complement of a DNA or RNA sequence.
- **`reverse_complement(seq: str) -> str`**: Find the reverse complement of a DNA or RNA sequence.
- **`reverse_transcription(seq: str) -> str`**: Perform reverse transcription on an RNA sequence.
- **`is_palindrome(seq: str) -> bool`**: Check if a sequence is a palindrome.
- **`has_start_codon(seq: str) -> Union[bool, str]`**: Check if an RNA sequence has a start codon.
- **`type_rna_or_dna(seqs: List[str]) -> str`**: Determine the type of RNA or DNA from a list of sequences.

You can use these functions directly if needed.

## **Common Errors**

- **Invalid Procedure**: If you specify an invalid operation, you will receive an "Invalid procedure. Check your sequences and try again." error.
- **Sequence Type Mismatch**: If you try to perform an operation on the wrong sequence type (e.g., transcribing a DNA sequence), you will receive a type-specific error message.
- **Unsupported Sequences**: If your sequences contain characters other than A, T, G, C, U, a, t, g, c, u, you will receive an "Input sequence must be DNA or RNA." error.

## **Specified Variables and Parameters**

- **`seq (str)`**: The input DNA or RNA sequence.
- **`args (Union[str, Tuple[str, ...]])`**: Additional sequences or options.
- **`procedure (str)`**: The specified operation to perform.
- **`seqs (List[str])`**: List of sequences to operate on.
- **`dna_or_rna (str)`**: Indicates whether the sequences are DNA, RNA, or mixed.
- **`new_seq (List[str])`**: List to store the results of operations.

## **Example**

```python
pythonCopy code
from dna_rna_tools_utils import run_dna_rna_tools

# Transcribe DNA to RNA and find the reverse complement
result = run_dna_rna_tools("ATGC", "transcribe", "reverse_complement")
print(result)  # Output: "GCAT"

```
