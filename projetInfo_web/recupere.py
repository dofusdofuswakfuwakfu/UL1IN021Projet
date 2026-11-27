from flask import Flask, request

app = Flask(__name__)

@app.route("/creation", methods=["POST"])
def creation():
    donnees = request.get_json()

    pseudo = donnees["pseudo"]
    mdp1 = donnees["mdp1"]

    return "", 200

print(mdp1)
print(pseudo)