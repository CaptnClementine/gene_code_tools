from typing import Tuple, Union, List
from gene_code_utils.filter_dna_utils import is_dna, is_in_gc_bounds, is_in_length_bounds, check_quality, write_filtered_fastq, read_fastq_file
from gene_code_utils.amino_analyzer_utils import  is_aa, aa_weight, count_hydroaffinity, peptide_cutter, one_to_three_letter_code, sulphur_containing_aa_counter
from gene_code_utils.dna_rna_tools_utils import type_rna_or_dna, transcribe, reverse_transcription, has_start_codon, reverse, complement, reverse_complement, is_palindrome
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


def run_amino_analyzer(sequence: str, procedure: str, *, weight_type: str = 'average', enzyme: str = 'trypsin'):
    """
    This is the main function to run the amino-analyzer.py tool.
    
    Args:
        sequence (str): The input protein sequence in one-letter code.
        procedure (str): amino-analyzer.py tool has 5 functions at all:
            1. aa_weight - Calculate the amino acids weight in a protein sequence. Return float weight
                        weight_type = 'average': default argument for 'aa_weight' function. weight_type = 'monoisotopic' can be used as a second option.
            2. count_hydroaffinity - Count the quantity of hydrophobic and hydrophilic amino acids in a protein sequence. Return list in order: hydrophobic, hydrophilic
            3. peptide_cutter - This function identifies cleavage sites in a given peptide sequence using a specified enzyme. Return list of cleavage sites
                        enzyme = 'trypsin': default argument for 'peptide_cutter' function. enzyme = 'chymotrypsin' can be used as a second option.
            4. one_to_three_letter_code - This function converts a protein sequence from one-letter amino acid code to three-letter code. Return string of amino acids in three-letter code
            5. sulphur_containing_aa_counter - This function counts sulphur-containing amino acids in a protein sequence. Return quantaty of sulphur-containing amino acids

    Returns:
        The result of the specified procedure.

    Raises:
        ValueError: If the procedure is not recognized or if the input sequence contains non-amino acid characters.

    Note:
        - Supported amino acid characters: V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h, w, f, y, r, k, s, t, m, a, g, p, c.
        - Make sure to provide a valid procedure name and sequence for analysis.
    """

    procedures = ['aa_weight', 'count_hydroaffinity', 'peptide_cutter', 'one_to_three_letter_code', 'sulphur_containing_aa_counter']
    if procedure not in procedures:
        raise ValueError(f"Incorrect procedure. Acceptable procedures: {', '.join(procedures)}")

    if not is_aa(sequence):
        raise ValueError("Incorrect sequence. Only amino acids are allowed (V, I, L, E, Q, D, N, H, W, F, Y, R, K, S, T, M, A, G, P, C, v, i, l, e, q, d, n, h, w, f, y, r, k, s, t, m, a, g, p, c).")

    if procedure == 'aa_weight':
        result = aa_weight(sequence, weight_type)
    elif procedure == 'count_hydroaffinity':
        result = count_hydroaffinity(sequence)
    elif procedure == 'peptide_cutter':
        result = peptide_cutter(sequence, enzyme)
    elif procedure == 'one_to_three_letter_code':
        result = one_to_three_letter_code(sequence)
    elif procedure == 'sulphur_containing_aa_counter':
        result = sulphur_containing_aa_counter(sequence)
    return result


def run_dna_rna_tools(seq: str, *args: Union[str, Tuple[str, ...]]) -> Union[str, List[str]]:
    """
    Run various DNA and RNA sequence operations.

    Args:
        seq (str): The input DNA or RNA sequence.
        *args (Union[str, Tuple[str, ...]]): Additional sequences or options.
            If the last argument is a string, it specifies the operation to perform.
            If the last argument is 'transcribe', 'reverse_transcription', or 'has_start_codon', the input sequence(s) must be RNA.
            Otherwise, the input sequence(s) must be DNA.

    Returns:
        Union[str, List[str]]: The result of the specified operation(s).
            If a single operation is performed, the result is a string.
            If multiple operations are performed, the result is a list of strings.
    """
    procedure = args[len(args)-1]
    seqs = list((seq,)+args[:-1])
    dna_or_rna = type_rna_or_dna(seqs)
    new_seq = []

    operation_map = {
        'transcribe': transcribe,
        'reverse_transcription': reverse_transcription,
        'has_start_codon': has_start_codon,
        'reverse': reverse,
        'complement': complement,
        'reverse_complement': reverse_complement,
        'is_palindrome': is_palindrome,
    }

    if procedure not in operation_map:
        raise ValueError("Invalid procedure. Check your sequences and try again.")
    if (procedure in ('transcribe')) and (dna_or_rna == 'RNA'):
        raise ValueError("This procedure is only for DNA sequences. Check your sequences and try again.")
    elif (procedure in ('reverse_transcription', 'has_start_codon')) and (dna_or_rna == 'DNA'):
        raise ValueError("This procedure is only for RNA sequences. Check your sequences and try again.")

    print(f"Hi! Here is your {procedure} for all your {dna_or_rna} sequences")

    operation_func = operation_map[procedure]
    new_seq = [operation_func(i) for i in seqs]
    return new_seq[0] if len(new_seq) == 1 else new_seq
