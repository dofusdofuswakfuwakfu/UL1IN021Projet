import sqlite3

con = sqlite3.connect('comptes.db')
cur = con.cursor()

def creer_cpt(pseudo: str, mdp: str) -> bool:
    """ Fonction pour créer un compte à partir d'un pseudo et un mot de
        passe à définir par l'utilisateur.
        Retourne False si le pseudo est déjà pris, si le pseudo comporte
        des caractères non autorisés, ou si le mot de passe ne respecte pas les
        contraintes.
        Retourne True si le compte a été créé.
    """
    aut = [chr(i) for i in range(48, 58)] # Chiffres de 0 à 9
    aut += [chr(i) for i in range(97, 123)] # Lettres minuscules
    aut += [chr(i) for i in range(65, 91)] # Lettres majuscules

    # Verification des caractères autorisés du pseudo
    for c in pseudo:
        if c not in aut:
            return False

    # Verification de l'unicité du pseudo
    res = cur.execute(f"""SELECT * FROM Compte WHERE LOWER(cpt_pseudo) = '{pseudo.lower()}'""")
    if res.fetchall() == []:
        return False

    nv_mdp = hash_mdp(mdp)
    cur.execute(f"INSERT INTO Compte VALUES('{pseudo}', '{mdp}', NULL, NULL, 0, 0)")
    con.commit()
    return True

def montrer_cpt() -> None:
    """ Affiche l'ensemble de comptes crées sur le site.
    """
    res = cur.execute("SELECT * FROM Compte")
    print(res.fetchall())
    return None

def hash_mdp(mdp: str) -> str:
    #TODO Mettre à jour la fonction se connecter quand cette
    #fonction sera implémentée.
    return mdp

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
    """ Retourne True si le pseudo et le mot de passe existent dans la BD,
        False sinon.
    """
    res = cur.execute(f"""SELECT * FROM Compte WHERE
                        (cpt_pseudo = '{pseudo}') AND
                        (cpt_mdp = '{mdp}')""")
    return not (res.fetchall() == [])

if __name__ == '__main__':
    print(se_connecter('lolou', '1234'))
    montrer_cpt()