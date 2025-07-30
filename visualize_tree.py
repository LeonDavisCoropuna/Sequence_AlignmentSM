import argparse
from Bio import Phylo
import matplotlib.pyplot as plt

def visualize_tree(newick_file, output_image):
    tree = Phylo.read(newick_file, "newick")

    # Normalizar ramas pequeñas
    min_length = 0.001
    for clade in tree.find_clades():
        if clade.branch_length is not None and clade.branch_length < min_length:
            clade.branch_length = min_length

    fig = plt.figure(figsize=(12, 6), dpi=100)
    axes = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, axes=axes, do_show=False)
    axes.axis('off')
    plt.tight_layout()

    # Guardar imagen
    plt.savefig(output_image)
    print(f"Árbol guardado en {output_image}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualizador de árboles filogenéticos")
    parser.add_argument("tree_file", help="Archivo .nwk de entrada")
    parser.add_argument("--out", default="tree.png", help="Archivo de salida (por defecto: tree.png)")
    args = parser.parse_args()

    visualize_tree(args.tree_file, args.out)
