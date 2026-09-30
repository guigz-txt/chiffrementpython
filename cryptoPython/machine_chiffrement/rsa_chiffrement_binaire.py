from rsagestion import RsaGestion


def main():
    rsa = RsaGestion()

    # Chargement de la clé publique
    rsa.chargement_clef_publique("clef_public.pem")

    fichier_entree = "fichier_test.bin"
    fichier_sortie = "fichier_chiffre.bin"

    print("Fichier à chiffrer :", fichier_entree)

    rsa.chiffrement_fichier(
        fichier_entree,
        fichier_sortie,
        format64=False
    )

    print("Fichier chiffré créé :", fichier_sortie)


if __name__ == "__main__":
    main()
