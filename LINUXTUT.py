#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗████████╗██╗   ██╗████████╗         ║
║   ██║     ██║████╗  ██║██║   ██║██║ ██╔╝╚══██╔══╝██║   ██║╚══██╔══╝         ║
║   ██║     ██║██╔██╗ ██║██║   ██║█████╔╝    ██║   ██║   ██║   ██║            ║
║   ██║     ██║██║╚██╗██║██║   ██║██╔═██╗    ██║   ██║   ██║   ██║            ║
║   ███████╗██║██║ ╚████║╚██████╔╝██║  ██╗   ██║   ╚██████╔╝   ██║            ║
║   ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝    ╚═╝            ║
║                                                                              ║
║         📚 TUTORIEL COMPLET DES COMMANDES LINUX - INTERACTIF 📚              ║
║              Apprenez Linux avec des visuels, exemples et quiz               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import subprocess
import textwrap
from datetime import datetime

# ══ COULEURS ANSI ══════════════════════════════════════════════════════════════
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

# ══ FONCTIONS UTILITAIRES ═════════════════════════════════════════════════════
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def pause():
    input(f"\n{C.DIM}Appuyez sur Entrée pour continuer...{C.RESET}")

def print_banner():
    banner = f"""
{C.BRIGHT_CYAN}    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗████████╗██╗   ██╗████████╗
    ██║     ██║████╗  ██║██║   ██║██║ ██╔╝╚══██╔══╝██║   ██║╚══██╔══╝
    ██║     ██║██╔██╗ ██║██║   ██║█████╔╝    ██║   ██║   ██║   ██║   
    ██║     ██║██║╚██╗██║██║   ██║██╔═██╗    ██║   ██║   ██║   ██║   
    ███████╗██║██║ ╚████║╚██████╔╝██║  ██╗   ██║   ╚██████╔╝   ██║   
    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝    ╚═╝   {C.RESET}
{C.BRIGHT_YELLOW}         📚 TUTORIEL COMPLET DES COMMANDES LINUX - INTERACTIF 📚{C.RESET}
{C.DIM}              Apprenez Linux avec des visuels, exemples et quiz{C.RESET}
    """
    print(banner)

def loading(text, duration=1.5):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    start = time.time()
    i = 0
    while time.time() - start < duration:
        print(f"\r{C.BRIGHT_CYAN}{chars[i % len(chars)]}{C.RESET} {text}...", end='', flush=True)
        time.sleep(0.1)
        i += 1
    print(f"\r{C.BRIGHT_GREEN}✓{C.RESET} {text} terminé!{' ' * 20}")

def box(title, content, color=C.BRIGHT_CYAN):
    lines = content.split('\n')
    width = max(len(line) for line in lines) + 4
    print(f"\n{color}╔{'═' * width}╗{C.RESET}")
    print(f"{color}║{C.RESET} {C.BOLD}{title}{C.RESET}{' ' * (width - len(title) - 1)}{color}║{C.RESET}")
    print(f"{color}╠{'═' * width}╣{C.RESET}")
    for line in lines:
        print(f"{color}║{C.RESET}  {line}{' ' * (width - len(line) - 3)}{color}║{C.RESET}")
    print(f"{color}╚{'═' * width}╝{C.RESET}")

