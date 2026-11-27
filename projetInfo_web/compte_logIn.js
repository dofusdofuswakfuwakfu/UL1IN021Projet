const pseudoUtilisateur = document.querySelector("#pseudo");
const mdp1 = document.querySelector("#mdp1");
const mdp2 = document.querySelector("#mdp2");

function pseudo() {
    if (!monNom) {
      pseudo();
    } else {
      localStorage.setItem("nom", monNom);
      pseudo.textContent = `${monNom}`
      validitePseudo.textContent = `oui`;
    }
  }


function validerCreation(){
    if (!pseudoUtilisateur) {
        console.log('Veuillez saisir un pseudo');
    }
    let regex = new RegExp^("^(?=.*\\w)(?=.*\\d)(?=.*{8.}).*$");
    if (!regex.test(mdp1)){
        console.log('Mot de passe invalide')
    }


}