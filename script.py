import os
import shutil

# Chemin de base
base_path = r"C:\Users\doubl\Documents\GitHub\exost_images"

# Premier choix : type d'opération
print("Mode de traitement :")
print("1 = Déplacer les fichiers depuis les sous-dossiers vers la racine (male/female)")
print("2 = Renommer les fichiers déjà dans la racine en supprimant le préfixe 'male_' ou 'female_'")
mode_input = input("Votre choix (1 ou 2) : ").strip()

if mode_input not in ["1", "2"]:
    print("Choix invalide. Veuillez entrer 1 ou 2.")
    exit()

# Choix du genre
gender_input = input("Choisissez un genre (0 = female, 1 = male) : ").strip()
gender = "male" if gender_input == "1" else "female"
prefix = gender + "_"

# Cible principale
target_dir = os.path.join(base_path, gender)

if not os.path.isdir(target_dir):
    print(f"Erreur : le dossier {target_dir} n'existe pas.")
    exit()

files_processed = 0

# MODE 1 : déplacement depuis sous-dossiers
if mode_input == "1":
    print("\nSous-mode :")
    print("1 = Conserver les noms de fichiers")
    print("2 = Retirer le préfixe 'male_' ou 'female_' lors du déplacement")
    submode = input("Votre choix (1 ou 2) : ").strip()

    if submode not in ["1", "2"]:
        print("Choix invalide.")
        exit()

    for folder in os.listdir(target_dir):
        folder_path = os.path.join(target_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        for file in os.listdir(folder_path):
            if file.endswith(".png"):
                src_path = os.path.join(folder_path, file)

                # Suppression du préfixe si demandé
                if submode == "2" and file.startswith(prefix):
                    new_file = file[len(prefix):]
                else:
                    new_file = file

                dst_path = os.path.join(target_dir, new_file)

                # Résolution de conflit
                if os.path.exists(dst_path):
                    base, ext = os.path.splitext(new_file)
                    i = 1
                    while os.path.exists(os.path.join(target_dir, f"{base}_{i}{ext}")):
                        i += 1
                    dst_path = os.path.join(target_dir, f"{base}_{i}{ext}")

                shutil.move(src_path, dst_path)
                print(f"✅ {file} → {os.path.basename(dst_path)}")
                files_processed += 1

        # Suppression du dossier s’il est vide
        if not os.listdir(folder_path):
            os.rmdir(folder_path)
            print(f"🗑️ Supprimé dossier vide : {folder_path}")

# MODE 2 : renommage direct dans la racine
elif mode_input == "2":
    for file in os.listdir(target_dir):
        if file.endswith(".png") and file.startswith(prefix):
            src = os.path.join(target_dir, file)
            new_name = file[len(prefix):]
            dst = os.path.join(target_dir, new_name)

            if os.path.exists(dst):
                base, ext = os.path.splitext(new_name)
                i = 1
                while os.path.exists(os.path.join(target_dir, f"{base}_{i}{ext}")):
                    i += 1
                dst = os.path.join(target_dir, f"{base}_{i}{ext}")

            os.rename(src, dst)
            print(f"✅ Renommé : {file} → {os.path.basename(dst)}")
            files_processed += 1

print(f"\n✅ {files_processed} fichiers traités avec succès pour : {gender}")
