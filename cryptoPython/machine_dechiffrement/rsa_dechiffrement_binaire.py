from rsagestion import RsaGestion


def main():
    rsa = RsaGestion()

    # Chargement de la clé privée
    rsa.chargement_clef_privee("clef_privee.pem")

    fichier_entree = "fichier_chiffre.bin"
    fichier_sortie = "fichier_dechiffre.bin"

    print("Fichier à déchiffrer :", fichier_entree)

    rsa.dechiffrement_fichier(
        fichier_entree,
        fichier_sortie,
        format64=False
    )

    print("Fichier déchiffré créé :", fichier_sortie)


if __name__ == "__main__":
    main()
