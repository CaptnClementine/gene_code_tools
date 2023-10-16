def convert_multiline_fasta_to_oneline(input_fasta, output_fasta = 'output_auto.fasta'):
    """
    Convert a multiline FASTA file into a one-line FASTA format and save it to a new file.
    
    Args:
        input_fasta (str): The path to the input FASTA file.
        output_fasta (str, optional): The path to the output FASTA file. If not provided, the output
        file name will be generated based on the input file name with '.fasta' extension.
    
    Returns:
        None
    
    Reads the input FASTA file, which can contain sequences split across multiple lines, and saves it
    to a new FASTA file where each sequence is on a single line. The output file will be created
    with the name provided in the output_fasta argument or generated based on the input file name.
    
    The function retains the header lines starting with '>' and removes any line breaks within the
    sequence.
    """
    with open(input_fasta) as fasta_file:
        output_list = []
        s = ''
        for line in fasta_file:
            if '>' in line:
                output_list.append(s[:-1])
                s = ''
                output_list.append(line[:-1])
            else:
                s += line[:-1]
        output_list.append(s[:-1])

    with open(output_fasta,'w') as fasta_file:
        f.write("\n".join(output_list[1:]))
