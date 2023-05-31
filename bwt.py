def bwt_transform(sequence):
    """
    Transforme une séquence en utilisant l'algorithme de transformation de Burrows-Wheeler (BWT).

    Returns:
        tuple: Un tuple contenant la séquence transformée et la table des rotations non triée.
    """
    # Verifie que l'entrée ne contient pas le symbole $
    assert '$' not in sequence  

    # Ajouter le marqueur de début et de fin de texte
    if type(sequence) == "str":
        sequence = '$' + sequence 
    else: # si la sequence est une liste obtenu `a partir du fichier fasta
        sequence = '$' + ''.join(sequence)  # Convertit la liste en une chaîne de caractères
    # Créer la table des rotations
    table_no_sorted = [sequence[i:] + sequence[:i] for i in range(len(sequence))]
    #table_no_sorted.reverse
    table_no_sorted = table_no_sorted[::-1]
    print(table_no_sorted)
    # Trier la table des rotations
    table = sorted(table_no_sorted)
    # Récupérer la dernière colonne de la table (symboles BWT)
    bwt = ''.join(row[-1] for row in table)

    return bwt, table_no_sorted


def detransform_bwt(bwt_sequence):
    """
    Réalise la détransformation de la séquence transformée en utilisant l'algorithme de Burrows-Wheeler (BWT).

    Returns:
        str: La séquence détransformée.
    """
    # Crée une liste de chaînes vides de même longueur que la séquence transformée
    table = [''] * len(bwt_sequence)  
    for i in range(len(bwt_sequence)):
        # Ajoute la colonne 'r' en concaténant chaque caractère de la séquence transformée avec la chaîne correspondante dans la table
        table = [bwt_sequence[i] + table[i] for i in range(len(bwt_sequence))]  
         # Trie la table des rotations
        table = sorted(table) 
        
    # Trouve la bonne ligne dans la table qui se termine par le symbole de fin $
    inverse_bwt = [row for row in table if row.endswith("$")][0]  
    # Supprime les marqueurs de début et de fin de la séquence
    inverse_bwt = inverse_bwt.rstrip('$')  
    # Affiche la séquence détransformée
    print(inverse_bwt)  

    # Retourne la séquence détransformée
    return inverse_bwt  

def process_fasta_file(file_path):
    """ 
    lecture du fichier et extraction de la sequence 
    """
    sequences = []  # Crée une liste où sera stockée la séquence
    current_sequence = ""  # Variable pour stocker la séquence courante en cours de lecture

    with open(file_path, "r") as file:  # Ouvre le fichier en mode lecture
        for line in file:  # Parcourt chaque ligne du fichier
            line = line.strip()  # Supprime les espaces vides avant et après la ligne

            if line.startswith(">"):  # Si la ligne commence par ">"
                if current_sequence:  # Si une séquence courante est en cours de lecture
                    sequences.append(current_sequence)  # Ajoute la séquence courante à la liste des séquences
                    current_sequence = ""  # Réinitialise la séquence courante

            else:  # Si la ligne ne commence pas par ">"
                current_sequence += line  # Ajoute la ligne à la séquence courante

        if current_sequence:  # Si une séquence courante est encore présente après avoir parcouru toutes les lignes du fichier
            sequences.append(current_sequence)  # Ajoute la séquence courante à la liste des séquences

    return sequences  # Retourne la liste des séquences extraites du fichier FASTA


def save_results(original_sequence, transformed_sequence, inverse_sequence):
    """
    Sauvegarde les résultats de la transformation BWT dans un fichier texte.

    """
    # ouvre un fichier texte
    with open("bwt_results.txt", "w") as file:
        # ecrit la sequence originale 
        file.write("Séquence originale:\n")
        
        if type(original_sequence) == "str":
            file.write(original_sequence + "\n\n")

        else: # si la sequence est une liste obtenu `a partir du fichier fasta
            original_sequence =''.join(original_sequence)  # Convertit la liste en une chaîne de caractères
            file.write(original_sequence + "\n\n")
        # ecrit la sequence  transformee
        file.write("Transformée de BWT:\n")
        file.write(transformed_sequence + "\n\n")  
        # ecrit la sequence  originale `a partir de la transformee
        file.write("Détransformée:\n")
        file.write(inverse_sequence)
    # ecrit le message de sauvegarde 
    print("\n Transformation sauvegardee dans le fichier : bwt_results.txt")


def display_steps(sequence):
    """
    Affiche chaque étape de la transformation BWT dans une boîte de dialogue.

    """

    # Effectue la transformation BWT et récupère la table non triée
    table_no_sorted = bwt_transform(sequence)[1]
    
    # Parcourt chaque étape de la table non triée
    for i, bwt in enumerate(table_no_sorted):
        # Affiche une boîte de dialogue avec l'étape actuelle de la transformation BWT
        print(f"Step {i + 1}", bwt)
        input("appyez sur entrer  pour voir la suite ")
        
def choice():
    """Dialogue avec l'utilisateur"""
    # Demande à l'utilisateur de choisir entre copier une séquence ou ouvrir un fichier
    choix = input('Tapez 1 pour copier la séquence / 2 pour ouvrir un fichier : ')
    
    if choix == str(1) or choix == str(2):  # Si le choix est 1 ou 2
        if choix == str(2):  # Si le choix est 2
            file_path = input("Veuillez entrer le chemin vers votre fichier FASTA : ")
            sequence = process_fasta_file(file_path)  # Appelle la fonction pour extraire la séquence du fichier FASTA
        else:  # Si le choix est 1
            sequence = input("Veuillez copier la séquence : ")
            
        bwt_sequence = bwt_transform(sequence)[0]  # Applique la transformation BWT à la séquence
        
        choix2 = input('Voulez-vous afficher les étapes de la transformation ? O/N ? :')
        if choix2 == "O" or choix2 == "N":  # Si le choix est O ou N
            if choix2 == "O": 
                display_steps(sequence)  # Appelle la fonction pour afficher les étapes de la transformation
        else:
            print("Choix incompris !")
        
        choix3 = input("Voulez-vous inverser la transformation ? O/N ? :")
        if choix3 == "O" or choix3 == "N":  # Si le choix est O ou N
            if choix3 == "O": 
                inverse_sequence = detransform_bwt(bwt_sequence)  # Détransforme la séquence BWT
        else:
            print("Choix incompris !")
        
        choix4 = input("Voulez-vous sauvegarder les résultats ? O/N ? :")
        if choix4 == "O" or choix4 == "N":  # Si le choix est O ou N
            if choix4 == "O" and choix3 == "O": 
                save_results(sequence, bwt_sequence, inverse_sequence)  # Sauvegarde les résultats
            else:  
                inverse_sequence = " "
                save_results(sequence, bwt_sequence, inverse_sequence)  # Sauvegarde les résultats
        else:
            print("Choix incompris !")
        
    else:
        print("Choisissez 1 ou 2.")
        choice()  # Appel récursif de la fonction choice() pour redemander le choix si le choix n'est ni 1 ni 2

            
if __name__ == "__main__":
    #sequence = 'ATTTCCGCCCGTAGAGAGCAAATT'
    choice()
    