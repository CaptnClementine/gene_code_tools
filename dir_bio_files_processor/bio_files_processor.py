from collections import deque


def select_genes_from_gbk_to_fasta(input_gbk: str, genes: list, n_before: int, n_after: int, output_fasta: str = 'output_auto.fasta') -> None:
    """
    Select specific genes from a GenBank (GBK) file, extract their genetic information, and save it as a FASTA format file.

    Args:
        input_gbk (str): The path to the input GenBank file. Please write your path with directory etc. You can use os.path.join(dir_name, file_name) 
        genes (list of str): A list of gene names to extract from the GenBank file.
        n_before (int): The number of sequences to include before the selected gene.
        n_after (int): The number of sequences to include after the selected gene.
        output_fasta (str, optional): The name of the output FASTA file. If not provided, it will be generated based on the gene name.

    Returns:
        None

    This function reads the input GenBank file, extracts CDS sequences, and selects specific genes. The selected sequences, along with surrounding context sequences, are saved as FASTA format files. Output files are named based on the gene name.

    The number of sequences before and after the selected gene is specified by n_before and n_after.

    """
    with open(input_gbk) as gbk_file:
        output_list = []
        read_line = []
        translation = ''
        translation_flag = 0
        for line in gbk_file:
            if 'CDS ' in line:
                read_line.append(translation)
                output_list.append(read_line)
                read_line = []
                translation = ''
                translation_flag = 0
            elif 'gene=' in line:
                read_line.append(line.strip())
            elif 'translation=' in line:
                if '"\n' in line:
                    translation += line.strip()
                else:
                    translation_flag = 1
                    translation += line.strip()
            elif '"' not in line and translation_flag == 1:
                translation += line.strip()
            elif '"' in line and translation_flag == 1:
                translation += line.strip()
                translation_flag = 0
        read_line.append(translation)
        output_list.append(read_line)    
    
    for gene in genes:
        output_translation = deque(["" for i in range(n_before + n_after)])
        find_flag, counter = 0, -1
        for cds in output_list[1:]:
            if 'gene=' in cds[0] and gene in cds[0]:
                find_flag = 1
            else:
                try:
                    output_translation.append(cds[1].split('="')[1][:-1])
                except:
                    output_translation.append(cds[0].split('="')[1][:-1])
                output_translation.popleft()
            if find_flag == 1:
                counter += 1
            if counter == n_after:
                break

        with open(f'{gene}_{output_fasta}','w') as gbk_file:
            gbk_file.write("\n".join(output_translation))


def convert_multiline_fasta_to_oneline(input_fasta: str, output_fasta: str = None) -> None:
    """
    Convert a multiline FASTA file into a one-line FASTA format and save it to a new file.
    
    Args:
        input_fasta (str): The path to the input FASTA file. Please write your path with directory etc. You can use os.path.join(dir_name, file_name) 
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
        read_line = ''
        for line in fasta_file:
            if '>' in line:
                output_list.append(read_line[:-1])
                read_line = ''
                output_list.append(line[:-1])
            else:
                read_line += line[:-1]
        output_list.append(read_line[:-1])

    with open(output_fasta,'w') as fasta_file:
        fasta_file.write("\n".join(output_list[1:]))
        
    
def change_fasta_start_pos(input_fasta: str, shift: int, output_fasta: str = 'output_auto.fasta') -> None:
    """
    Shift the start position of a FASTA sequence and save it to a new file. You can use it only for one one-line FASTA-alignment 

    Args:
        input_fasta (str): The path to the input FASTA file. Please write your path with directory etc. You can use os.path.join(dir_name, file_name) 
        shift (int): The number of positions to shift the sequence.
        output_fasta (str, optional): The name of the output FASTA file. If not provided, it will be generated based on the input file name.

    Returns:
        None
    """
    with open(input_fasta) as fasta_file:
        data = fasta_file.readlines()
        data[1] = data[1][shift:] + data[1][:shift]
    with open(output_fasta,'w') as fasta_file:
        fasta_file.write("".join(data))
