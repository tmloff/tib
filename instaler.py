import os
import sys
import shutil
import subprocess
import time

def check_python():
    print("🔍 Vérification de Python...")
    try:
        subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ Python est installé.")
    except subprocess.CalledProcessError:
        print("❌ Python n'est pas installé. Installez-le avant de continuer.")
        sys.exit(1)

def check_git():
    print("🔍 Vérification de Git...")
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ Git est installé.")
    except subprocess.CalledProcessError:
        print("❌ Git n'est pas installé. Installez-le avant de continuer.")
        sys.exit(1)

def find_postgresql():
    possible_paths = [
        "C:\\Program Files\\PostgreSQL\\15\\bin",
        "C:\\Program Files\\PostgreSQL\\14\\bin",
        "C:\\Program Files\\PostgreSQL\\13\\bin"
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def check_postgresql():
    print("🔍 Vérification de PostgreSQL...")
    try:
        subprocess.run(["pg_dump", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ PostgreSQL est installé et accessible.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️ PostgreSQL n'est pas accessible. Tentative de correction...")
        pg_path = find_postgresql()
        if pg_path:
            print(f"🔧 PostgreSQL trouvé à {pg_path}, ajout au PATH...")
            os.environ["PATH"] += os.pathsep + pg_path
            subprocess.run(f'setx PATH "%PATH%;{pg_path}"', shell=True)
            print("♻️ Redémarrage de la vérification de PostgreSQL...")
            time.sleep(2)
            check_postgresql()
        else:
            print("❌ PostgreSQL n'est pas trouvé. Ajoutez-le au PATH ou installez-le.")
            sys.exit(1)

def install_bddtransfer():
    install_dir = "C:\\Outils\\bddtransfer"
    exe_path = os.path.join(install_dir, "bddtransfer.py")
    
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)
    
    print("📂 Installation de bddtransfer dans", install_dir)
    
    script_content = """(CONTENU DU SCRIPT PRINCIPAL ICI)"""
    with open(exe_path, "w", encoding="utf-8") as f:
        f.write(script_content)
    
    print("✅ Script installé !")

def add_to_path():
    print("🔧 Ajout de bddtransfer à PATH...")
    install_dir = "C:\\Outils\\bddtransfer"
    
    subprocess.run(f'setx PATH "%PATH%;{install_dir}"', shell=True)
    print("✅ Ajouté à PATH. Vous pouvez exécuter 'bddtransfer' depuis le terminal.")

def main():
    print("🚀 Installation de BDDTransfer...")
    check_python()
    check_git()
    check_postgresql()
    install_bddtransfer()
    add_to_path()
    print("🎉 Installation terminée ! Vous pouvez utiliser 'bddtransfer'.")

if __name__ == "__main__":
    main()