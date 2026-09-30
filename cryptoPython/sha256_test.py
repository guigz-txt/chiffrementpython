from hashgestion import HashGestion


def main():
    hash_gestion = HashGestion()

    print("=== SHA256 ===")

    fichier_texte = "test.txt"
    fichier_binaire = "test.bin"

    print(f"Hash de {fichier_texte} :")
    print(hash_gestion.calculate_file_sha256(fichier_texte))

    print(f"\nHash de {fichier_binaire} :")
    print(hash_gestion.calculate_file_sha256(fichier_binaire))


if __name__ == "__main__":
    main()
