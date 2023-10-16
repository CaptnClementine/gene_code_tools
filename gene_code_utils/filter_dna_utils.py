from typing import Dict, Tuple


def read_fastq_file(input_path: str) -> Dict[str, Tuple[str, str, str]]:
    """
    Read a FASTQ file and convert it into a dictionary.

    Args:
        input_path (str): Path to the input FASTQ file.

    Returns:
        fastq_dict (dict): A dictionary containing FASTQ sequences.
            Key: Sequence name (string).
            Value: Tuple of three strings (sequence, comment, quality).
    """
    fastq_dict = {}
    current_name = ''
    current_seq = ''
    current_comment = ''
    current_quality = ''
    line_counter = 1

    with open(input_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line_counter == 1:
                current_name = line[1:]
                line_counter += 1
            elif line_counter == 2:
                current_seq = line
                line_counter += 1
            elif line_counter == 3:
                current_comment = line
                line_counter += 1
            elif line_counter == 4:
                current_quality = line
                line_counter += 1

            if line_counter == 5:
                fastq_dict[current_name] = (current_seq, current_comment, current_quality)
                line_counter = 1

    return fastq_dict


def write_filtered_fastq(filtered_seqs: Dict[str, Tuple[str, str, str]], output_filename: str):
    """
    Write a FASTQ file

    Args:
        filtered_seqs (dict): dict of FASTQ to write them in output
        output_filename (str): Path to the output FASTQ file. By default, it is the same as the input name.
    """
    with open(f'{output_filename}', 'w') as file:
        for name, (seq, comment, quality) in filtered_seqs.items():
            file.write(f'@{name}_{seq}_{comment}_{quality}\n')


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
    return lower_bound <= gc_content <= upper_bound


def is_in_length_bounds(bounds: tuple, dna: str) -> bool:
    """
    Check if the length of a DNA sequence falls within the specified bounds.

    Args:
        bounds (tuple): A tuple specifying the lower and upper bounds for sequence length.
        dna (str): The input DNA sequence.

    Returns:
        bool: True if the sequence length is within the bounds, False otherwise.
    """
    dna_length = len(dna)
    lower_bound = min(bounds[0], bounds[1])
    upper_bound = max(bounds[0], bounds[1])
    if upper_bound < 0 or lower_bound < 0:
        raise ValueError("Invalid length_bounds. Each value must be greater than zero.")
    if upper_bound == lower_bound:
        upper_bound += 1
    return lower_bound <= dna_length <= upper_bound


def check_quality(quality_threshold: int, quality: str) -> bool:
    """
    Check if the average quality score of a sequence exceeds a threshold.

    Args:
        quality_threshold (int): The quality threshold for filtering sequences.
        quality (str): The quality string (in Phred+33 format).

    Returns:
        bool: True if the average quality score is above the threshold, False otherwise.
    """
    if quality_threshold < 0 or quality_threshold > 42:
        raise ValueError("Invalid quality_threshold. Must be an integer in the range [0, 42]")
    score = 0
    for char in quality:
        score += ord(char) - 33
        if ord(char) < 33 or ord(char) > 126:
            return False
    avg_quality = score / len(quality) 
    return quality_threshold <= avg_quality
