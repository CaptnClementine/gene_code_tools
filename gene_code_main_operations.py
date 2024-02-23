import os
from typing import Tuple, Union

import numpy as np
from Bio import SeqIO
from Bio import SeqUtils


class InvalidInput(ValueError):
    """
    Exception raised for invalid input values.

    Inherits from ValueError.

    Attributes:
        message (str): Explanation of the error.
    """
    pass


def filter_dna(input_path: str, output_filename: str = '', gc_bounds: Union[Tuple[int, int], int] = (0, 100),
               length_bounds: Union[Tuple[int, int], int] = (0, 2 ** 32), quality_threshold: int = 0) -> None:
    """
    Filter and process a dictionary of FASTQ sequences based on specified criteria.

    Args:
        input_path (str): Path to the input FASTQ file. Please write your path with directory etc.
                          You can use os.path.join(dir_name, file_name)
        output_filename (str): Name of the output FASTQ file. By default, it is the same as the input name.
        gc_bounds (tuple or int): GC content filtering bounds.
            If a tuple, it represents the lower and upper bounds (inclusive) for GC content as percentages.
            If an int, it represents the upper bound for GC content as a percentage.
        length_bounds (tuple or int, optional): Length filtering bounds.
            If a tuple, it represents the lower and upper bounds (inclusive) for sequence length.
            If an int, it represents the upper bound for sequence length.
            Default is (0, 2**32).
        quality_threshold (int, optional): Quality threshold for filtering sequences based on average quality.
            Sequences with an average quality below this threshold will be discarded.
            Default is 0 (phred33 scale).

    Returns:
        filtered_seqs (dict): A file containing filtered FASTQ sequences.
            Key: Sequence name (string).
            Value: Tuple of two strings (sequence, comment, quality).

    Example:
        filtered_seqs = filtr_dna(seqs, gc_bounds=(20, 80), length_bounds=50, quality_threshold=30)
        - here gc_bounds interval will be [20, 80] and length_bounds will be [0, 50].
          quality_threshold will be 30 <= sequence score

    """

    good_reads = []
    records = SeqIO.parse(input_path, "fastq")
    if isinstance(gc_bounds, int):
        gc_bounds = (0, gc_bounds)
    if isinstance(length_bounds, int):
        length_bounds = (0, length_bounds)
    if not isinstance(gc_bounds, tuple) or not isinstance(length_bounds, tuple):
        raise InvalidInput()
    for record in records:
        if (np.mean(record.letter_annotations["phred_quality"]) >= quality_threshold) and \
                is_in_gc_bounds(gc_bounds, SeqUtils.gc_fraction(record) * 100) and \
                is_in_length_bounds(length_bounds, len(record.seq)):
            good_reads.append(record)

    if output_filename == '':
        output_filename = os.path.basename(input_path)
    if not os.path.exists('fastq_filtrator_results'):
        os.mkdir('fastq_filtrator_results')
    output_filename = os.path.join('fastq_filtrator_results', output_filename)
    SeqIO.write(good_reads, handle=output_filename, format="fastq")

    return None


def is_in_gc_bounds(bounds: tuple, gc_content: float) -> bool:
    """
    Check if the GC content of a DNA sequence falls within the specified bounds.

    Args:
        bounds (tuple): A tuple specifying the lower and upper bounds for GC content.
        gc_content (float): GC content of input DNA.

    Returns:
        bool: True if the GC content is within the bounds, False otherwise.
    """

    upper_bound = max(bounds[0], bounds[1])
    lower_bound = min(bounds[0], bounds[1])
    if upper_bound <= 0 or lower_bound < 0:
        raise InvalidInput("Invalid gc_bounds. Each value must be greater than zero.")
    if upper_bound == lower_bound:
        upper_bound += 1
    return lower_bound <= gc_content <= upper_bound


def is_in_length_bounds(bounds: tuple, dna_length: int) -> bool:
    """
    Check if the length of a DNA sequence falls within the specified bounds.

    Args:
        bounds (tuple): A tuple specifying the lower and upper bounds for sequence length.
        dna_length (int): The length of input DNA sequence.

    Returns:
        bool: True if the sequence length is within the bounds, False otherwise.
    """

    lower_bound = min(bounds[0], bounds[1])
    upper_bound = max(bounds[0], bounds[1])
    if upper_bound < 0 or lower_bound < 0:
        raise ValueError("Invalid length_bounds. Each value must be greater than zero.")
    if upper_bound == lower_bound:
        upper_bound += 1
    return lower_bound <= dna_length <= upper_bound
