from typing import Tuple, Union, List
import os


def filter_dna(input_path: str, output_filename: str = '', gc_bounds: Union[Tuple[int, int], int] = (0, 100),
              length_bounds: Union[Tuple[int, int], int] = (0, 2**32), quality_threshold: int = 0) -> None:
    """
    Filter and process a dictionary of FASTQ sequences based on specified criteria.

    Args:
        input_path (str): Path to the input FASTQ file. Please write your path with directory etc. You can use os.path.join(dir_name, file_name) 
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
        filtered_seqs (dict): A dictionary containing filtered FASTQ sequences.
            Key: Sequence name (string).
            Value: Tuple of two strings (sequence, comment, quality).

    Example:
        filtered_seqs = filtr_dna(seqs, gc_bounds=(20, 80), length_bounds=50, quality_threshold=30)
        - here gc_bounds interval will be [20, 80] and length_bounds will be [0, 50].
          quality_threshold will be 30 <= sequence score

    """
    seqs = read_fastq_file(input_path)
    filtered_seqs = dict()
    for fastq_name, (seq, seq_comment, quality) in seqs.items():
        if is_dna(seq):
            if type(gc_bounds) == int:
                gc_bounds = (0, gc_bounds)
            if type(length_bounds) == int:
                length_bounds = (0, length_bounds)
            if is_in_gc_bounds(gc_bounds, seq) and is_in_length_bounds(length_bounds, seq) and check_quality(quality_threshold, quality):
                filtered_seqs[fastq_name] = (seq,seq_comment, quality)
    
    if output_filename == '':
        output_filename =  os.path.basename(input_path)
    if not os.path.exists('fastq_filtrator_results'):
        os.mkdir('fastq_filtrator_results')
    output_filename = os.path.join('fastq_filtrator_results', output_filename)
    write_filtered_fastq(filtered_seqs, output_filename)

    return None
