import os
import subprocess
import datetime
import sys

# Étape 1 : Fonction pour créer un backup
def create_backup():
    host = input("🔹 Adresse du serveur PostgreSQL (ex: localhost) : ")
    user = input("🔹 Nom d'utilisateur PostgreSQL (ex: postgres) : ")
    database = input("🔹 Nom de la base de données : ")
    password = input("🔹 Mot de passe PostgreSQL : ")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dump_file = f"backup_{timestamp}.sql"

    print("🔄 Création du backup...")

    if os.name == "nt":
        dump_command = f'set PGPASSWORD={password} && pg_dump -U {user} -h {host} -d {database} -F c -f {dump_file}'
    else:
        dump_command = f'PGPASSWORD={password} pg_dump -U {user} -h {host} -d {database} -F c -f {dump_file}'

    try:
        subprocess.run(dump_command, shell=True, check=True)
        print(f"✅ Backup créé : {dump_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la création du backup : {e}")

# Étape 2 : Fonction pour restaurer un backup
def restore_backup():
    host = input("🔹 Adresse du serveur PostgreSQL (ex: localhost) : ")
    user = input("🔹 Nom d'utilisateur PostgreSQL (ex: postgres) : ")
    database = input("🔹 Nom de la base de données : ")
    password = input("🔹 Mot de passe PostgreSQL : ")
    backup_file = input("🔹 Nom du fichier de backup à restaurer : ")

    print("🔄 Restauration du backup...")

    if os.name == "nt":
        restore_command = f'set PGPASSWORD={password} && pg_restore -U {user} -h {host} -d {database} -F c {backup_file}'
    else:
        restore_command = f'PGPASSWORD={password} pg_restore -U {user} -h {host} -d {database} -F c {backup_file}'

    try:
        subprocess.run(restore_command, shell=True, check=True)
        print(f"✅ Restauration terminée depuis {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la restauration : {e}")

# Étape 3 : Fonction pour push sur GitHub
def push_backup():
    print("🔄 Ajout du backup au dépôt Git...")
    subprocess.run("git add backup_*.sql", shell=True, check=True)
    subprocess.run('git commit -m "Ajout automatique du backup"', shell=True, check=True)
    subprocess.run("git push", shell=True, check=True)
    print("✅ Backup poussé sur GitHub !")

# Menu principal
def main():
    print("\n📌 Menu :")
    print("1️⃣ Créer un backup")
    print("2️⃣ Restaurer un backup")
    print("3️⃣ Pousser le backup sur GitHub")
    choix = input("🔹 Choisissez une option (1, 2 ou 3) : ")

    if choix == "1":
        create_backup()
    elif choix == "2":
        restore_backup()
    elif choix == "3":
        push_backup()
    else:
        print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
