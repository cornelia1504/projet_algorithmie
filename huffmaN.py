import heapq
import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter as tk
from tkinter import ttk

import bwt as b
#import bwt as b

# Définition des classes Node et Leaf pour la construction de l'arbre de Huffman
class Node:
    def __init__(self, left=None, right=None):
        self.left = left  # Le sous-arbre gauche du nœud
        self.right = right  # Le sous-arbre droit du nœud

    def __repr__(self):
        return f"[{repr(self.left)}, {repr(self.right)}]"
        # Renvoie une représentation sous forme de chaîne de caractères du nœud et de ses sous-arbres.


class Leaf:
    def __init__(self, char):
        self.char = char  # Le caractère associé à la feuille

    def __repr__(self):
        return repr(self.char)
        # Renvoie une représentation sous forme de chaîne de caractères du caractère de la feuille.



def build_huffman_tree(frequencies):
    """
    Construit un arbre de Huffman à partir des fréquences des caractères.
    Node: Racine de l'arbre de Huffman.

    """

    heap = []  # Tas binaire pour stocker les nœuds de l'arbre
    for char, freq in frequencies.items():
        leaf = Leaf(char)  # Crée un nœud feuille pour chaque caractère avec sa fréquence
        heapq.heappush(heap, (freq, id(leaf), leaf))  # Ajoute le nœud feuille au tas

    while len(heap) > 1:
        # Extraction des deux nœuds de poids minimum du tas
        weight1, _, left = heapq.heappop(heap)
        weight2, _, right = heapq.heappop(heap)

        # Crée un nouveau nœud interne avec les nœuds extraits comme fils
        new_node = Node(left, right)

        # Calcule le poids du nouveau nœud en additionnant les poids des fils
        new_weight = weight1 + weight2

        # Ajoute le nouveau nœud au tas avec son poids et son ID
        heapq.heappush(heap, (new_weight, id(new_node), new_node))

    # À la fin, le tas contient un seul nœud qui est la racine de l'arbre de Huffman
    _, _, root = heapq.heappop(heap)
    return root



def generate_huffman_code(node, code, current_code=""):
    """
    Génère le code de Huffman pour chaque caractère de l'arbre de Huffman.
    
        - node : Le nœud actuel de l'arbre de Huffman.
        - code : Le dictionnaire qui stockera le code de Huffman pour chaque caractère.
        - current_code : Le code de Huffman actuel (par défaut : chaîne vide).
    """
    if isinstance(node, Leaf):
        code[node.char] = current_code or "0"
        # Si le nœud est une feuille, on associe le code de Huffman actuel au caractère de la feuille
        # dans le dictionnaire code. Si le code de Huffman actuel est vide, on utilise "0" par défaut.

    elif isinstance(node, Node):
        generate_huffman_code(node.left, code, current_code + "0")
        # Si le nœud est un nœud interne, on explore le sous-arbre gauche en ajoutant "0" au code de Huffman actuel.

        generate_huffman_code(node.right, code, current_code + "1")
        # On explore ensuite le sous-arbre droit en ajoutant "1" au code de Huffman actuel.


def encode_sequence(sequence, huffman_code):
    """
    Encode une séquence en utilisant le code de Huffman donné.
        - sequence : La séquence à encoder.
        - huffman_code : Le dictionnaire qui contient le code de Huffman pour chaque caractère.

    """
    encoded_sequence = ""
    for char in sequence:
        encoded_sequence += huffman_code[char]
        # Pour chaque caractère de la séquence, on ajoute le code de Huffman correspondant
        # à la séquence encodée.

    return encoded_sequence



def decode_sequence(encoded_sequence, huffman_tree):
    """
    Décode une séquence encodée en utilisant l'arbre de Huffman donné.
        - encoded_sequence : La séquence encodée.
        - huffman_tree : L'arbre de Huffman utilisé pour le décodage.
    """
    decoded_sequence = ""
    current_node = huffman_tree
    for bit in encoded_sequence:
        if bit == "0":
            current_node = current_node.left
            # Si le bit est "0", on se déplace vers le nœud gauche de l'arbre de Huffman.
        elif bit == "1":
            current_node = current_node.right
            # Si le bit est "1", on se déplace vers le nœud droit de l'arbre de Huffman.

        if isinstance(current_node, Leaf):
            decoded_sequence += current_node.char
            current_node = huffman_tree
            # Si le nœud courant est une feuille, cela signifie qu'on a atteint un caractère décodé.
            # On l'ajoute à la séquence décodée et on revient à la racine de l'arbre de Huffman.

    return decoded_sequence


def compress_sequence(sequence, huffman_code):
    """
    Compresse une séquence en utilisant le code de Huffman donné.
        - sequence : La séquence à compresser.
        - huffman_code : Le dictionnaire qui contient le code de Huffman pour chaque caractère.
    """
    compressed_sequence = ""
    for char in sequence:
        compressed_sequence += huffman_code[char]
        # Pour chaque caractère de la séquence, on ajoute le code de Huffman correspondant
        # à la séquence compressée.

    return compressed_sequence


def decompress_sequence(compressed_sequence, huffman_tree):
    """
    Décompresse une séquence compressée en utilisant l'arbre de Huffman donné.
        - compressed_sequence : La séquence compressée.
        - huffman_tree : L'arbre de Huffman utilisé pour la décompression.
    """
    decompressed_sequence = ""
    current_node = huffman_tree
    for bit in compressed_sequence:
        if bit == "0":
            current_node = current_node.left
            # Si le bit est "0", on se déplace vers le nœud gauche de l'arbre de Huffman.
        elif bit == "1":
            current_node = current_node.right
            # Si le bit est "1", on se déplace vers le nœud droit de l'arbre de Huffman.

        if isinstance(current_node, Leaf):
            decompressed_sequence += current_node.char
            current_node = huffman_tree
            # Si le nœud courant est une feuille, cela signifie qu'on a atteint un caractère décompressé.
            # On l'ajoute à la séquence décompressée et on revient à la racine de l'arbre de Huffman.

    return decompressed_sequence




