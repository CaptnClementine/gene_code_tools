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


def count_gc_content(dna: str) -> float:
    """
    Calculate the GC content percentage of a DNA sequence.

    Args:
        dna (str): The input DNA sequence.

    Returns:
        float: The GC content percentage.
    """
    dna = dna.upper()
    gc = dna.count('G') + dna.count('C')
    at = dna.count('A') + dna.count('T')
    gc_content = gc / (at + gc) * 100
    return gc_content
