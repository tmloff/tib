# Imports
import json

def create_backup() :
    print('''
------- 📌CONNEXION DB -------''')
    connect_db = {
        "host": input("🔹 Host du serveur PostgreSQL : "),
        "database": input("🔹 Nom db PostgreSQL : "),
        "user": input("🔹 Nom d'utilisateur PostgreSQL : "),
        "password": input("🔹 Mot de passe PostgreSQL : "),
    }

    print("🔄 Création du backup...")
    

def start() :
    print('''
   ████████╗██╗██████╗░
   ╚══██╔══╝██║██╔══██╗
   ░░░██║░░░██║██████╦╝
   ░░░██║░░░██║██╔══██╗
   ░░░██║░░░██║██████╦╝
   ░░░╚═╝░░░╚═╝╚═════╝░
Transfer, Integrate, Backup

---------  📌MENU   ---------        
1️⃣ Créer un backup
2️⃣ Restaurer un backup
3️⃣ Pousser le backup sur GitHub''')
    option = input("🔹 Choisissez une option (1, 2 ou 3) : ")
    
    if option == "1":
        create_backup()
    elif option == "2":
        restore_backup()
    elif option == "3":
        push_backup()
    else :
        print("❌ Option non valide")
start()