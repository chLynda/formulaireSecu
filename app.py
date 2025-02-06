from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sqlite3
import hashlib
import os

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'static/images'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL)''')
    
    # Création d'un utilisateur de test
    test_user = 'lyndaa'
    test_pass = hashlib.sha256('lyndaa123*'.encode()).hexdigest()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (test_user, test_pass))
    except sqlite3.IntegrityError:
        pass  # L'utilisateur existe déjà
    
    conn.commit()
    conn.close()

init_db()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message': 'Veuillez remplir tous les champs'})
    
    # Hachage du mot de passe
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = c.fetchone()
    conn.close()
    
    if user:
        return jsonify({'success': True, 'message': 'Vous êtes connecté'})
    else:
        return jsonify({'success': False, 'message': 'Identifiant ou mot de passe incorrect'})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'success': False, 'message': 'Veuillez remplir tous les champs'})
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        success = True
        message = 'Compte créé avec succès'
    except sqlite3.IntegrityError:
        success = False
        message = 'Cet identifiant existe déjà'
    finally:
        conn.close()
    
    return jsonify({'success': success, 'message': message})

if __name__ == '__main__':
    app.run(debug=True)