# ══ BASE DE DONNÉES DES COMMANDES ═════════════════════════════════════════════
COMMANDS = {
    # === NAVIGATION ===
    "ls": {
        "category": "Navigation",
        "description": "Liste le contenu d'un répertoire",
        "syntaxe": "ls [OPTIONS] [CHEMIN]",
        "options": {
            "-l": "Format long (permissions, propriétaire, taille, date)",
            "-a": "Affiche les fichiers cachés (commençant par .)",
            "-h": "Tailles lisibles (K, M, G)",
            "-R": "Récursif (sous-répertoires)",
            "-t": "Trie par date de modification",
            "-S": "Trie par taille (décroissant)",
            "-r": "Ordre inverse",
            "--color": "Colorise la sortie",
        },
        "exemples": [
            ("ls", "Liste simple du répertoire courant"),
            ("ls -la", "Liste détaillée avec fichiers cachés"),
            ("ls -lh /var/log", "Liste détaillée avec tailles lisibles"),
            ("ls -lt", "Trie par date, plus récent en premier"),
            ("ls -R /home", "Liste récursive de /home"),
        ],
        "cas_usage": [
            "Voir les fichiers dans un dossier",
            "Vérifier les permissions d'un fichier",
            "Trouver le plus récent fichier modifié",
            "Voir la taille des fichiers",
        ],
        "visual": """
    📁 /home/user/
    ├── 📄 document.txt    (rwxr-xr-x  user  2.4K)
    ├── 📁 projets/        (drwxr-xr-x  user  4.0K)
    ├── 🔒 .bashrc         (rw-r--r--  user  3.1K)  ← caché (-a)
    └── 📄 notes.md        (rw-r--r--  user  1.2K)
        """,
    },
    "cd": {
        "category": "Navigation",
        "description": "Change de répertoire courant",
        "syntaxe": "cd [CHEMIN]",
        "options": {},
        "exemples": [
            ("cd /home/user", "Va dans /home/user"),
            ("cd ..", "Remonte d'un niveau"),
            ("cd ~", "Va dans le répertoire personnel"),
            ("cd -", "Retourne au répertoire précédent"),
            ("cd /var/log && ls", "Va dans /var/log et liste"),
        ],
        "cas_usage": [
            "Se déplacer dans l'arborescence",
            "Retourner rapidement à son home",
            "Naviguer entre deux répertoires",
        ],
        "visual": """
    🏠 ~ (home)
       │
       ├── cd Documents
       ▼
    📁 ~/Documents
       │
       ├── cd ..
       ▼
    🏠 ~ (retour)
        """,
    },
    "pwd": {
        "category": "Navigation",
        "description": "Affiche le répertoire courant (Print Working Directory)",
        "syntaxe": "pwd",
        "options": {
            "-L": "Affiche le chemin logique (avec liens symboliques)",
            "-P": "Affiche le chemin physique (résout les liens)",
        },
        "exemples": [
            ("pwd", "/home/user/projets/linux"),
            ("pwd -P", "/home/user/projets/linux (chemin réel)"),
        ],
        "cas_usage": [
            "Savoir où on est dans l'arborescence",
            "Vérifier le chemin absolu",
            "Dans les scripts pour obtenir le répertoire",
        ],
        "visual": """
    ┌─────────────────────────────┐
    │  $ pwd                      │
    │  /home/user/projets/linux   │
    │       ↑                     │
    │   Vous êtes ici !           │
    └─────────────────────────────┘
        """,
    },
    "mkdir": {
        "category": "Navigation",
        "description": "Crée un répertoire",
        "syntaxe": "mkdir [OPTIONS] NOM",
        "options": {
            "-p": "Crée les répertoires parents si nécessaire",
            "-v": "Mode verbeux (affiche ce qui est créé)",
            "-m": "Définit les permissions (ex: -m 755)",
        },
        "exemples": [
            ("mkdir mon_dossier", "Crée un dossier simple"),
            ("mkdir -p projet/src/tests", "Crée toute l'arborescence"),
            ("mkdir -m 700 privé", "Crée avec permissions restrictives"),
        ],
        "cas_usage": [
            "Créer la structure d'un nouveau projet",
            "Créer des dossiers imbriqués en une commande",
            "Créer des dossiers avec permissions spécifiques",
        ],
        "visual": """
    Avant:              Après mkdir -p projet/src:
    📁 /home/user       📁 /home/user
                          └── 📁 projet/
                              └── 📁 src/
        """,
    },
    "rm": {
        "category": "Navigation",
        "description": "Supprime des fichiers ou répertoires",
        "syntaxe": "rm [OPTIONS] FICHIER...",
        "options": {
            "-r": "Récursif (pour les répertoires)",
            "-f": "Force (sans confirmation)",
            "-i": "Interactif (demande confirmation)",
            "-v": "Verbeux",
        },
        "exemples": [
            ("rm fichier.txt", "Supprime un fichier"),
            ("rm -r dossier/", "Supprime un répertoire et son contenu"),
            ("rm -rf /tmp/*", "Force suppression de tout dans /tmp"),
            ("rm -i *.log", "Demande confirmation pour chaque .log"),
        ],
        "cas_usage": [
            "Nettoyer des fichiers temporaires",
            "Supprimer un projet entier",
            "⚠️ ATTENTION: rm -rf / détruit tout le système !",
        ],
        "visual": """
    ⚠️  ZONE DANGEREUSE  ⚠️
    
    rm -rf /          ← ❌ NEVER DO THIS
    rm -rf /*         ← ❌ NEVER DO THIS
    
    Sécurité: alias rm='rm -i' dans .bashrc
        """,
    },
    "cp": {
        "category": "Navigation",
        "description": "Copie des fichiers ou répertoires",
        "syntaxe": "cp [OPTIONS] SOURCE DESTINATION",
        "options": {
            "-r": "Récursif (pour les répertoires)",
            "-v": "Verbeux",
            "-i": "Interactif (écrasement)",
            "-p": "Préserve les attributs (date, permissions)",
            "-u": "Copie seulement si source plus récente",
        },
        "exemples": [
            ("cp fichier.txt backup/", "Copie dans le dossier backup"),
            ("cp -r projet/ projet_backup/", "Copie récursive d'un projet"),
            ("cp -pv *.conf /etc/", "Copie avec préservation verbeuse"),
        ],
        "cas_usage": [
            "Faire une sauvegarde de fichiers",
            "Dupliquer un projet",
            "Sauvegarder des fichiers de configuration",
        ],
        "visual": """
    cp fichier.txt backup/
    
    📁 /home/user
    ├── 📄 fichier.txt  ──────►  📁 backup/
    │                              └── 📄 fichier.txt
    └── 📁 backup/
        """,
    },
    "mv": {
        "category": "Navigation",
        "description": "Déplace ou renomme des fichiers/répertoires",
        "syntaxe": "mv [OPTIONS] SOURCE DESTINATION",
        "options": {
            "-i": "Interactif",
            "-v": "Verbeux",
            "-n": "Ne pas écraser",
            "-u": "Écraser seulement si plus récent",
        },
        "exemples": [
            ("mv ancien.txt nouveau.txt", "Renomme un fichier"),
            ("mv fichier.txt /tmp/", "Déplace vers /tmp"),
            ("mv *.txt documents/", "Déplace tous les .txt"),
        ],
        "cas_usage": [
            "Renommer des fichiers",
            "Organiser des fichiers dans des dossiers",
            "Déplacer des logs vers un autre disque",
        ],
        "visual": """
    mv ancien.txt nouveau.txt
    
    Avant:              Après:
    📄 ancien.txt   →   📄 nouveau.txt
        """,
    },
    "touch": {
        "category": "Navigation",
        "description": "Crée un fichier vide ou met à jour la date",
        "syntaxe": "touch [OPTIONS] FICHIER...",
        "options": {
            "-a": "Change seulement la date d'accès",
            "-m": "Change seulement la date de modification",
            "-t": "Date spécifique (YYYYMMDDhhmm.ss)",
            "-c": "Ne crée pas le fichier s'il n'existe pas",
        },
        "exemples": [
            ("touch nouveau.txt", "Crée un fichier vide"),
            ("touch -t 202401011200 fichier.txt", "Date fixée au 1er janvier 2024"),
            ("touch *.txt", "Met à jour la date de tous les .txt"),
        ],
        "cas_usage": [
            "Créer rapidement un fichier vide",
            "Forcer la recompilation (make)",
            "Changer la date d'un fichier",
        ],
        "visual": """
    touch fichier.txt
    
    Avant:              Après:
    (rien)         →   📄 fichier.txt
                       (taille: 0 octets)
        """,
    },

    # === AFFICHAGE FICHIERS ===
    "cat": {
        "category": "Fichiers",
        "description": "Affiche le contenu d'un fichier",
        "syntaxe": "cat [OPTIONS] FICHIER...",
        "options": {
            "-n": "Numérote les lignes",
            "-b": "Numérote les lignes non vides",
            "-E": "Affiche $ à la fin de chaque ligne",
            "-T": "Affiche les tabulations comme ^I",
            "-s": "Supprime les lignes vides multiples",
        },
        "exemples": [
            ("cat fichier.txt", "Affiche le contenu"),
            ("cat -n script.py", "Affiche avec numéros de ligne"),
            ("cat file1 file2 > combined", "Concatène dans un nouveau fichier"),
        ],
        "cas_usage": [
            "Lire rapidement un fichier",
            "Concaténer des fichiers",
            "Voir le contenu d'un fichier de config",
        ],
        "visual": """
    $ cat -n hello.py
         1  #!/usr/bin/env python3
         2  print("Hello World!")
         3  
         4  def main():
         5      return 0
        """,
    },
    "less": {
        "category": "Fichiers",
        "description": "Affiche un fichier page par page (navigable)",
        "syntaxe": "less [OPTIONS] FICHIER",
        "options": {
            "-N": "Affiche les numéros de ligne",
            "-S": "Coupe les lignes longues (pas de wrap)",
            "+F": "Suivi en temps réel (comme tail -f)",
            "-i": "Recherche insensible à la casse",
        },
        "exemples": [
            ("less /var/log/syslog", "Voir les logs système"),
            ("less +F /var/log/apache2/access.log", "Suivre les logs en direct"),
        ],
        "cas_usage": [
            "Lire de gros fichiers (logs)",
            "Naviguer dans un fichier avec recherche",
            "Suivre un fichier en temps réel",
        ],
        "visual": """
    ┌─────────────────────────────┐
    │ ligne 1                     │
    │ ligne 2                     │
    │ ...                         │
    │ ──── (espace) page suivante │
    │ q pour quitter              │
    │ /motif pour chercher        │
    └─────────────────────────────┘
        """,
    },
    "head": {
        "category": "Fichiers",
        "description": "Affiche les premières lignes d'un fichier",
        "syntaxe": "head [OPTIONS] FICHIER",
        "options": {
            "-n N": "Affiche N lignes (défaut: 10)",
            "-c N": "Affiche N octets",
            "-q": "Pas d'en-tête de fichier",
        },
        "exemples": [
            ("head fichier.txt", "10 premières lignes"),
            ("head -n 5 fichier.txt", "5 premières lignes"),
            ("head -n 1 *.csv", "Première ligne de chaque CSV"),
        ],
        "cas_usage": [
            "Voir l'en-tête d'un fichier CSV",
            "Vérifier le début d'un log",
            "Extraire la première ligne",
        ],
        "visual": """
    head -n 3 fichier.txt
    
    ┌─────────────┐
    │ ligne 1     │ ←
    │ ligne 2     │ ←  affiché
    │ ligne 3     │ ←
    │ ligne 4     │
    │ ...         │  (caché)
    └─────────────┘
        """,
    },
    "tail": {
        "category": "Fichiers",
        "description": "Affiche les dernières lignes d'un fichier",
        "syntaxe": "tail [OPTIONS] FICHIER",
        "options": {
            "-n N": "Affiche N lignes (défaut: 10)",
            "-f": "Suivi en temps réel (follow)",
            "-F": "Suivi avec réouverture si fichier recréé",
        },
        "exemples": [
            ("tail /var/log/syslog", "10 dernières lignes"),
            ("tail -f /var/log/apache2/access.log", "Suivre les logs en direct"),
            ("tail -n 20 fichier.txt", "20 dernières lignes"),
        ],
        "cas_usage": [
            "Surveiller des logs en temps réel",
            "Voir les dernières erreurs",
            "Suivre l'activité d'un serveur",
        ],
        "visual": """
    tail -f /var/log/syslog
    
    ... (lignes précédentes)
    │ Jan 15 10:30:01 serveur CRON[1234]: ... │ ←
    │ Jan 15 10:30:05 serveur sshd[5678]: ... │ ←  dernières lignes
    │ Jan 15 10:30:12 serveur nginx[9012]: .. │ ←
    └─────────────────────────────────────────┘
    ⏳ En attente de nouvelles lignes...
        """,
    },
    "grep": {
        "category": "Fichiers",
        "description": "Recherche de texte dans des fichiers (Global Regular Expression Print)",
        "syntaxe": "grep [OPTIONS] MOTIF [FICHIER...]",
        "options": {
            "-i": "Insensible à la casse",
            "-v": "Inverse (lignes qui ne correspondent PAS)",
            "-n": "Numéros de ligne",
            "-r": "Récursif (dans les sous-répertoires)",
            "-l": "Affiche seulement les noms de fichiers",
            "-c": "Compte les occurrences",
            "-E": "Expressions régulières étendues",
            "-w": "Mot entier uniquement",
            "--color": "Colorise les correspondances",
        },
        "exemples": [
            ("grep 'erreur' log.txt", "Cherche 'erreur' dans log.txt"),
            ("grep -ri 'TODO' projet/", "Cherche TODO dans tout le projet"),
            ("grep -n 'def ' *.py", "Trouve les définitions de fonctions"),
            ("ps aux | grep python", "Filtre les processus python"),
        ],
        "cas_usage": [
            "Trouver une erreur dans les logs",
            "Chercher du code dans un projet",
            "Filtrer la sortie d'une commande",
            "Compter les occurrences",
        ],
        "visual": """
    $ grep -n 'erreur' log.txt
    15:2024-01-15 erreur: connexion échouée
    42:2024-01-15 erreur: timeout
         ↑                    ↑
      numéro              correspondance
      de ligne            en rouge
        """,
    },
    "find": {
        "category": "Fichiers",
        "description": "Recherche de fichiers dans une arborescence",
        "syntaxe": "find [CHEMIN] [EXPRESSION]",
        "options": {
            "-name": "Recherche par nom (sensible à la casse)",
            "-iname": "Recherche par nom (insensible)",
            "-type": "Type: f=fichier, d=répertoire, l=lien",
            "-size": "Taille: +10M, -1k, 500c",
            "-mtime": "Modifié il y a N jours (-1 = aujourd'hui)",
            "-exec": "Exécute une commande sur chaque résultat",
            "-delete": "Supprime les fichiers trouvés",
        },
        "exemples": [
            ("find . -name '*.py'", "Trouve tous les fichiers .py"),
            ("find /var/log -mtime +7", "Logs modifiés il y a +7 jours"),
            ("find . -type f -size +100M", "Fichiers de plus de 100Mo"),
            ("find . -name '*.tmp' -delete", "Supprime tous les .tmp"),
            ("find . -name '*.log' -exec gzip {} \\;", "Compresse tous les .log"),
        ],
        "cas_usage": [
            "Trouver des fichiers par nom",
            "Nettoyer les vieux logs",
            "Trouver les gros fichiers",
            "Exécuter une action sur plusieurs fichiers",
        ],
        "visual": """
    find /home -name '*.jpg'
    
    📁 /home
    ├── 📁 user1
    │   └── 📄 photo.jpg     ← trouvé!
    ├── 📁 user2
    │   └── 📄 image.jpg     ← trouvé!
    └── 📁 user3
        └── 📄 doc.pdf       (pas trouvé)
        """,
    },

    # === SYSTÈME ===
    "ps": {
        "category": "Système",
        "description": "Affiche les processus en cours",
        "syntaxe": "ps [OPTIONS]",
        "options": {
            "aux": "Tous les processus de tous les utilisateurs (BSD)",
            "-ef": "Format complet (System V)",
            "-u user": "Processus d'un utilisateur",
            "--sort": "Trie (ex: --sort=-%mem)",
        },
        "exemples": [
            ("ps aux", "Tous les processus (format BSD)"),
            ("ps -ef | grep nginx", "Cherche les processus nginx"),
            ("ps aux --sort=-%mem | head", "10 processus les plus gourmands"),
        ],
        "cas_usage": [
            "Voir quels programmes tournent",
            "Trouver le PID d'un processus",
            "Identifier les processus gourmands",
        ],
        "visual": """
    $ ps aux
    USER   PID  %CPU %MEM  COMMAND
    root     1   0.0  0.1  systemd
    root   500   0.1  1.2  nginx
    user  1234   5.0 10.5  firefox
           ↑           ↑
          PID      mémoire utilisée
        """,
    },
    "top": {
        "category": "Système",
        "description": "Affiche les processus en temps réel (tableau interactif)",
        "syntaxe": "top",
        "options": {
            "-u user": "Processus d'un utilisateur",
            "-p PID": "Surveille un PID spécifique",
            "-d N": "Rafraîchissement toutes les N secondes",
        },
        "exemples": [
            ("top", "Vue temps réel interactive"),
            ("top -u www-data", "Processus de l'utilisateur www-data"),
        ],
        "cas_usage": [
            "Surveiller l'utilisation CPU/RAM",
            "Identifier un processus qui ralentit le système",
            "Tuer un processus (k dans top)",
        ],
        "visual": """
    ┌─────────────────────────────────────┐
    │  PID USER  %CPU %MEM  COMMAND       │
    │ 1234 root   45%  20%  backup.sh     │ ← utilise beaucoup de CPU
    │ 5678 www    2%   5%   nginx         │
    │ ...                                 │
    │                                     │
    │  k → tuer un processus              │
    │  q → quitter                        │
    │  M → trier par mémoire              │
    └─────────────────────────────────────┘
        """,
    },
    "kill": {
        "category": "Système",
        "description": "Envoie un signal à un processus",
        "syntaxe": "kill [OPTIONS] PID",
        "options": {
            "-9": "SIGKILL (force, ne peut pas être ignoré)",
            "-15": "SIGTERM (demande polie de terminer, défaut)",
            "-1": "SIGHUP (recharge la configuration)",
            "-l": "Liste tous les signaux",
        },
        "exemples": [
            ("kill 1234", "Demande au PID 1234 de terminer"),
            ("kill -9 1234", "Tue immédiatement le processus"),
            ("killall firefox", "Tue tous les processus firefox"),
            ("pkill -f 'python app.py'", "Tue par nom de commande"),
        ],
        "cas_usage": [
            "Arrêter un programme bloqué",
            "Redémarrer un service (SIGHUP)",
            "Forcer la fermeture d'une application",
        ],
        "visual": """
    Processus 1234 (firefox)
           │
    kill 1234     → SIGTERM ──► 🛑 (fermeture propre)
    kill -9 1234  → SIGKILL ──► 💀 (destruction forcée)
    kill -1 1234  → SIGHUP  ──► 🔄 (recharge config)
        """,
    },
    "df": {
        "category": "Système",
        "description": "Affiche l'espace disque utilisé (Disk Free)",
        "syntaxe": "df [OPTIONS] [FICHIER...]",
        "options": {
            "-h": "Tailles lisibles (K, M, G, T)",
            "-T": "Affiche le type de système de fichiers",
            "-i": "Affiche les inodes",
        },
        "exemples": [
            ("df -h", "Espace disque lisible"),
            ("df -h /home", "Espace pour /home uniquement"),
            ("df -Th", "Avec types de filesystem"),
        ],
        "cas_usage": [
            "Vérifier l'espace disque disponible",
            "Identifier une partition pleine",
            "Voir le type de filesystem",
        ],
        "visual": """
    $ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda1        50G   35G   12G  75% /
    /dev/sdb1       500G  100G  400G  20% /data
                              ↑
                        ⚠️ attention si >90%
        """,
    },
    "du": {
        "category": "Système",
        "description": "Affiche l'espace utilisé par fichiers/répertoires (Disk Usage)",
        "syntaxe": "du [OPTIONS] [FICHIER...]",
        "options": {
            "-h": "Tailles lisibles",
            "-s": "Résumé (total seulement)",
            "-a": "Tous les fichiers (pas seulement répertoires)",
            "--max-depth=N": "Limite la profondeur",
            "-c": "Affiche un total cumulé",
        },
        "exemples": [
            ("du -sh /var/log", "Taille totale de /var/log"),
            ("du -h --max-depth=1 /home", "Taille par utilisateur"),
            ("du -ah | sort -rh | head -20", "20 plus gros fichiers"),
        ],
        "cas_usage": [
            "Trouver quoi prend de la place",
            "Identifier les gros dossiers",
            "Nettoyer l'espace disque",
        ],
        "visual": """
    $ du -sh /var/*
    50M  /var/cache
    2G   /var/log      ← ⚠️ gros consommateur
    100M /var/mail
    5M   /var/tmp
        """,
    },
    "free": {
        "category": "Système",
        "description": "Affiche l'utilisation de la mémoire",
        "syntaxe": "free [OPTIONS]",
        "options": {
            "-h": "Tailles lisibles",
            "-m": "En mégaoctets",
            "-g": "En gigaoctets",
            "-s N": "Rafraîchit toutes les N secondes",
        },
        "exemples": [
            ("free -h", "Mémoire en format lisible"),
            ("free -ms 2", "Actualise toutes les 2 secondes"),
        ],
        "cas_usage": [
            "Vérifier la RAM disponible",
            "Identifier une fuite mémoire",
            "Surveiller l'utilisation SWAP",
        ],
        "visual": """
    $ free -h
                  total   used   free  shared  buff/cache  available
    Mem:           16G    8G     2G    500M       6G         7G
                  ↑       ↑      ↑
                total   utilisé  libre
    
    💡 available = vraiment disponible pour les apps
        """,
    },
    "uptime": {
        "category": "Système",
        "description": "Affiche depuis combien de temps le système tourne",
        "syntaxe": "uptime",
        "options": {},
        "exemples": [
            ("uptime", "Temps d'activité + charge"),
        ],
        "cas_usage": [
            "Vérifier quand le serveur a redémarré",
            "Voir la charge système",
            "Diagnostic de stabilité",
        ],
        "visual": """
    $ uptime
     14:30:00 up 45 days, 3:25, 2 users, load average: 0.52, 0.58, 0.59
              ↑           ↑                          ↑
           heure      depuis 45 jours             charge (1, 5, 15 min)
        """,
    },

    # === RÉSEAU ===
    "ip": {
        "category": "Réseau",
        "description": "Gestion des interfaces réseau (remplace ifconfig)",
        "syntaxe": "ip [OPTIONS] OBJECT COMMAND",
        "options": {
            "addr": "Adresses IP",
            "link": "Interfaces réseau",
            "route": "Table de routage",
            "neigh": "Voisins (ARP)",
        },
        "exemples": [
            ("ip addr", "Affiche les IPs de toutes les interfaces"),
            ("ip addr show eth0", "IP de eth0 uniquement"),
            ("ip link set eth0 up", "Active l'interface eth0"),
            ("ip route", "Affiche la table de routage"),
            ("ip neigh", "Table ARP"),
        ],
        "cas_usage": [
            "Voir son adresse IP",
            "Activer/désactiver une interface",
            "Voir la passerelle par défaut",
            "Voir les voisins du réseau",
        ],
        "visual": """
    $ ip addr
    1: lo: <LOOPBACK> ...
        inet 127.0.0.1/8
    2: eth0: <UP> ...
        inet 192.168.1.10/24    ← votre IP locale
           ↑
        interface
        """,
    },
    "ping": {
        "category": "Réseau",
        "description": "Teste la connectivité réseau",
        "syntaxe": "ping [OPTIONS] HÔTE",
        "options": {
            "-c N": "Envoie N paquets puis s'arrête",
            "-i N": "Intervalle de N secondes",
            "-s N": "Taille du paquet en octets",
            "-t": "Définit le TTL",
        },
        "exemples": [
            ("ping google.com", "Teste la connexion à Google"),
            ("ping -c 4 8.8.8.8", "4 paquets vers DNS Google"),
            ("ping -i 0.2 192.168.1.1", "Ping rapide (5/sec)"),
        ],
        "cas_usage": [
            "Vérifier sa connexion Internet",
            "Tester la latence",
            "Diagnostiquer un problème réseau",
        ],
        "visual": """
    $ ping -c 3 google.com
    PING google.com (142.250.80.46)
    64 bytes from ...: icmp_seq=1 ttl=117 time=15.2 ms  ← ✅
    64 bytes from ...: icmp_seq=2 ttl=117 time=14.8 ms  ← ✅
    64 bytes from ...: icmp_seq=3 ttl=117 time=15.5 ms  ← ✅
    
    --- google.com ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss
        """,
    },
    "curl": {
        "category": "Réseau",
        "description": "Transfère des données depuis/vers un serveur",
        "syntaxe": "curl [OPTIONS] URL",
        "options": {
            "-I": "En-têtes HTTP seulement",
            "-L": "Suit les redirections",
            "-o fichier": "Sauvegarde dans un fichier",
            "-O": "Sauvegarde avec le nom original",
            "-X METHOD": "Méthode HTTP (GET, POST, PUT, DELETE)",
            "-d 'data'": "Données POST",
            "-H 'Header'": "En-tête personnalisé",
            "-v": "Mode verbeux",
        },
        "exemples": [
            ("curl https://api.example.com", "Requête GET simple"),
            ("curl -I https://google.com", "Voir les en-têtes"),
            ("curl -o fichier.zip https://site.com/fichier.zip", "Télécharger"),
            ("curl -X POST -d 'name=test' https://api.com/users", "Requête POST"),
        ],
        "cas_usage": [
            "Tester une API",
            "Télécharger un fichier",
            "Vérifier les en-têtes HTTP",
            "Automatiser des requêtes web",
        ],
        "visual": """
    curl https://api.example.com/users
    
    Vous ──HTTP GET──► Serveur
      ◄──JSON 200────┘
    
    [{"id":1,"name":"Alice"},{"id":2,"name":"Bob"}]
        """,
    },
    "wget": {
        "category": "Réseau",
        "description": "Télécharge des fichiers depuis le web",
        "syntaxe": "wget [OPTIONS] URL",
        "options": {
            "-O fichier": "Nom de sortie personnalisé",
            "-P répertoire": "Télécharge dans un répertoire",
            "-c": "Reprend un téléchargement interrompu",
            "-b": "Arrière-plan",
            "--limit-rate=200k": "Limite la vitesse",
        },
        "exemples": [
            ("wget https://example.com/fichier.zip", "Télécharge un fichier"),
            ("wget -c https://example.com/gros-fichier.iso", "Reprend un téléchargement"),
            ("wget -P ~/Downloads https://site.com/file", "Télécharge dans Downloads"),
        ],
        "cas_usage": [
            "Télécharger des fichiers en ligne de commande",
            "Reprendre un téléchargement coupé",
            "Télécharger un site entier (mirror)",
        ],
        "visual": """
    wget https://example.com/fichier.zip
    
    --2024-01-15 10:30:00--  https://example.com/fichier.zip
    Résolution de example.com... 93.184.216.34
    Connexion vers example.com|93.184.216.34|:443... connecté.
    Taille: 50M
    Sauvegarde en: «fichier.zip»
    
    fichier.zip     100%[====>]  50.00M  10MB/s   in 5.0s
        """,
    },
    "ssh": {
        "category": "Réseau",
        "description": "Connexion sécurisée à distance (Secure Shell)",
        "syntaxe": "ssh [OPTIONS] [user@]hôte",
        "options": {
            "-p PORT": "Port personnalisé (défaut: 22)",
            "-i clé": "Clé privée SSH",
            "-X": "Transfert X11 (graphique)",
            "-L": "Tunnel local",
            "-N": "Pas de commande (tunnel uniquement)",
        },
        "exemples": [
            ("ssh user@serveur.com", "Connexion classique"),
            ("ssh -p 2222 user@serveur.com", "Port personnalisé"),
            ("ssh -i ~/.ssh/id_rsa user@serveur", "Avec clé privée"),
            ("ssh user@serveur 'ls -la'", "Exécute une commande distante"),
        ],
        "cas_usage": [
            "Administrer un serveur distant",
            "Transférer des fichiers (avec scp/sftp)",
            "Créer des tunnels sécurisés",
            "Exécuter des commandes à distance",
        ],
        "visual": """
    ssh user@serveur.com
    
    Votre PC ──SSH (chiffré)──► Serveur distant
       │                           │
       └──────── tunnel ───────────┘
       
    $ ls              ← tapé sur votre PC
    fichier.txt       ← exécuté sur le serveur
        """,
    },
    "scp": {
        "category": "Réseau",
        "description": "Copie sécurisée de fichiers via SSH",
        "syntaxe": "scp [OPTIONS] SOURCE DESTINATION",
        "options": {
            "-r": "Récursif (répertoires)",
            "-P PORT": "Port SSH",
            "-i clé": "Clé privée",
            "-p": "Préserve les attributs",
            "-C": "Compression",
        },
        "exemples": [
            ("scp fichier.txt user@serveur:/tmp/", "Envoie vers le serveur"),
            ("scp user@serveur:/etc/nginx/nginx.conf .", "Récupère depuis le serveur"),
            ("scp -r projet/ user@serveur:/var/www/", "Envoie un répertoire entier"),
        ],
        "cas_usage": [
            "Déployer des fichiers sur un serveur",
            "Sauvegarder des fichiers distants",
            "Transférer entre deux serveurs",
        ],
        "visual": """
    scp fichier.txt user@serveur:/home/user/
    
    📄 fichier.txt  ──SSH sécurisé──►  🖥️ serveur
                                        └── 📄 fichier.txt
        """,
    },
    "netstat": {
        "category": "Réseau",
        "description": "Affiche les connexions réseau, tables de routage, interfaces",
        "syntaxe": "netstat [OPTIONS]",
        "options": {
            "-t": "Connexions TCP",
            "-u": "Connexions UDP",
            "-l": "Ports en écoute",
            "-n": "Numérique (pas de résolution DNS)",
            "-p": "Affiche le PID/programme",
            "-a": "Toutes les connexions",
        },
        "exemples": [
            ("netstat -tlnp", "Ports en écoute avec programmes"),
            ("netstat -an | grep :80", "Connexions sur le port 80"),
            ("netstat -i", "Statistiques des interfaces"),
        ],
        "cas_usage": [
            "Voir quels ports sont ouverts",
            "Identifier quel programme écoute sur un port",
            "Diagnostiquer des problèmes de connexion",
        ],
        "visual": """
    $ netstat -tlnp
    Proto  Local Address   Foreign Address  State    PID/Program
    tcp    0.0.0.0:22      0.0.0.0:*        LISTEN   1234/sshd
    tcp    0.0.0.0:80      0.0.0.0:*        LISTEN   5678/nginx
    tcp    0.0.0.0:443     0.0.0.0:*        LISTEN   5678/nginx
              ↑                              ↑
            port                           programme
        """,
    },

    # === PERMISSIONS ===
    "chmod": {
        "category": "Permissions",
        "description": "Change les permissions d'un fichier",
        "syntaxe": "chmod [OPTIONS] MODE FICHIER...",
        "options": {
            "-R": "Récursif",
            "-v": "Verbeux",
        },
        "exemples": [
            ("chmod 755 script.sh", "rwxr-xr-x (exécutable par tous)"),
            ("chmod 644 fichier.txt", "rw-r--r-- (lecture pour tous)"),
            ("chmod +x script.py", "Ajoute le droit d'exécution"),
            ("chmod -R 700 ~/.ssh", "Permissions strictes sur .ssh"),
        ],
        "cas_usage": [
            "Rendre un script exécutable",
            "Restreindre l'accès à un fichier",
            "Corriger les permissions après un transfert",
        ],
        "visual": """
    chmod 755 script.sh
    
    ┌─────────────────────────────────────────┐
    │  7    5    5                            │
    │ rwx  r-x  r-x                           │
    │  ↓    ↓    ↓                            │
    │ user group other                        │
    │                                         │
    │ 4=r  2=w  1=x  →  7=rwx  5=r-x  0=---  │
    └─────────────────────────────────────────┘
        """,
    },
    "chown": {
        "category": "Permissions",
        "description": "Change le propriétaire d'un fichier",
        "syntaxe": "chown [OPTIONS] [USER][:GROUP] FICHIER...",
        "options": {
            "-R": "Récursif",
            "-v": "Verbeux",
        },
        "exemples": [
            ("chown user fichier.txt", "Change le propriétaire"),
            ("chown user:group fichier.txt", "Change user et groupe"),
            ("chown :group fichier.txt", "Change seulement le groupe"),
            ("chown -R www-data:www-data /var/www", "Pour un serveur web"),
        ],
        "cas_usage": [
            "Corriger le propriétaire après un transfert",
            "Configurer un serveur web",
            "Partager des fichiers entre utilisateurs",
        ],
        "visual": """
    chown alice:developers projet/
    
    Avant:              Après:
    root:root   →   alice:developers
      ↑   ↑            ↑      ↑
    user groupe      user   groupe
        """,
    },
    "sudo": {
        "category": "Permissions",
        "description": "Exécute une commande en tant que super-utilisateur",
        "syntaxe": "sudo [OPTIONS] COMMANDE",
        "options": {
            "-u user": "Exécute en tant qu'utilisateur spécifique",
            "-i": "Simule un login root (shell interactif)",
            "-s": "Shell root",
            "-l": "Liste les commandes autorisées",
        },
        "exemples": [
            ("sudo apt update", "Met à jour les paquets"),
            ("sudo -i", "Ouvre un shell root"),
            ("sudo -u www-data whoami", "Exécute en tant que www-data"),
        ],
        "cas_usage": [
            "Installer des logiciels",
            "Modifier des fichiers système",
            "Gérer les services",
            "Exécuter des commandes en tant qu'autre user",
        ],
        "visual": """
    $ sudo apt update
    [sudo] Mot de passe de user: ********
    
    user ──► sudo ──► root ──► apt update
           ↑
      vérification /etc/sudoers
        """,
    },

    # === ARCHIVAGE ===
    "tar": {
        "category": "Archivage",
        "description": "Archive et compresse des fichiers",
        "syntaxe": "tar [OPTIONS] [FICHIER_ARCHIVE] [FICHIERS...]",
        "options": {
            "-c": "Crée une archive",
            "-x": "Extrait une archive",
            "-t": "Liste le contenu",
            "-v": "Verbeux",
            "-f": "Spécifie le fichier archive",
            "-z": "Compresse avec gzip (.tar.gz)",
            "-j": "Compresse avec bzip2 (.tar.bz2)",
            "-J": "Compresse avec xz (.tar.xz)",
        },
        "exemples": [
            ("tar -czvf backup.tar.gz dossier/", "Crée une archive compressée"),
            ("tar -xzvf backup.tar.gz", "Extrait une archive"),
            ("tar -tzvf backup.tar.gz", "Liste le contenu"),
            ("tar -czvf backup.tar.gz --exclude='*.tmp' dossier/", "Exclut des fichiers"),
        ],
        "cas_usage": [
            "Sauvegarder des données",
            "Transférer plusieurs fichiers",
            "Compresser pour économiser l'espace",
        ],
        "visual": """
    tar -czvf backup.tar.gz projet/
    
    📁 projet/              📦 backup.tar.gz
    ├── 📄 file1.py   ──►   (compressé)
    ├── 📄 file2.py   ──►
    └── 📁 src/       ──►
    
    c=créer  z=gzip  v=verbeux  f=fichier
        """,
    },
    "gzip": {
        "category": "Archivage",
        "description": "Compresse/décompresse des fichiers",
        "syntaxe": "gzip [OPTIONS] FICHIER...",
        "options": {
            "-d": "Décompresse (comme gunzip)",
            "-k": "Garde le fichier original",
            "-v": "Verbeux",
            "-r": "Récursif",
        },
        "exemples": [
            ("gzip fichier.txt", "Compresse en fichier.txt.gz"),
            ("gzip -d fichier.txt.gz", "Décompresse"),
            ("gzip -k fichier.txt", "Compresse en gardant l'original"),
        ],
        "cas_usage": [
            "Compresser des logs",
            "Réduire la taille de fichiers",
            "Décompresser des fichiers .gz",
        ],
        "visual": """
    gzip fichier.txt
    
    📄 fichier.txt (1.2M)  ──►  📦 fichier.txt.gz (400K)
                                      ↑
                                  ~67% de compression
        """,
    },

    # === UTILITAIRES ===
    "echo": {
        "category": "Utilitaires",
        "description": "Affiche du texte",
        "syntaxe": "echo [OPTIONS] [TEXTE...]",
        "options": {
            "-n": "Pas de saut de ligne final",
            "-e": "Interprète les caractères d'échappement",
        },
        "exemples": [
            ("echo 'Hello World'", "Affiche Hello World"),
            ("echo $PATH", "Affiche la variable d'environnement"),
            ("echo 'texte' > fichier.txt", "Écrit dans un fichier"),
            ("echo 'texte' >> fichier.txt", "Ajoute à la fin d'un fichier"),
        ],
        "cas_usage": [
            "Afficher du texte",
            "Écrire dans un fichier",
            "Voir la valeur d'une variable",
            "Dans les scripts pour le debug",
        ],
        "visual": """
    $ echo "Hello $USER"
    Hello alice
    
    $ echo "ligne 1" > file.txt    →  écrase le fichier
    $ echo "ligne 2" >> file.txt   →  ajoute à la fin
        """,
    },
    "cat": {
        "category": "Utilitaires",
        "description": "Concatène et affiche des fichiers",
        "syntaxe": "cat [OPTIONS] [FICHIER...]",
        "options": {
            "-n": "Numérote les lignes",
            "-b": "Numérote les lignes non vides",
        },
        "exemples": [
            ("cat fichier1 fichier2", "Concatène deux fichiers"),
            ("cat > fichier.txt", "Crée un fichier (Ctrl+D pour finir)"),
        ],
        "cas_usage": [
            "Lire un fichier",
            "Combiner des fichiers",
            "Créer un fichier rapidement",
        ],
        "visual": "",
    },
    "wc": {
        "category": "Utilitaires",
        "description": "Compte les lignes, mots et octets",
        "syntaxe": "wc [OPTIONS] [FICHIER...]",
        "options": {
            "-l": "Lignes uniquement",
            "-w": "Mots uniquement",
            "-c": "Octets uniquement",
            "-m": "Caractères",
        },
        "exemples": [
            ("wc fichier.txt", "Lignes, mots, octets"),
            ("wc -l *.py", "Nombre de lignes par fichier Python"),
            ("cat fichier | wc -l", "Nombre de lignes via pipe"),
        ],
        "cas_usage": [
            "Compter les lignes de code",
            "Mesurer la taille d'un fichier texte",
            "Dans les scripts pour le comptage",
        ],
        "visual": """
    $ wc fichier.txt
      42   150  1200 fichier.txt
      ↑     ↑     ↑
    lignes mots  octets
        """,
    },
    "sort": {
        "category": "Utilitaires",
        "description": "Trie les lignes d'un fichier",
        "syntaxe": "sort [OPTIONS] [FICHIER...]",
        "options": {
            "-r": "Ordre inverse",
            "-n": "Tri numérique",
            "-k N": "Trie selon la N-ième colonne",
            "-t": "Délimiteur de champ",
            "-u": "Lignes uniques",
        },
        "exemples": [
            ("sort fichier.txt", "Trie alphabétique"),
            ("sort -n nombres.txt", "Trie numérique"),
            ("sort -k 3 -n data.csv", "Trie par 3ème colonne numérique"),
            ("sort fichier | uniq", "Lignes uniques triées"),
        ],
        "cas_usage": [
            "Trier des données",
            "Trier par colonne spécifique",
            "Préparer des données pour l'analyse",
        ],
        "visual": """
    $ sort nombres.txt
    1
    5
    10
    100
    
    $ sort -n nombres.txt  ← correct!
    1
    5
    10
    100
        """,
    },
    "uniq": {
        "category": "Utilitaires",
        "description": "Filtre les lignes adjacentes identiques",
        "syntaxe": "uniq [OPTIONS] [FICHIER]",
        "options": {
            "-c": "Compte les occurrences",
            "-d": "Affiche seulement les doublons",
            "-u": "Affiche seulement les uniques",
        },
        "exemples": [
            ("sort fichier | uniq", "Lignes uniques"),
            ("sort fichier | uniq -c", "Compte chaque ligne"),
        ],
        "cas_usage": [
            "Compter les occurrences",
            "Supprimer les doublons",
            "Analyser des logs",
        ],
        "visual": """
    $ sort access.log | uniq -c | sort -rn | head
    542 /index.html
    301 /about.html
    120 /contact.html
      ↑
    nombre de requêtes
        """,
    },
    "history": {
        "category": "Utilitaires",
        "description": "Affiche l'historique des commandes",
        "syntaxe": "history [OPTIONS]",
        "options": {
            "-c": "Efface l'historique",
            "-d N": "Supprime la ligne N",
        },
        "exemples": [
            ("history", "Affiche tout l'historique"),
            ("history | grep apt", "Cherche dans l'historique"),
            ("!42", "Exécute la commande n°42"),
            ("!!", "Exécute la dernière commande"),
        ],
        "cas_usage": [
            "Retrouver une commande précédente",
            "Répéter une commande",
            "Chercher dans l'historique",
        ],
        "visual": """
    $ history | tail -5
    998  ls -la
    999  cd projets/
    1000  git status
    1001  sudo apt update
    1002  history
    
    $ !1001  →  exécute "sudo apt update"
    $ !!     →  exécute la dernière commande
        """,
    },
    "alias": {
        "category": "Utilitaires",
        "description": "Crée des raccourcis de commandes",
        "syntaxe": "alias NOM='COMMANDE'",
        "options": {},
        "exemples": [
            ("alias ll='ls -la'", "Crée l'alias ll"),
            ("alias", "Liste tous les alias"),
            ("unalias ll", "Supprime l'alias ll"),
        ],
        "cas_usage": [
            "Créer des raccourcis fréquents",
            "Simplifier des commandes longues",
            "Personnaliser son shell",
        ],
        "visual": """
    $ alias ll='ls -la --color=auto'
    $ alias gs='git status'
    $ alias ..='cd ..'
    
    $ ll
    total 128
    drwxr-xr-x  5 user user 4096 Jan 15 10:00 .
    ...
        """,
    },
    "crontab": {
        "category": "Utilitaires",
        "description": "Planifie des tâches récurrentes",
        "syntaxe": "crontab [OPTIONS]",
        "options": {
            "-e": "Édite le crontab",
            "-l": "Liste les tâches",
            "-r": "Supprime toutes les tâches",
        },
        "exemples": [
            ("crontab -e", "Édite les tâches planifiées"),
            ("crontab -l", "Liste les tâches"),
        ],
        "cas_usage": [
            "Sauvegardes automatiques",
            "Nettoyage de logs",
            "Mises à jour automatiques",
            "Scripts de surveillance",
        ],
        "visual": """
    # Format: minute heure jour_mois mois jour_semaine commande
    
    ┌───────────── minute (0-59)
    │ ┌───────────── heure (0-23)
    │ │ ┌───────────── jour du mois (1-31)
    │ │ │ ┌───────────── mois (1-12)
    │ │ │ │ ┌───────────── jour de la semaine (0-7, 0=dimanche)
    │ │ │ │ │
    * * * * * commande
    
    0 2 * * * /backup.sh     → tous les jours à 2h00
    */5 * * * * /check.sh    → toutes les 5 minutes
    0 0 * * 0 /weekly.sh     → tous les dimanches à minuit
        """,
    },

    # === AVANCÉ ===
    "awk": {
        "category": "Avancé",
        "description": "Traitement de texte par colonnes (langage complet)",
        "syntaxe": "awk 'PATTERN { ACTION }' FICHIER",
        "options": {
            "-F": "Délimiteur de champ",
            "-v": "Définit une variable",
        },
        "exemples": [
            ("awk '{print $1}' fichier", "Affiche la 1ère colonne"),
            ("awk -F: '{print $1}' /etc/passwd", "Noms d'utilisateurs"),
            ("awk '$3 > 100 {print $1}' data.txt", "Filtre sur la 3ème colonne"),
            ("awk '{sum+=$2} END {print sum}'", "Somme de la 2ème colonne"),
        ],
        "cas_usage": [
            "Extraire des colonnes de données",
            "Calculer des statistiques",
            "Filtrer et transformer des données",
        ],
        "visual": """
    $ cat data.txt
    Alice 25 Paris
    Bob 30 Lyon
    
    $ awk '{print $1, $3}' data.txt
    Alice Paris
    Bob Lyon
      ↑     ↑
    $1    $3
        """,
    },
    "sed": {
        "category": "Avancé",
        "description": "Éditeur de flux (modifie du texte en ligne)",
        "syntaxe": "sed [OPTIONS] 'COMMANDE' FICHIER",
        "options": {
            "-i": "Modifie le fichier en place",
            "-n": "Pas d'affichage automatique",
            "-e": "Multiple commandes",
        },
        "exemples": [
            ("sed 's/ancien/nouveau/' fichier", "Remplace la 1ère occurrence"),
            ("sed 's/ancien/nouveau/g' fichier", "Remplace toutes les occurrences"),
            ("sed -i 's/foo/bar/g' fichier", "Modifie le fichier"),
            ("sed '3d' fichier", "Supprime la ligne 3"),
            ("sed -n '5,10p' fichier", "Affiche les lignes 5 à 10"),
        ],
        "cas_usage": [
            "Remplacer du texte dans des fichiers",
            "Supprimer des lignes",
            "Extraire des lignes spécifiques",
            "Modifier en masse des fichiers de config",
        ],
        "visual": """
    sed 's/erreur/succès/g' log.txt
    
    Avant:              Après:
    erreur: connexion  →  succès: connexion
    erreur: timeout    →  succès: timeout
    
    s = substituer    g = global (toutes les occurrences)
        """,
    },
    "xargs": {
        "category": "Avancé",
        "description": "Construit et exécute des commandes à partir de l'entrée standard",
        "syntaxe": "xargs [OPTIONS] COMMANDE",
        "options": {
            "-n N": "N arguments par commande",
            "-P N": "N processus parallèles",
            "-I {}": "Remplace {} par l'argument",
            "-0": "Utilise \0 comme délimiteur",
        },
        "exemples": [
            ("find . -name '*.log' | xargs rm", "Supprime tous les .log"),
            ("cat urls.txt | xargs -n 1 curl -O", "Télécharge les URLs une par une"),
            ("find . -name '*.py' | xargs -I {} cp {} backup/", "Copie chaque .py"),
        ],
        "cas_usage": [
            "Traiter des listes de fichiers",
            "Exécuter des commandes en parallèle",
            "Combiner avec find",
        ],
        "visual": """
    find . -name '*.tmp' | xargs rm
    
    find trouve:        xargs exécute:
    ./a.tmp      ──►    rm ./a.tmp
    ./b.tmp      ──►    rm ./b.tmp
    ./c.tmp      ──►    rm ./c.tmp
        """,
    },
    "tee": {
        "category": "Avancé",
        "description": "Redirige la sortie vers fichier ET écran simultanément",
        "syntaxe": "tee [OPTIONS] FICHIER...",
        "options": {
            "-a": "Ajoute au fichier (append)",
            "-i": "Ignore les interruptions",
        },
        "exemples": [
            ("commande | tee log.txt", "Affiche ET sauvegarde"),
            ("commande | tee -a log.txt", "Ajoute au log existant"),
            ("commande | tee file1 file2", "Sauvegarde dans 2 fichiers"),
        ],
        "cas_usage": [
            "Sauvegarder la sortie tout en la voyant",
            "Créer des logs en temps réel",
            "Dupliquer la sortie vers plusieurs fichiers",
        ],
        "visual": """
    commande | tee log.txt
    
    ┌──────────┐
    │ commande │
    └────┬─────┘
         │
    ┌────┴────┐
    ▼         ▼
  écran    log.txt
  (stdout)  (fichier)
        """,
    },
    "watch": {
        "category": "Avancé",
        "description": "Exécute une commande périodiquement et affiche le résultat",
        "syntaxe": "watch [OPTIONS] COMMANDE",
        "options": {
            "-n N": "Intervalle de N secondes (défaut: 2)",
            "-d": "Met en évidence les différences",
            "-t": "Sans en-tête",
        },
        "exemples": [
            ("watch -n 1 'ps aux | grep python'", "Surveille les processus python"),
            ("watch -d ls -la", "Surveille un répertoire avec diff"),
            ("watch free -h", "Surveille la mémoire"),
        ],
        "cas_usage": [
            "Surveiller des fichiers en temps réel",
            "Monitorer des processus",
            "Observer l'utilisation des ressources",
        ],
        "visual": """
    watch -n 2 ls -la
    
    Every 2.0s: ls -la
    
    -rw-r--r-- 1 user user 1234 Jan 15 10:00 fichier.txt
                                    ↑
                              se rafraîchit toutes les 2s
        """,
    },
    "tmux": {
        "category": "Avancé",
        "description": "Multiplexeur de terminal (sessions persistantes)",
        "syntaxe": "tmux [OPTIONS] [COMMANDE]",
        "options": {},
        "exemples": [
            ("tmux new -s session1", "Nouvelle session nommée"),
            ("tmux attach -t session1", "Rejoint une session"),
            ("tmux ls", "Liste les sessions"),
        ],
        "cas_usage": [
            "Session persistante (ne meurt pas à la déconnexion)",
            "Plusieurs fenêtres dans un terminal",
            "Partager un terminal à distance",
        ],
        "visual": """
    ┌─────────────────────────────────────┐
    │ [session1] 0:bash* 1:vim- 2:top    │ ← barre de status
    ├─────────────────────────────────────┤
    │                                     │
    │   Fenêtre active (bash)             │
    │                                     │
    │   Ctrl+b c → nouvelle fenêtre       │
    │   Ctrl+b n → fenêtre suivante       │
    │   Ctrl+b d → détacher               │
    └─────────────────────────────────────┘
        """,
    },
}

