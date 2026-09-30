import base64
from aesgestion import AesGestion
from rsagestion import RsaGestion


def main():
    # ==============================
    # 1. Chargement des clés RSA
    # ==============================

    rsa = RsaGestion()

    rsa.chargement_clefs(
        "machine_chiffrement/clef_public.pem",
        "machine_dechiffrement/clef_privee.pem"
    )

    # ==============================
    # 2. Génération de la clé AES
    # ==============================

    aes = AesGestion()
    aes.generate_aes_key()

    # Conversion de la clé AES en Base64
    cle_aes_base64 = base64.b64encode(aes.aes_key).decode("utf-8")

    print("Clé AES générée.")

    # ==============================
    # 3. Chiffrement de la clé AES
    #    avec RSA
    # ==============================

    cle_aes_chiffree = rsa.chiffrement_rsa(cle_aes_base64)

    with open("cle_aes_chiffree.txt", "w", encoding="utf-8") as f:
        f.write(cle_aes_chiffree)

    print("Clé AES chiffrée avec RSA.")

    # ==============================
    # 4. Chiffrement du message
    #    avec AES
    # ==============================

    message = "Bonjour, ceci est un message chiffré avec RSA + AES."

    message_chiffre = aes.encrypt_string_to_base64(message)

    with open("message_hybride_chiffre.txt", "w", encoding="utf-8") as f:
        f.write(message_chiffre)

    print("Message chiffré avec AES.")

    # ==============================
    # 5. Déchiffrement de la clé AES
    #    avec la clé privée RSA
    # ==============================

    with open("cle_aes_chiffree.txt", "r", encoding="utf-8") as f:
        cle_aes_chiffree = f.read()

    cle_aes_base64_dechiffree = rsa.dechiffrement_rsa(
        cle_aes_chiffree
    )

    cle_aes = base64.b64decode(cle_aes_base64_dechiffree)

    print("Clé AES déchiffrée avec RSA.")

    # ==============================
    # 6. Utilisation de la clé AES
    #    récupérée
    # ==============================

    aes_recepteur = AesGestion()
    aes_recepteur.aes_key = cle_aes

    # ==============================
    # 7. Déchiffrement du message
    #    avec AES
    # ==============================

    with open("message_hybride_chiffre.txt", "r", encoding="utf-8") as f:
        message_chiffre = f.read()

    message_dechiffre = aes_recepteur.decrypt_string_from_base64(
        message_chiffre
    )

    print("\nMessage original :")
    print(message)

    print("\nMessage déchiffré :")
    print(message_dechiffre)

    # Vérification
    if message == message_dechiffre:
        print("\nSUCCÈS : le message a été correctement déchiffré.")
    else:
        print("\nERREUR : les messages sont différents.")


if __name__ == "__main__":
    main()
