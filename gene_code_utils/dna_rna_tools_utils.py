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
