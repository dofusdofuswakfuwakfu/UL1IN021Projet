import sqlite3
from argon2 import PasswordHasher

ph = PasswordHasher()
con = sqlite3.connect('comptes.db')
cur = con.cursor()

def creer_cpt(pseudo: str, mdp: str) -> bool:
    """ Fonction pour créer un compte à partir d'un pseudo et un mot de
        passe à définir par l'utilisateur.
        Retourne False si le pseudo est déjà dans la base de données,
        True sinon.
    """

    # Verification de l'unicité du pseudo
    res = cur.execute(f"""SELECT * FROM Compte WHERE LOWER(cpt_pseudo) = '{pseudo.lower()}'""")
    if res.fetchall() != []:
        return False

    nv_mdp = hash_mdp(mdp)
    cur.execute(f"INSERT INTO Compte VALUES('{pseudo}', '{nv_mdp}', NULL, NULL, 0, 0)")
    con.commit()
    return True

def afficher_cpt() -> None:
    """ Affiche l'ensemble de comptes crées sur le site.
    """
    res = cur.execute("SELECT * FROM Compte")
    print(res.fetchall())
    return None

def hash_mdp(mdp: str) -> str:
    """ Fonction de hash en utilisant la librairie argon2-cffi.
        La compréhension du fonctionnement est hors de ma portée,
        malheureusement...
    """
    res = ph.hash(mdp)
    return res

def supprimer_cpt(pseudo: str) -> bool:
    """ Supprime un compte depuis son pseudo.
        Retourne True si la suppression est réussie, False sinon.
        
        TODO: mettre à jour la base de données niveaux
        lorsque le compte est supprimé. 
    """
    res = cur.execute(f"DELETE FROM Compte WHERE cpt_pseudo = '{pseudo}'")
    con.commit()
    return True

def se_connecter(pseudo: str, mdp: str) -> bool:
    """ Retourne True si le pseudo et le mot de passe correspondent dans la BD,
        False sinon.
    """
    res = cur.execute(f"""SELECT * FROM Compte WHERE
                        (cpt_pseudo = '{pseudo}')
                        """)
    mdp_hashed = res.fetchone()[1]
    try:
        ph.verify(mdp_hashed, mdp)
        return True
    except Exception:
        return False

# Tests
# Le mot de passe de lolou est 123
# Le mot de passe de haha est 123 aussi. 
if __name__ == '__main__':
    print(se_connecter('lolou', '123'))
    print(se_connecter('haha', '123'))
    res = cur.execute("""SELECT cpt_mdp FROM COMPTE""")
    print(res.fetchall())
