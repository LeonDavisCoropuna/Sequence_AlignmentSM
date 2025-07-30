import sys
import subprocess
import os
import re
from Bio import AlignIO
from Bio.Align.Applications import ClustalOmegaCommandline

def run_alignment(input_file, output_file="aligned_sequences.fasta"):
    print("[INFO] Ejecutando alineamiento múltiple...")
    clustalomega_cline = ClustalOmegaCommandline(infile=input_file, outfile=output_file, verbose=True, auto=True, force=True)
    clustalomega_cline()
    print(f"[INFO] MSA generado en: {output_file}")
    return output_file

def build_tree(msa_output, tree_file="tree.nwk"):
    print("[INFO] Generando árbol filogenético...")
    subprocess.run(["FastTree", "-out", tree_file, msa_output], check=True)
    print(f"[INFO] Árbol Newick generado en: {tree_file}")
    return tree_file

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python create.py <archivo.fasta>")
        sys.exit(1)

    input_fasta = sys.argv[1]

    # Paso 1: Alineamiento Múltiple
    msa_output = run_alignment(input_fasta)

    # Paso 2: Generar árbol Newick
    newick_tree = build_tree(msa_output)

  