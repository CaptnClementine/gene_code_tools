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