#sequence = "TCATGGA$GGTCCCAAACCTGTATA"

sequence= input("copiez la sequence a compresse : ")
#sequence = "NNTNACTTNGNNGTTNCCTATACCT"
#sequence = b.bwt_transform(sequence)  # Applique la transformation BWT à la séquence

print(sequence)
def frequence(sequence):
    # Construction du dictionnaire de fréquences
    frequencies = {}

    # Parcourt chaque caractère dans la séquence
    for char in sequence:
        # Vérifie si le caractère existe déjà dans le dictionnaire des fréquences
        if char in frequencies:
            # Si le caractère existe, incrémente sa fréquence de 1
            frequencies[char] += 1
        else:
            # Si le caractère n'existe pas, initialise sa fréquence à 1
            frequencies[char] = 1
    return frequencies

# Construction de l'arbre de Huffman
frequencies = frequence(sequence)
huffman_tree = build_huffman_tree(frequencies)

# Génération du code de Huffman
huffman_code = {}
generate_huffman_code(huffman_tree, huffman_code)

# Encodage de la séquence transformée
encoded_sequence = encode_sequence(sequence, huffman_code)

# Compression de la séquence en une chaîne de caractères
compressed_sequence = compress_sequence(sequence, huffman_code)

# Décompression de la chaîne binaire en acides nucléiques
decompressed_sequence = decode_sequence(encoded_sequence, huffman_tree)


def save_results(huffman_tree, huffman_code,encoded_sequence, decompressed_sequence):
    """
    Sauvegarde les résultats de la coompression dans un fichier texte.

    """
    # ouvre un fichier texte
    with open("huffman_results.txt", "w") as file:
        # ecrit la sequence originale 
        file.write("Séquence originale:\n")
        
        if type(sequence) == "str":
            file.write(sequence + "\n\n")

        # ecrit la sequence  transformee
        file.write("Arbre de Huffman:\n")
        file.write(repr(huffman_tree) + "\n\n")  
        # ecrit la sequence  originale `a partir de la transformee
        file.write("Code associé:\n")
        file.write(str(huffman_code))
        file.write("Encodage de la transformée:\n")
        file.write(encoded_sequence)
    # ecrit le message de sauvegarde 
    print("\n Transformation sauvegardee dans le fichier : hufman_results.txt")

# Affichage des résultats
print(frequencies)
print("Arbre de Huffman:")
print(repr(huffman_tree))
print("Code associé:")
print(huffman_code)
print("Encodage de la transformée:")
print(encoded_sequence)
print("Compressage en terme de chaîne de charactère:")
print(compressed_sequence) #no
print()
print("Décompressage en acide nucleique:")
print(decompressed_sequence)
save_results(huffman_tree, huffman_code,encoded_sequence, decompressed_sequence)

####################################
#ici c est la fonction avec laquelle j'ai tente d'afficher les resulats
# Fonction pour afficher les résultats
def display_results(frequencies, huffman_tree, huffman_code, encoded_sequence, compressed_sequence, decompressed_sequence):
    window = tk.Tk()
    window.title("Résultats de compression de séquence")

    # Création du tableau pour afficher les fréquences
    frequencies_frame = ttk.LabelFrame(window, text="Fréquences des caractères")
    frequencies_frame.pack(padx=10, pady=10)

    frequencies_table = ttk.Treeview(frequencies_frame, columns=("Character", "Frequency"), show="headings")
    frequencies_table.heading("Character", text="Caractère")
    frequencies_table.heading("Frequency", text="Fréquence")

    for char, freq in frequencies.items():
        frequencies_table.insert("", "end", values=(char, freq))

    frequencies_table.pack()

    # Affichage de l'arbre de Huffman
    huffman_tree_frame = ttk.LabelFrame(window, text="Arbre de Huffman")
    huffman_tree_frame.pack(padx=10, pady=10)

    huffman_tree_label = ttk.Label(huffman_tree_frame, text=repr(huffman_tree))
    huffman_tree_label.pack()

    # Affichage du code de Huffman
    huffman_code_frame = ttk.LabelFrame(window, text="Code de Huffman")
    huffman_code_frame.pack(padx=10, pady=10)

    huffman_code_label = ttk.Label(huffman_code_frame, text=huffman_code)
    huffman_code_label.pack()

    # Affichage de la séquence encodée
    encoded_sequence_frame = ttk.LabelFrame(window, text="Séquence encodée")
    encoded_sequence_frame.pack(padx=10, pady=10)

    encoded_sequence_label = ttk.Label(encoded_sequence_frame, text=encoded_sequence)
    encoded_sequence_label.pack()

    # Affichage de la séquence compressée
    compressed_sequence_frame = ttk.LabelFrame(window, text="Séquence compressée")
    compressed_sequence_frame.pack(padx=10, pady=10)

    compressed_sequence_label = ttk.Label(compressed_sequence_frame, text=compressed_sequence)
    compressed_sequence_label.pack()

    # Affichage de la séquence décompressée
    decompressed_sequence_frame = ttk.LabelFrame(window, text="Séquence décompressée")
    decompressed_sequence_frame.pack(padx=10, pady=10)

    decompressed_sequence_label = ttk.Label(decompressed_sequence_frame, text=decompressed_sequence)
    decompressed_sequence_label.pack()

    window.mainloop()

display_results(frequencies, huffman_tree, huffman_code, encoded_sequence, compressed_sequence, decompressed_sequence)

####################################