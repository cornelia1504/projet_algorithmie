import tkinter as tk
from tkinter import messagebox, filedialog
import bwt as b

def display_steps():
    """
    Affiche chaque étape de la transformation BWT dans une boîte de dialogue.

    """
    sequence = sequence_entry.get()

    # Effectue la transformation BWT et récupère la table non triée
    table_no_sorted = b.bwt_transform(sequence)[1]
    
    # Parcourt chaque étape de la table non triée
    for i, bwt in enumerate(table_no_sorted):
        # Affiche une boîte de dialogue avec l'étape actuelle de la transformation BWT
        messagebox.showinfo(f"Step {i + 1}", bwt)


def display():
    """
    Affiche la séquence transformée avec les étapes de la transformation BWT.
    """
    # Récupère la séquence saisie dans le champ de saisie
    sequence = sequence_entry.get()
    
    # Vérifie si une séquence est saisie
    if sequence:
        # Effectue la transformation BWT sur la séquence
        transformed_sequence = b.bwt_transform(sequence)
        
        # Affiche une boîte de dialogue avec la séquence transformée
        messagebox.showinfo("BWT Transformation", f"{transformed_sequence}")
        # Appelle la fonction pour afficher les étapes de la transformation BWT
        # display_steps(sequence)


def transform_sequence():
    """
    Transforme la séquence saisie en utilisant l'algorithme BWT.
    """
    # Récupère la séquence saisie dans le champ de saisie
    sequence = sequence_entry.get()
    
    # Vérifie si une séquence est saisie
    if sequence:
        # Effectue la transformation BWT sur la séquence
        transformed_sequence, _ = b.bwt_transform(sequence)
        
        # Affiche une boîte de dialogue avec la séquence transformée
        messagebox.showinfo("BWT Transformation", f"Transformed sequence:\n{transformed_sequence}")


def detransform_sequence():
    """
    Détransforme la séquence transformée en utilisant l'algorithme BWT.
    """
    # Récupère la séquence saisie dans le champ de saisie
    sequence = sequence_entry.get()

    # Effectue la transformation BWT sur la séquence
    transformed_sequence, _ = b.bwt_transform(sequence)
    
    # Vérifie si une séquence transformée est présente
    if transformed_sequence:
        # Effectue la détransformation BWT sur la séquence transformée
        inverse_sequence = b.detransform_bwt(transformed_sequence)
        
        # Affiche une boîte de dialogue avec la séquence détransformée
        messagebox.showinfo("BWT Detransformation", f"Inverse sequence:\n{inverse_sequence}")
        
        # Sauvegarde les résultats dans un fichier
        b.save_results(sequence_entry.get(), transformed_sequence, inverse_sequence)


def browse_file():
    """
    Ouvre une boîte de dialogue pour sélectionner un fichier FASTA et insère son contenu dans le champ de saisie.
    """
    # Ouvre une boîte de dialogue pour sélectionner un fichier FASTA
    file_path = filedialog.askopenfilename(filetypes=[("FASTA files", "*.fasta" or "*.fa")])
    
    # Vérifie si un fichier a été sélectionné
    if file_path:
        # Traite le contenu du fichier FASTA
        sequences = b.process_fasta_file(file_path)
        
        # Vérifie si des séquences ont été récupérées
        if sequences:
            # Supprime le contenu actuel du champ de saisie
            sequence_entry.delete(0, tk.END)
            
            # Insère la première séquence dans le champ de saisie
            sequence_entry.insert(tk.END, sequences[0])


def save_bwt():
    """
    Sauvegarde la séquence originale, transformée et détransformée dans un fichier.
    """
    # Récupère la séquence saisie dans le champ de saisie
    sequence = sequence_entry.get()
    
    # Effectue la transformation BWT sur la séquence
    bwt_sequence = b.bwt_transform(sequence)[0]
    
    # Effectue la détransformation BWT sur la séquence transformée
    inverse_sequence = b.detransform_bwt(bwt_sequence)
    
    # Sauvegarde les résultats dans un fichier
    b.save_results(sequence, bwt_sequence, inverse_sequence)
    
    # Affiche une boîte de dialogue avec le message de sauvegarde
    messagebox.showinfo("Sauvegarder", f"Transformation sauvegardée dans le fichier : bwt_results.txt")



# Créer une fenêtre
window = tk.Tk()

# Définir la taille de la fenêtre
window.geometry("400x300")

# Définir le titre de la fenêtre
window.title("BWT Transformation")

# Créer une étiquette pour le champ de saisie
label = tk.Label(window, text="Enter sequence ")
label.pack()

# Créer un champ de saisie
sequence_entry = tk.Entry(window)
sequence_entry.pack()

# Créer un bouton pour parcourir les fichiers
browse_button = tk.Button(window, text="Choose a FASTA file \n Browse", command=browse_file)
browse_button.pack()

# Créer un bouton pour la transformation
transform_button = tk.Button(window, text="Transform", command=transform_sequence)
transform_button.pack()

# Créer un bouton pour afficher les étapes de transformation en matrice
transform_button = tk.Button(window, text="Transform matrix", command=display)
transform_button.pack()

# Créer un bouton pour afficher les étapes de transformation
transform_button = tk.Button(window, text="Transform Step", command=display_steps)
transform_button.pack()

# Créer un bouton pour la détransformation
detransform_button = tk.Button(window, text="Detransform", command=detransform_sequence)
detransform_button.pack()

# Créer un bouton pour sauvegarder les résultats
detransform_button = tk.Button(window, text="Save", command=save_bwt) 
detransform_button.pack()

# Lancer la boucle principale de la fenêtre
window.mainloop()