# ══ CATÉGORIES ════════════════════════════════════════════════════════════════
CATEGORIES = {
    "1": ("Navigation", ["ls", "cd", "pwd", "mkdir", "rm", "cp", "mv", "touch"]),
    "2": ("Fichiers", ["cat", "less", "head", "tail", "grep", "find"]),
    "3": ("Système", ["ps", "top", "kill", "df", "du", "free", "uptime"]),
    "4": ("Réseau", ["ip", "ping", "curl", "wget", "ssh", "scp", "netstat"]),
    "5": ("Permissions", ["chmod", "chown", "sudo"]),
    "6": ("Archivage", ["tar", "gzip"]),
    "7": ("Utilitaires", ["echo", "wc", "sort", "uniq", "history", "alias", "crontab"]),
    "8": ("Avancé", ["awk", "sed", "xargs", "tee", "watch", "tmux"]),
}

# ══ FONCTIONS D'AFFICHAGE ═════════════════════════════════════════════════════
def show_command(cmd_name):
    if cmd_name not in COMMANDS:
        print(f"{C.BRIGHT_RED}✗ Commande inconnue: {cmd_name}{C.RESET}")
        return
    
    cmd = COMMANDS[cmd_name]
    
    clear()
    print_banner()
    
    # Titre
    print(f"\n{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
    print(f"{C.BOLD}{C.BRIGHT_CYAN}  📖 {cmd_name.upper()}{C.RESET}")
    print(f"{C.DIM}  {cmd['description']}{C.RESET}")
    print(f"{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}\n")
    
    # Syntaxe
    box("📝 SYNTAXE", cmd['syntaxe'], C.BRIGHT_GREEN)
    
    # Options
    if cmd['options']:
        print(f"\n{C.BRIGHT_CYAN}⚙️  OPTIONS:{C.RESET}")
        for opt, desc in cmd['options'].items():
            print(f"  {C.BRIGHT_YELLOW}{opt:<15}{C.RESET} {desc}")
    
    # Exemples
    print(f"\n{C.BRIGHT_CYAN}💡 EXEMPLES:{C.RESET}")
    for ex, desc in cmd['exemples']:
        print(f"\n  {C.BRIGHT_GREEN}$ {ex}{C.RESET}")
        print(f"  {C.DIM}→ {desc}{C.RESET}")
    
    # Cas d'usage
    print(f"\n{C.BRIGHT_CYAN}🎯 CAS D'USAGE:{C.RESET}")
    for cas in cmd['cas_usage']:
        print(f"  {C.BRIGHT_MAGENTA}•{C.RESET} {cas}")
    
    # Visuel
    if cmd['visual']:
        print(f"\n{C.BRIGHT_CYAN}🖼️  VISUALISATION:{C.RESET}")
        print(f"{C.BRIGHT_WHITE}{cmd['visual']}{C.RESET}")
    
    # Simulation interactive
    print(f"\n{C.BRIGHT_YELLOW}{'─'*70}{C.RESET}")
    print(f"{C.BRIGHT_CYAN}🎮 SIMULATION INTERACTIVE:{C.RESET}")
    
    while True:
        sim = input(f"\n{C.BRIGHT_YELLOW}Voulez-vous tester cette commande ? (o/n/démo): {C.RESET}").strip().lower()
        if sim in ['n', 'non', '']:
            break
        elif sim in ['o', 'oui']:
            custom = input(f"{C.BRIGHT_YELLOW}Entrez la commande (ex: {cmd_name} --help): {C.RESET}").strip()
            if custom:
                print(f"\n{C.BRIGHT_GREEN}$ {custom}{C.RESET}\n")
                os.system(custom)
            break
        elif sim == 'demo':
            if cmd['exemples']:
                demo_cmd = cmd['exemples'][0][0]
                print(f"\n{C.BRIGHT_GREEN}$ {demo_cmd}{C.RESET}\n")
                if cmd_name in ['rm', 'mv', 'chmod', 'chown']:
                    print(f"{C.BRIGHT_RED}⚠️  Commande sensible - exécution simulée{C.RESET}")
                else:
                    os.system(demo_cmd)
            break
    
    pause()


def show_category(cat_key):
    if cat_key not in CATEGORIES:
        return
    
    cat_name, commands = CATEGORIES[cat_key]
    
    while True:
        clear()
        print_banner()
        
        print(f"\n{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
        print(f"{C.BOLD}{C.BRIGHT_CYAN}  📂 {cat_name.upper()}{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}\n")
        
        for i, cmd in enumerate(commands, 1):
            desc = COMMANDS[cmd]['description']
            print(f"  {C.BRIGHT_GREEN}[{i}]{C.RESET} {C.BOLD}{cmd:<12}{C.RESET} {C.DIM}{desc}{C.RESET}")
        
        print(f"\n  {C.BRIGHT_RED}[0]{C.RESET} Retour au menu principal")
        
        choice = input(f"\n{C.BRIGHT_YELLOW}➤ Choix: {C.RESET}").strip()
        
        if choice == "0":
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(commands):
                show_command(commands[idx])
        except ValueError:
            pass


def quiz():
    questions = [
        ("Quelle commande liste les fichiers d'un répertoire ?", "ls"),
        ("Quelle commande affiche le répertoire courant ?", "pwd"),
        ("Quelle commande change de répertoire ?", "cd"),
        ("Quelle commande copie des fichiers ?", "cp"),
        ("Quelle commande déplace/renomme des fichiers ?", "mv"),
        ("Quelle commande supprime des fichiers ?", "rm"),
        ("Quelle commande crée un répertoire ?", "mkdir"),
        ("Quelle commande affiche le contenu d'un fichier ?", "cat"),
        ("Quelle commande cherche du texte dans des fichiers ?", "grep"),
        ("Quelle commande affiche les processus ?", "ps"),
        ("Quelle commande tue un processus ?", "kill"),
        ("Quelle commande affiche l'espace disque ?", "df"),
        ("Quelle commande teste la connectivité réseau ?", "ping"),
        ("Quelle commande change les permissions ?", "chmod"),
        ("Quelle commande archive des fichiers ?", "tar"),
    ]
    
    score = 0
    total = len(questions)
    
    clear()
    print_banner()
    print(f"\n{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
    print(f"{C.BOLD}{C.BRIGHT_CYAN}  🎮 QUIZ LINUXTUT{C.RESET}")
    print(f"{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}\n")
    
    for i, (question, answer) in enumerate(questions, 1):
        print(f"\n{C.BRIGHT_CYAN}Question {i}/{total}:{C.RESET}")
        print(f"{C.BOLD}{question}{C.RESET}")
        
        user_answer = input(f"{C.BRIGHT_YELLOW}➤ Votre réponse: {C.RESET}").strip().lower()
        
        if user_answer == answer.lower():
            print(f"{C.BRIGHT_GREEN}✓ Correct !{C.RESET}")
            score += 1
        else:
            print(f"{C.BRIGHT_RED}✗ Faux ! La réponse était: {answer}{C.RESET}")
        
        time.sleep(0.5)
    
    print(f"\n{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
    print(f"{C.BOLD}{C.BRIGHT_CYAN}  RÉSULTAT: {score}/{total}{C.RESET}")
    
    if score == total:
        print(f"{C.BRIGHT_GREEN}  🏆 Parfait ! Vous êtes un expert Linux !{C.RESET}")
    elif score >= total * 0.7:
        print(f"{C.BRIGHT_GREEN}  🌟 Très bien ! Continuez comme ça !{C.RESET}")
    elif score >= total * 0.5:
        print(f"{C.BRIGHT_YELLOW}  📚 Pas mal ! Révisez un peu et recommencez !{C.RESET}")
    else:
        print(f"{C.BRIGHT_RED}  💪 Continuez à pratiquer, vous allez y arriver !{C.RESET}")
    
    print(f"{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
    pause()


def search_command():
    clear()
    print_banner()
    
    print(f"\n{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
    print(f"{C.BOLD}{C.BRIGHT_CYAN}  🔍 RECHERCHE DE COMMANDE{C.RESET}")
    print(f"{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}\n")
    
    query = input(f"{C.BRIGHT_YELLOW}Entrez un mot-clé (nom, description, usage): {C.RESET}").strip().lower()
    
    if not query:
        return
    
    results = []
    for name, cmd in COMMANDS.items():
        if (query in name.lower() or 
            query in cmd['description'].lower() or
            any(query in ex[0].lower() for ex in cmd['exemples']) or
            any(query in cas.lower() for cas in cmd['cas_usage'])):
            results.append(name)
    
    if results:
        print(f"\n{C.BRIGHT_GREEN}✓ {len(results)} commande(s) trouvée(s):{C.RESET}\n")
        for i, cmd in enumerate(results, 1):
            print(f"  {C.BRIGHT_CYAN}[{i}]{C.RESET} {C.BOLD}{cmd}{C.RESET} - {C.DIM}{COMMANDS[cmd]['description']}{C.RESET}")
        
        choice = input(f"\n{C.BRIGHT_YELLOW}➤ Numéro à afficher (ou Entrée): {C.RESET}").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(results):
                show_command(results[idx])
        except ValueError:
            pass
    else:
        print(f"\n{C.BRIGHT_RED}✗ Aucune commande trouvée pour '{query}'{C.RESET}")
        pause()


def cheat_sheet():
    clear()
    print_banner()
    
    print(f"\n{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}")
    print(f"{C.BOLD}{C.BRIGHT_CYAN}  📋 CHEAT SHEET - COMMANDES ESSENTIELLES{C.RESET}")
    print(f"{C.BRIGHT_YELLOW}{'═'*70}{C.RESET}\n")
    
    cheats = [
        ("Navigation", [
            "ls -la          → Liste détaillée avec fichiers cachés",
            "cd ~            → Retour au home",
            "cd -            → Répertoire précédent",
            "pwd             → Chemin courant",
            "mkdir -p a/b/c  → Crée l'arborescence",
        ]),
        ("Fichiers", [
            "cat fichier     → Affiche le contenu",
            "less fichier    → Affiche page par page",
            "head -n 5 f     → 5 premières lignes",
            "tail -f log     → Suit un fichier en direct",
            "grep 'mot' f    → Cherche 'mot'",
        ]),
        ("Système", [
            "ps aux          → Tous les processus",
            "top             → Processus en temps réel",
            "kill -9 PID     → Tue un processus",
            "df -h           → Espace disque",
            "free -h         → Mémoire",
        ]),
        ("Réseau", [
            "ip addr         → Adresses IP",
            "ping google.com → Teste la connexion",
            "curl -I url     → En-têtes HTTP",
            "ssh user@host   → Connexion SSH",
            "scp file host:  → Copie sécurisée",
        ]),
        ("Permissions", [
            "chmod 755 file  → rwxr-xr-x",
            "chmod +x script → Rend exécutable",
            "chown user file → Change propriétaire",
            "sudo cmd        → En tant que root",
        ]),
        ("Avancé", [
            "cmd | grep x    → Pipe (filtre)",
            "cmd > file      → Redirection",
            "cmd >> file     → Ajoute au fichier",
            "cmd1 && cmd2    → cmd2 si cmd1 OK",
            "cmd1 || cmd2    → cmd2 si cmd1 échoue",
        ]),
    ]
    
    for title, cmds in cheats:
        print(f"\n{C.BRIGHT_CYAN}▶ {title}:{C.RESET}")
        for cmd in cmds:
            print(f"  {C.BRIGHT_GREEN}{cmd}{C.RESET}")
    
    pause()


# ══ MENU PRINCIPAL ════════════════════════════════════════════════════════════
def main():
    loading("Chargement de LINUXTUT", 2)
    
    while True:
        clear()
        print_banner()
        
        print(f"\n{C.BRIGHT_YELLOW}{'╔'+'═'*68+'╗'}{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}║{' '*20}📋 MENU PRINCIPAL{' '*31}║{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}{'╠'+'═'*68+'╣'}{C.RESET}")
        
        for key, (name, _) in CATEGORIES.items():
            print(f"{C.BRIGHT_YELLOW}║{C.RESET}  {C.BRIGHT_CYAN}[{key}]{C.RESET} {name:<55}{C.BRIGHT_YELLOW}║{C.RESET}")
        
        print(f"{C.BRIGHT_YELLOW}{'╠'+'═'*68+'╣'}{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}║{C.RESET}  {C.BRIGHT_GREEN}[S]{C.RESET} {'🔍 Rechercher une commande':<55}{C.BRIGHT_YELLOW}║{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}║{C.RESET}  {C.BRIGHT_GREEN}[Q]{C.RESET} {'🎮 Quiz interactif':<55}{C.BRIGHT_YELLOW}║{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}║{C.RESET}  {C.BRIGHT_GREEN}[C]{C.RESET} {'📋 Cheat sheet':<55}{C.BRIGHT_YELLOW}║{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}║{C.RESET}  {C.BRIGHT_RED}[0]{C.RESET} {'❌ Quitter':<55}{C.BRIGHT_YELLOW}║{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}{'╚'+'═'*68+'╝'}{C.RESET}")
        
        print(f"\n  {C.DIM}LINUXTUT v2.0 | {datetime.now().strftime('%H:%M:%S')} | {len(COMMANDS)} commandes | {len(CATEGORIES)} catégories{C.RESET}")
        
        choice = input(f"\n{C.BRIGHT_YELLOW}➤ Votre choix: {C.RESET}").strip().lower()
        
        if choice == "0" or choice == "q":
            print(f"\n{C.BRIGHT_GREEN}✓ Merci d'avoir utilisé LINUXTUT ! 🐧{C.RESET}\n")
            break
        elif choice == "s":
            search_command()
        elif choice == "q":
            quiz()
        elif choice == "c":
            cheat_sheet()
        elif choice in CATEGORIES:
            show_category(choice)
        else:
            print(f"\n{C.BRIGHT_RED}✗ Option invalide{C.RESET}")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.BRIGHT_GREEN}✓ Au revoir ! 🐧{C.RESET}\n")
        sys.exit(0)
