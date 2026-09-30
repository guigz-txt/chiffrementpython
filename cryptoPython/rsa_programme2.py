from rsagestion import RsaGestion


def main():
    rsa = RsaGestion()

    fichier_public = "clef_public.pem"
    fichier_prive = "clef_privee.pem"
    fichier_chiffre = "message_chiffre.txt"
    fichier_dechiffre = "message_dechiffre.txt"

    # Chargement des clés depuis les fichiers
    rsa.chargement_clefs(fichier_public, fichier_prive)

    message = "Bonjour, ceci est le deuxième test RSA."

    print("Message original :")
    print(message)

    # Chiffrement dans un fichier
    rsa.chiffre_dans_fichier(message, fichier_chiffre)

    print("\nMessage chiffré enregistré dans :", fichier_chiffre)

    # Déchiffrement du fichier
    message_dechiffre = rsa.dechiffre_fichier(fichier_chiffre)

    print("\nMessage déchiffré :")
    print(message_dechiffre)

    # Sauvegarde du message déchiffré
    with open(fichier_dechiffre, "w", encoding="utf-8") as f:
        f.write(message_dechiffre)

    print("\nMessage déchiffré enregistré dans :", fichier_dechiffre)


if __name__ == "__main__":
    main()
