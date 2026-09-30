from rsagestion import RsaGestion


def main():
    rsa = RsaGestion()

    # La machine de chiffrement possède uniquement la clé publique
    rsa.chargement_clef_publique("clef_public.pem")

    message = "Message envoyé vers une autre machine."

    print("Message original :")
    print(message)

    rsa.chiffre_dans_fichier(message, "message_chiffre.txt")

    print("\nMessage chiffré enregistré dans message_chiffre.txt")


if __name__ == "__main__":
    main()
