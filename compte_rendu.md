# TP Chiffrement en Python

## Q1

Création d'un dépôt Git local avec `git init`, puis ajout des fichiers fournis dans le dépôt.

## Q2

Les classes fournies sont :

- `HashGestion` pour le hachage SHA256.
- `AesGestion` pour le chiffrement AES.
- `RsaGestion` pour le chiffrement RSA.

## Q3. Différence entre hachage et chiffrement

Le hachage transforme une donnée en une empreinte de taille fixe. Il est conçu pour être à sens unique : on ne doit pas pouvoir retrouver directement la donnée originale à partir de l'empreinte.

Le chiffrement transforme une donnée en une donnée chiffrée qui peut être retrouvée grâce à une clé de déchiffrement.

## Q4. But du hachage

Le hachage permet principalement de vérifier l'intégrité d'une donnée.

Une modification du fichier ou du message entraîne normalement une empreinte différente.

Le hachage seul ne permet pas d'assurer la confidentialité du contenu.
