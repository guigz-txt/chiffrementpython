from rsagestion import RsaGestion


def main():
    rsa = RsaGestion()

    # La machine de déchiffrement possède la clé privée
    rsa.chargement_clef_privee("clef_privee.pem")

    # Déchiffrement du fichier reçu
    message = rsa.dechiffre_fichier("message_chiffre.txt")

    print("Message déchiffré :")
    print(message)

    with open("message_dechiffre.txt", "w", encoding="utf-8") as f:
        f.write(message)


if __name__ == "__main__":
    main()
