import os
import shutil

# Chemin de base
base_path = r"C:\Users\doubl\Documents\GitHub\exost_images\male"

# Demande du genre
gender_input = input("Choisissez un genre (0 = female, 1 = male) : ").strip()
gender = "male" if gender_input == "1" else "female"

# Dossier cible (male ou female)
target_dir = os.path.join(base_path, gender)

if not os.path.isdir(target_dir):
    print(f"Erreur : le dossier {target_dir} n'existe pas.")
    exit()

# Parcours des sous-dossiers
for folder in os.listdir(target_dir):
    folder_path = os.path.join(target_dir, folder)

    if not os.path.isdir(folder_path):
        continue  # Ignore les fichiers

    for file in os.listdir(folder_path):
        if file.endswith(".png"):
            src_path = os.path.join(folder_path, file)
            dst_path = os.path.join(target_dir, file)

            # Gérer les conflits éventuels
            if os.path.exists(dst_path):
                print(f"Conflit détecté pour {file}, renommage automatique...")
                base, ext = os.path.splitext(file)
                i = 1
                while os.path.exists(os.path.join(target_dir, f"{base}_{i}{ext}")):
                    i += 1
                dst_path = os.path.join(target_dir, f"{base}_{i}{ext}")

            shutil.move(src_path, dst_path)
            print(f"Déplacé : {file} → {gender}/")

print("✅ Tous les fichiers .png ont été déplacés à la racine du dossier :", gender)
