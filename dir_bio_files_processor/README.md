# 🔬 Gene and Sequence Data Processing Tool

This tool provides various functions for working with genetic data, including selecting specific genes from GenBank files, converting FASTA files to one-line format, shifting positions in FASTA alignments, and parsing BLAST output files.
### Brief functions overview
| Function                                     | Description                                    | Usage Example                                            |
| -------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------- |
| `select_genes_from_gbk_to_fasta`             | Select specific genes from GenBank files and save as FASTA. | `select_genes_from_gbk_to_fasta(input_gbk, genes, n_before, n_after, output_fasta)` |
| `convert_multiline_fasta_to_oneline`        | Convert multiline FASTA to one-line format.    | `convert_multiline_fasta_to_oneline(input_fasta, output_fasta)` |
| `change_fasta_start_pos`                     | Shift start position in FASTA alignments.       | `change_fasta_start_pos(input_fasta, shift, output_fasta)` |
| `parse_blast_output`                         | Parse BLAST output and extract sequence identifiers. | `parse_blast_output(input_file, output_file)` |

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Select Genes from GenBank](#select-genes-from-genbank)
  - [Convert Multiline FASTA to Oneline](#convert-multiline-fasta-to-oneline)
  - [Change FASTA Start Position](#change-fasta-start-position)
  - [Parse BLAST Output](#parse-blast-output)
- [Examples](#examples)
- [Common Errors](#common-errors)
- [Contributing](#contributing)
- [License](#license)

## Description

This tool is designed to work with genetic data in GenBank and FASTA file formats. It provides a set of functions to select specific genes from GenBank files, convert FASTA files to a one-line format, shift positions in FASTA alignments, and parse BLAST output files. These functions are particularly useful for various bioinformatics and genetic analysis tasks.

## Features

- Select specific genes from GenBank files.
- Convert multiline FASTA files to one-line FASTA format.
- Shift positions in FASTA alignments.
- Parse BLAST output files to extract sequence identifiers.

## Getting Started

Follow the instructions to install and use the tool.

### Prerequisites

- Python (>=3.0)

### Installation

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required packages:

    ```bash
    pip install package1 package2
    ```

## Usage

Learn how to use each function provided by the tool. If you need sample files for these functions, please check the 'example_files' directory in the main repository :blush:

### :arrow_forward: Select Genes from GenBank

```python
from gene_tool import select_genes_from_gbk_to_fasta

# Example usage
select_genes_from_gbk_to_fasta(
    input_gbk="input.gbk",
    genes=["gene1", "gene2"],
    n_before=5,
    n_after=5,
    output_fasta="output.fasta"
)
```

### :arrow_forward: Convert Multiline FASTA to Oneline

```python
from gene_tool import convert_multiline_fasta_to_oneline

# Example usage
convert_multiline_fasta_to_oneline(
    input_fasta="input.fasta",
    output_fasta="output.fasta"
)
```

### :arrow_forward: Change FASTA Start Position

```python
from gene_tool import change_fasta_start_pos

# Example usage
change_fasta_start_pos(
    input_fasta="input.fasta",
    shift=10,
    output_fasta="output.fasta"
)
```

### :arrow_forward: Parse BLAST Output

```python
from gene_tool import parse_blast_output

# Example usage
parse_blast_output(
    input_file="blast_output.txt",
    output_file="output.fasta"
)
```

## Common Errors

:white_check_mark: Please ensure that you have provided the correct file path with all the necessary directories. If you are uncertain about the path, you can use os.path.join(dir_name1, dir_name2, file_name) for assistance

- If the input file path provided is incorrect or the file does not exist, the functions will raise a `FileNotFoundError`.
- When specifying gene names in `select_genes_from_gbk_to_fasta`, ensure the gene names match the ones in the GenBank file, or the function won't find any genes.
- Make sure to provide a valid input FASTA file path for `convert_multiline_fasta_to_oneline`. If the file is not found, a `FileNotFoundError` will be raised.
- Ensure that the `shift` parameter in `change_fasta_start_pos` is within the valid range for the length of the sequence.

❗ Be careful if you have not specified an output file. Some functions use the same default output file names as their default arguments.

For more detailed information on each function and usage, see below.


If you have any questions, suggestions, or encounter any issues while using the amino-analyzer tool, feel free to reach out [CaptnClementine](https://github.com/YourGitHubUsername) 💛
