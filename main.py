# Imports
import json
import subprocess
import os

def create_backup():
    print('''
------- 📌 CONNEXION DB -------''')
    connect_db = {
        "host": input("🔹 Host du serveur PostgreSQL : "),
        "database": input("🔹 Nom db PostgreSQL : "),
        "user": input("🔹 Nom d'utilisateur PostgreSQL : "),
        "password": input("🔹 Mot de passe PostgreSQL : "),
        "port": input("🔹 Port PostgreSQL : ")
    }

    os.environ["PGPASSWORD"] = connect_db["password"]  

    backup_path = r"C:\code\TIB\backups\backup.sql"  
    print("🔄 Création du backup...")

    try:
        subprocess.run(
            ["pg_dump", "-U", connect_db["user"], "-h", connect_db["host"], "-p", connect_db["port"],
             "-F", "c", "-b", "-v", "-f", backup_path, connect_db["database"]],
            check=True
        )
        print(f"✅ Backup de {connect_db['database']} effectuée avec succès !")
        print(f"📂 Fichier sauvegardé : {backup_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue : {e}")

def dev() :
    print(''' ❌ Fonctionnalité en cour de dev
Repository du projet : https://github.com/tmloff/tib''')
    menu()
    
def menu() : 
    print('''
---------  📌MENU   ---------        
1️⃣ Créer un backup
2️⃣ Restaurer un backup
3️⃣ Pousser le backup sur GitHub
4️⃣ Configuration''')
    option = input("🔹 Choisissez une option (1, 2, 3 ou 4) : ")
    
    if option == "1":
        create_backup()
    elif option == "2":
        dev()
    elif option == "3":
        dev()
    elif option == "4":
        dev()
    else :
        print("❌ Option non valide")

def start() :
    print('''
            ████████╗██╗██████╗░
            ╚══██╔══╝██║██╔══██╗
            ░░░██║░░░██║██████╦╝
            ░░░██║░░░██║██╔══██╗
            ░░░██║░░░██║██████╦╝
            ░░░╚═╝░░░╚═╝╚═════╝░
        Transfer, Integrate, Backup

===============================================
=  Versiion : 0.0.1                           =
=  Créateur : TML (Timéo Menvielle Larrouy)   =
=  Contributeurs : 0                          =
=  Mise à jour : 27/02/2025                   =
===============================================


''')
    menu()
start()