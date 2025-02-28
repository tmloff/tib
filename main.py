# Imports
import json
import subprocess
import os

Infos_dev = {
    "Version": "0.0.2",
    "Contributeurs" : 0,
    "maj" : "28/02/25"
}

def create_backup():
    with open("data.json", "r", encoding="utf-8") as fichier:
        connect_db = json.load(fichier)

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
        config()
    else :
        print("❌ Option non valide")

def connect_db(modif=False):
    if not modif:
        print('''
------- 📌 CONNEXION DB -------''')
        db_infos = {
            "host": input("🔹 Host du serveur PostgreSQL : "),
            "database": input("🔹 Nom db PostgreSQL : "),
            "user": input("🔹 Nom d'utilisateur PostgreSQL : "),
            "password": input("🔹 Mot de passe PostgreSQL : "),
            "port": input("🔹 Port PostgreSQL : ")
        }
        with open("data.json", "w", encoding="utf-8") as fichier:
            json.dump(db_infos, fichier, indent=4, ensure_ascii=False)
        print("✅ Infos enregistrées")
        return
    
    print('''
------- 🖋️ MODIFICATION DB -------

Info à modifier :
1️⃣  Host du serveur PostgreSQL
2️⃣  Nom db PostgreSQL
3️⃣  Nom d'utilisateur PostgreSQL 
4️⃣  Mot de passe PostgreSQL
5️⃣  Port PostgreSQL

Autres options :
6️⃣  Tout modifier
7️⃣  Retour au menu
''')

    try:
        option = int(input("🔹 Choisissez une option (1 à 7) : "))
    except ValueError:
        print("❌ Entrée invalide, veuillez entrer un nombre.")
        connect_db(modif)
        return

    try:
        with open("data.json", "r", encoding="utf-8") as fichier:
            db_infos = json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠️ Le fichier de configuration est introuvable ou corrompu. Création d'un nouveau fichier...")
        connect_db()
        return

    if "host" not in db_infos and option != 7:
        connect_db()
        return

    match option:
        case 1:
            db_infos["host"] = input("🔹 Nouveau host du serveur PostgreSQL : ")
        case 2:
            db_infos["database"] = input("🔹 Nouveau nom db PostgreSQL : ")
        case 3:
            db_infos["user"] = input("🔹 Nouveau nom d'utilisateur PostgreSQL : ")
        case 4:
            db_infos["password"] = input("🔹 Nouveau mot de passe PostgreSQL : ")
        case 5:
            db_infos["port"] = input("🔹 Nouveau port PostgreSQL : ")
        case 6:
            connect_db()
            return
        case 7:
            menu()
            return
        case _:
            print("❌ Option non valide")
            connect_db(modif)
            return

    with open("data.json", "w", encoding="utf-8") as fichier:
        json.dump(db_infos, fichier, indent=4, ensure_ascii=False)
    print("✅ Infos modifiées")
    menu()
        
def config() :
    print('''
---------  🔧CONFIGURATION   ---------
1️⃣ Changer les identifients de la bdd
2️⃣ Changer le repository
3️⃣ Retour au menu
          ''')
    optionBrut = input("🔹 Choisissez une option (1, 2 ou 3) : ")
    option = int(optionBrut)
    
    if option == 1 :
        connect_db(True)
    elif option == 2 :
        dev()
    elif option == 3 :
        menu()
    else : 
        print("❌ Option non valide")

def start() :
    print(f'''
            ████████╗██╗██████╗░
            ╚══██╔══╝██║██╔══██╗
            ░░░██║░░░██║██████╦╝
            ░░░██║░░░██║██╔══██╗
            ░░░██║░░░██║██████╦╝
            ░░░╚═╝░░░╚═╝╚═════╝░
        Transfer, Integrate, Backup

===============================================
=  Version : {Infos_dev["Version"]}                            =
=  Créateur : TML (Timéo Menvielle Larrouy)   =
=  Contributeurs : {Infos_dev["Contributeurs"]}                          =
=  Mise à jour : {Infos_dev["maj"]}                     =
===============================================


''')
    menu()
start()