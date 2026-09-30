from aesgestion import AesGestion


def main():
    aes = AesGestion()

    # Génération et sauvegarde de la clé AES
    aes.generate_aes_key()
    aes.save_aes_key_to_file("clef_aes.bin")

    message = "Bonjour, ceci est un message chiffré avec AES."

    print("Message original :")
    print(message)

    # Chiffrement
    message_chiffre = aes.encrypt_string_to_base64(message)

    print("\nMessage chiffré :")
    print(message_chiffre)

    # Déchiffrement
    message_dechiffre = aes.decrypt_string_from_base64(message_chiffre)

    print("\nMessage déchiffré :")
    print(message_dechiffre)


if __name__ == "__main__":
    main()
