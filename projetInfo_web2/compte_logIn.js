function validerCreation(){

  console.log("Mon fichier JavaScript est chargé !");

  const message = document.querySelector("#message");
  const pseudoUtilisateur = document.querySelector("#pseudo").value;
  const mdp1 = document.querySelector("#mdp1").value;
  const mdp2 = document.querySelector("#mdp2").value;
  const regex = /^(?=.*[a-zA-Z])(?=.*\\d){8.}$"/;

    if (pseudoUtilisateur.trim() === "") {
      alert("Veuillez saisir un pseudo");
        return;
    }
    
    if (!regex.test(mdp1)){
      alert('Mot de passe invalide')
        document.getElementById("criteres").style.color = "red"
        return;
    }

    if (mdp1 !== mdp2) {
      alert('Les mots de passe ne correspondent pas')
      return;
    }
}