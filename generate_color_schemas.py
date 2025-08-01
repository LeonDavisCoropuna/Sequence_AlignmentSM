import numpy as np
from sklearn.manifold import MDS
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from Bio.Align import substitution_matrices
import json

# --- 1. Cargar BLOSUM62 y definir alfabeto ---
blosum62 = substitution_matrices.load("BLOSUM62")
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")  # 20 aminoácidos estándar

# --- 2. Convertir BLOSUM62 a matriz de distancias (como en el paper) ---
def blosum62_to_distance(blosum_matrix, alphabet):
    n = len(alphabet)
    D = np.zeros((n, n))
    for i, aa1 in enumerate(alphabet):
        for j, aa2 in enumerate(alphabet):
            if j <= i:
                D[i, j] = (blosum_matrix[aa1, aa1] - blosum_matrix[aa1, aa2] + 
                           blosum_matrix[aa2, aa2] - blosum_matrix[aa2, aa1]) / 2
    D = D / np.mean(D[D > 0])  # Escalar (promedio = 1)
    return D + D.T - np.diag(np.diag(D))  # Hacer simétrica

D = blosum62_to_distance(blosum62, amino_acids)

# --- 3. Mapear distancias a colores CIELAB (similar al paper) ---
def optimize_colors(distance_matrix, lightness_range=(60, 75), exclude_green=False):
    mds = MDS(n_components=3, dissimilarity="precomputed", random_state=42, n_init=1)
    colors_lab = mds.fit_transform(distance_matrix)
    
    # Normalizar a rangos CIELAB (parámetros del paper)
    L_min, L_max = lightness_range
    colors_lab[:, 0] = np.interp(colors_lab[:, 0], (colors_lab[:, 0].min(), colors_lab[:, 0].max()), (L_min, L_max))  # L*
    colors_lab[:, 1] = np.interp(colors_lab[:, 1], (colors_lab[:, 1].min(), colors_lab[:, 1].max()), (-50, 50))  # a*
    colors_lab[:, 2] = np.interp(colors_lab[:, 2], (colors_lab[:, 2].min(), colors_lab[:, 2].max()), (-50, 50))  # b*
    
    if exclude_green:
        colors_lab[:, 1] = np.clip(colors_lab[:, 1], 0, None)  # a* > 0 (excluir verde)
    
    return colors_lab

colors_lab = optimize_colors(D, lightness_range=(60, 75))

# --- 4. Convertir CIELAB a HEX ---
def lab_to_hex(L, a, b):
    lab = LabColor(L, a, b)
    rgb = convert_color(lab, sRGBColor)
    return sRGBColor.get_rgb_hex(rgb)

protein_scheme = {aa: lab_to_hex(*color) for aa, color in zip(amino_acids, colors_lab)}
protein_scheme.update({'-': '#FFFFFF', '?': '#808080', '*': '#808080'})  # Símbolos especiales

# --- 5. Guardar ---
with open("protein_colors.json", "w") as f:
    json.dump(protein_scheme, f, indent=2)