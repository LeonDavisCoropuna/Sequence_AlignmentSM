from Bio import AlignIO

# Leer el archivo en formato Stockholm
alignment = AlignIO.read("PF00069.alignment.seed", "stockholm")

# Guardar el alineamiento en formato FASTA
AlignIO.write(alignment, "alignment.fasta", "fasta")

print("✅ Alineamiento exportado a 'alignment.fasta'")
