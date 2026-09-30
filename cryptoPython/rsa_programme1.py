from rsagestion import RsaGestion


def main():
    rsa = RsaGestion()

    fichier_public = "clef_public.pem"
    fichier_prive = "clef_privee.pem"

    # Génération de la paire de clés RSA
    rsa.generation_clef(fichier_public, fichier_prive, 2048)

    # Message à chiffrer
    message = "Bonjour, ceci est un message secret."

    print("\nMessage original :")
    print(message)

    # Chiffrement avec la clé publique
    message_chiffre = rsa.chiffrement_rsa(message)

    print("\nMessage chiffré :")
    print(message_chiffre)

    # Déchiffrement avec la clé privée
    message_dechiffre = rsa.dechiffrement_rsa(message_chiffre)

    print("\nMessage déchiffré :")
    print(message_dechiffre)


if __name__ == "__main__":
    main()
