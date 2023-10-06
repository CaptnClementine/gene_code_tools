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


def is_in_gc_bounds(bounds: tuple, dna: str) -> bool:
    """
    Check if the GC content of a DNA sequence falls within the specified bounds.

    Args:
        bounds (tuple): A tuple specifying the lower and upper bounds for GC content.
        dna (str): The input DNA sequence.

    Returns:
        bool: True if the GC content is within the bounds, False otherwise.
    """
    gc_content = count_gc_content(dna)
    upper_bound = max(bounds[0], bounds[1])
    lower_bound = min(bounds[0], bounds[1])
    if upper_bound < 0 or lower_bound < 0:
        raise ValueError("Invalid gc_bounds. Each value must be greater than zero.")
    if upper_bound == lower_bound:
        upper_bound += 1
    return lower_bound <= gc_content < upper_bound

