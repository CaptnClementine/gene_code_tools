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
