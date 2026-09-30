from aesgestion import AesGestion

def main():
    aes = AesGestion()

    # Chargement de la clé AES générée précédemment
    aes.load_aes_key_from_file("clef_aes.bin")

    fichier_entree = "fichier_test.txt"
    fichier_chiffre = "fichier_chiffre_aes.bin"
    fichier_dechiffre = "fichier_dechiffre_aes.txt"

    # Création du fichier de test
    with open(fichier_entree, "w", encoding="utf-8") as f:
        f.write("Bonjour, ceci est un fichier de test chiffré avec AES.")

    print("Fichier original :", fichier_entree)

    # Chiffrement
    aes.encrypt_file(fichier_entree, fichier_chiffre)
    print("Fichier chiffré :", fichier_chiffre)

    # Déchiffrement
    aes.decrypt_file(fichier_chiffre, fichier_dechiffre)
    print("Fichier déchiffré :", fichier_dechiffre)

    # Vérification
    with open(fichier_dechiffre, "r", encoding="utf-8") as f:
        contenu = f.read()

    print("\nContenu déchiffré :")
    print(contenu)

if __name__ == "__main__":
    main()
