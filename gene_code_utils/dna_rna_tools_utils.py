DNA = set ('ATGCatgc')
RNA = set ('AUGCaugc')


def is_dna(seq: str) -> bool:
    """
    Check if a sequence is DNA.

    Args:
        seq (str): The input sequence to check.

    Returns:
        bool: True if the sequence is DNA, False otherwise.
    """
    unique_chars = set(seq)
    return unique_chars <= DNA


def is_rna(seq: str) -> bool:
    """
    Check if a sequence is RNA.

    Args:
        seq (str): The input sequence to check.

    Returns:
        bool: True if the sequence is RNA, False otherwise.
    """
    unique_chars = set(seq)
    return unique_chars <= RNA


def type_rna_or_dna(seqs: List[str]) -> str:
    """
    Determine the type of RNA or DNA from a list of sequences.

    Args:
        seqs (List[str]): List of sequences to determine their type.

    Returns:
        str: 'DNA' if all sequences are DNA, 'RNA' if all sequences are RNA,
            'MIXED' if there are both DNA and RNA sequences, or raises a ValueError for unsupported sequences.
    """
    counter_dna = 0
    counter_rna = 0
    ambigiuos = 0
    for i in seqs:
      if is_dna(i) and is_rna(i):
          ambigiuos = ambigiuos+1
      else:
        if is_dna(i):
            counter_dna=counter_dna+1
        elif is_rna(i):
            counter_rna=counter_rna+1
    if (counter_dna + ambigiuos) == len(seqs):
        print('You have ', ambigiuos, ' ambigious NA. I suppose they are DNA')
        return "DNA"
    elif (counter_rna + ambigiuos) == len(seqs):
        print('You have ', ambigiuos, ' ambigious NA. I suppose they are RNA')
        return "RNA"
    elif (counter_dna + counter_rna + ambigiuos)  == len(seqs):
        return "MIXED"
    else:
        raise ValueError("I can work only with RNA and DNA. \n Check your sequences and try one more time!")   


def reverse(seq: str) -> str:
    """
    Reverse a sequence.

    Args:
        seq (str): The input sequence.

    Returns:
        str: The reversed sequence.
    """
    return seq[::-1]


def complement(seq: str) -> str:
    """
    Find the complement of a DNA or RNA sequence.

    Args:
        seq (str): The input DNA or RNA sequence.

    Returns:
        str: The complemented sequence.
    """
    new_seq = []
    if is_dna(seq):
        complement_dict = {'A': 'T', 'a': 't', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c', 'T': 'A', 't': 'a'}
    elif is_rna(seq):
        complement_dict = {'A': 'U', 'a': 'u', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c', 'U': 'A', 'u': 'a'}
    else:
        raise ValueError("Input sequence must be DNA or RNA.")
    for i in seq:
        new_seq.append(complement_dict.get(i))
    return ''.join(new_seq)


def reverse_complement(seq: str) -> str:
    """
    Find the reverse complement of a DNA or RNA sequence.

    Args:
        seq (str): The input DNA or RNA sequence.

    Returns:
        str: The reverse complemented sequence.
    """
    return reverse(complement(seq))


def reverse_transcription(seq: str) -> str:
    """
    Perform reverse transcription on an RNA sequence.

    Args:
        seq (str): The input RNA sequence.

    Returns:
        str: The reverse transcribed DNA sequence.
    """
    c_dna = []
    u_to_t = {'U': 'T', 'u': 't'}
    for i in seq:
        if i in u_to_t:
            c_dna.append(u_to_t.get(i))
        else:
            c_dna.append(i)
    return ''.join(c_dna)


def has_start_codon(seq: str) -> Union[bool, str]:
    """
    Check if an RNA sequence has a start codon.

    Args:
        seq (str): The input RNA sequence.

    Returns:
        Union[bool, str]: True if a start codon is found, False if not found,
            '?' if the input is DNA and needs to be transcribed first.
    """
    if is_rna(seq):
        return "AUG" in seq.upper()
    if is_dna(seq):
        print("First, you should transcribe your DNA.")
        return '?'
    raise ValueError("Input sequence must be DNA or RNA.")


def is_palindrome(seq: str) -> bool:
    """
    Check if a sequence is a palindrome.

    Args:
        seq (str): The input sequence to check.

    Returns:
        bool: True if the sequence is a palindrome, False otherwise.
    """
    new_seq = reverse_complement(seq)
    return new_seq.upper() == seq.upper()
