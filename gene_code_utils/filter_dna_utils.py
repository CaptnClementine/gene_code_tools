def is_dna(seq: str) -> bool:
    """
    Check if the input sequence consists only of DNA characters.

    Args:
        seq (str): The input DNA sequence.

    Returns:
        bool: True if the sequence contains only DNA characters, False otherwise.
    """
    unique_chars = set(seq)
    nucleotides = set('ATGCatgc')
    return unique_chars <= nucleotides
