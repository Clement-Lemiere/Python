let my_list = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

let index = null
let valeur = ""
let longueur = 0
for (let i = 0; i<my_list.length; i++){
    //console.log(i);
    //console.log(my_list[i]);
    //console.log(my_list[i].length);
    //console.log();

    if (my_list[i].length > longueur){
        //mise à jour
        //ou stockage de la plus grande valeur rencontrée jusqu'à maintenant.
        longueur = my_list[i].length;
        //stockage des autres informations demandées
        index=i
        valeur = my_list[i]
    }

}
// console.log(index);
// console.log(valeur);
// console.log(longueur);
// console.log();

// Boucle foreach qui permet de récupérer les valeurs, mais pas l'index.

//Initialisation de l'index.
let i = 0;

//reset des données ( nécessaire car on a déjà le même algo plus haut)
index=null;
valeur="";
longueur=0;
for (let word of my_list){
    console.log(i, word, word.length);

    if (my_list[i].length > longueur){
        //mise à jour
        //ou stockage de la plus grande valeur rencontrée jusqu'à maintenant.
        longueur = my_list[i].length;
        //stockage des autres informations demandées
        index=i
        valeur = my_list[i]
    }
    //incrément de l'index/
    i++;
}