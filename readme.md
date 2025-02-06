

### Technologies Utilisées
- **Frontend** : HTML, CSS, JavaScript
- **Backend** : Python avec Flask
- **Base de données** : SQLite
- **Sécurité** : Hachage SHA-256 pour les mots de passe


## Installation


2. Installez les dépendances Python :
```bash
pip install flask flask-cors
```

4. Lancez le serveur :
```bash
python app.py
```

5. Ouvrez `index.html` dans votre navigateur web

## Utilisation

### Connexion
- Accédez à l'application via le fichier index.html
- Utilisez les identifiants par défaut :
  - Identifiant : lyndaa
  - Mot de passe :lyndaa123*



### Base de données
La base de données SQLite (`users.db`) est créée automatiquement avec la table suivante :
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
```


